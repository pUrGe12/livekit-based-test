import os
import time
import uuid
from typing import List, Dict, Optional

from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone

class Memory:
    def __init__(self):
        # NO LOCAL WEIGHTS!!!! Memory usage drops from 2GB+ to ~0MB. This was the one thing fucking it all up
        self.index_name = "wise-faq"
        self.pinecone_api_key = os.getenv("pinecone_api_key")
        self.pc = Pinecone(api_key=self.pinecone_api_key)
        
        # We use a model hosted by Pinecone. 
        # 'multilingual-e5-large' uses 1024 dimensions so we don't have to change the dimensions
        self.model_name = "multilingual-e5-large" 
        self.index = self.create_index()

    def create_index(self):
        if self.index_name not in [idx["name"] for idx in self.pc.list_indexes()]:
            self.pc.create_index(
                name=self.index_name,
                dimension=1024,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        while not self.pc.describe_index(self.index_name).status["ready"]:
            time.sleep(1)

        return self.pc.Index(self.index_name)

    def embed(self, text: str) -> List[float]:
        """
        Calls Pinecone's API to generate embeddings instead of using local CPU/RAM.
        Again we're optimizing let's goo!
        """
        # Pinecone expects a list of strings, we send one.
        res = self.pc.inference.embed(
            model=self.model_name,
            inputs=[text],
            parameters={"input_type": "passage"}
        )
        return res[0].values

    def save_faq(self, question: str, answer: str, section: str, source: str, url: str, faq_id: Optional[str] = None) -> bool:
        faq_id = faq_id or uuid.uuid4().hex
        embed_text = f"Question: {question}\nAnswer: {answer}"
        
        embedding = self.embed(embed_text)

        vector = {
            "id": faq_id,
            "values": embedding,
            "metadata": {
                "question": question,
                "answer": answer,
                "section": section,
                "source": source,
                "url": url,
            },
        }

        try:
            self.index.upsert(vectors=[vector], namespace="anything_works")
            return True
        except Exception as e:
            print(f"Failed to upsert FAQ {faq_id}: {e}")
            return False

    def query(self, query: str, top_k: int = 5) -> List[Dict]:
        # For searching, it's better to use input_type="query" 
        # So we override the default embed behavior slightly here:
        res_emb = self.pc.inference.embed(
            model=self.model_name,
            inputs=[query],
            parameters={"input_type": "query"}
        )
        embedding = res_emb[0].values

        try:
            res = self.index.query(
                vector=embedding,
                top_k=top_k,
                include_metadata=True,
                namespace="anything_works",
            )

            results = []
            for match in res["matches"]:
                results.append({
                    "score": match["score"],
                    "question": match["metadata"]["question"],
                    "answer": match["metadata"]["answer"],
                    "section": match["metadata"]["section"],
                    "source": match["metadata"]["source"],
                    "url": match["metadata"]["url"],
                })
            return results
        except Exception as e:
            print(f"Query failed: {e}")
            return []