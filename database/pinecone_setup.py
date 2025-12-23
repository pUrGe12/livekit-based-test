import os
import time
import uuid
from typing import List, Dict, Optional

from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone
from sentence_transformers import SentenceTransformer


class Memory:
    """
    This is the pinecone based Memory module. Shouldn't really be called memory but fine. Its simply a question answer
    based RAG. Also, the actual conversation history can be stored in a separate database I suppose...
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-m3"
        )  # This is the current "king" on the open-source leaderboard.
        self.index_name = "wise-faq"
        self.pinecone_api_key = os.getenv("pinecone_api_key")
        self.pc = Pinecone(api_key=self.pinecone_api_key)
        self.index = self.create_index()

    def create_index(self):
        """
        helper function to create indices for each memory structure
        """
        # if not already created
        if self.index_name not in [idx["name"] for idx in self.pc.list_indexes()]:
            self.pc.create_index(
                name=self.index_name,
                dimension=1024,  # BAAI/bge-m3 works with 1024 dimensions -> Its slower but accurate
                metric="cosine",  # using cosine-similary cause that works best
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )

        while not self.pc.describe_index(self.index_name).status["ready"]:
            time.sleep(1)

        return self.pc.Index(self.index_name)

    def embed(self, text: str) -> List[float]:
        """
        Create a normalized embedding for cosine similarity.
        """
        emb = self.model.encode(text, normalize_embeddings=True)
        return emb.tolist()

    def save_faq(
        self,
        question: str,
        answer: str,
        section: str,
        source: str,
        url: str,
        faq_id: Optional[str] = None,
    ) -> bool:
        """
        We should typically enforce keyword arguments here using a "*", but I will take lite on that for now. This is what
        I need to call in order to populate the database
        """
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
            self.index.upsert(
                vectors=[vector],
                namespace="anything_works",
            )
            return True
        except Exception as e:
            print(f"Failed to upsert FAQ {faq_id}: {e}")
            return False

    def query(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Semantic search over the FAQ KB.

        Returns ranked FAQ entries with scores.
        """

        embedding = self.embed(query)

        try:
            res = self.index.query(
                vector=embedding,
                top_k=top_k,
                include_metadata=True,
                namespace="anything_works",
            )

            results = []
            for match in res["matches"]:
                results.append(
                    {
                        "score": match["score"],
                        "question": match["metadata"]["question"],
                        "answer": match["metadata"]["answer"],
                        "section": match["metadata"]["section"],
                        "source": match["metadata"]["source"],
                        "url": match["metadata"]["url"],
                    }
                )

            return results

        except Exception as e:
            print(f"Query failed: {e}")
            return []
