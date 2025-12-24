from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from tool import end_call, retrieve_transfer_status_data

load_dotenv(".env.local")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""
You are a wise app transfer status assistant. Be friendly to the user.

If the user's question is about the status, delay, receipt, or whereabouts of a money transfer,
call the retrieve_transfer_status_data tool with an appropriate search query.

If the question is NOT about money transfer status AND about something else related to wise,
say that you cannot answer the question and cut the call using end_call function.

Do NOT answer transfer-status questions yourself, always use the tool.

If the question is NOT about money transfer status AND also not something else related to wise, be polite in your replies but do not entertain such questions.

Always answer in short sentences.
            """,
            tools=[end_call, retrieve_transfer_status_data]
        )

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt="deepgram/nova-3:en",        # Will fix all of this later, or let this be. It's fast enough and handle interruptions!
        llm="google/gemini-2.5-flash",
        tts="elevenlabs/eleven_turbo_v2_5:cgSgspJ2msm6clMCkdW9",
        # vad=silero.VAD.load(),
        # turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )

if __name__ == "__main__":
    agents.cli.run_app(
        agents.WorkerOptions(
            entrypoint_fnc=entrypoint,
            agent_name="livekit-agent-3",
        )
    )