from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
# from livekit.plugins import noise_cancellation, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from tool import end_call, retrieve_transfer_status_data

load_dotenv(".env.local")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a helpful voice AI assistant.
            You eagerly assist users with their questions by providing information from your extensive knowledge.
            Your responses are concise, to the point, and without any complex formatting or punctuation including emojis, asterisks, or other symbols.
            You are curious, friendly, and have a sense of humor.""",
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
            # Increase limits to 4GB or higher if needed
            # memory_warn_mb=4000, 
            # memory_limit_mb=8000, 
        )
    )