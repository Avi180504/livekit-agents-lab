from dotenv import load_dotenv
load_dotenv()

from livekit.agents import Agent, JobContext, WorkerOptions, cli

class AIAgent(Agent):
    async def on_start(self, ctx: JobContext):
        print("🤖 AI Agent session started")

    async def on_message(self, ctx: JobContext, message: str):
        print(f"📩 User said: {message}")
        await ctx.send_text(f"AI says: I received -> {message}")

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=AIAgent,
            agent_name="ai-agent"
        )
    )

