from livekit import api
from livekit.agents import function_tool, RunContext, get_job_context

from database.pinecone_setup import Memory

m = Memory()		# WE HAVE TO LOAD THIS ONLY ONCE, OTHERWISE COOKED ONLY


@function_tool
async def end_call(ctx: RunContext) -> str:
	"""
	Use this tool to end the call for a given context
	"""
	job_ctx = get_job_context()
	if job_ctx is None:
		print("Shouldn't happen")
		return "error"

	print(f"ending call for room: {job_ctx.room.name}")

	try:
		await job_ctx.api.room.delete_room(
			api.DeleteRoomRequest(
				room=job_ctx.room.name,
			)
		)
		print("deleted")
		return "done"

	except Exception as e:
		print(f"couldn't delete: {e}")
		return "error"


@function_tool
async def retrieve_transfer_status_data(ctx: RunContext, query: str):
	"""
	Use this tool whenever the user asks anything about their wise transfer status

	Args:
		query: The specific query for a vector DB holding a bunch of questions and answers
	"""
	job_ctx = get_job_context()
	if job_ctx is None:
		print("Dude, I will pass job context chill out")
		return ""

	print(f"Calling the rag pipeline here")

	try:
		raw = m.query(query=query)
		# This returns a list od dictionaries. We just pick the top one
		output = raw[0].get("answer", "Querying for the answer failed, the response didn't contain an answer!")
		return output

	except Exception as e:
		print(f"This happened: {e}")
		return ""