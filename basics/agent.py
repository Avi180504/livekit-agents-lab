from livekit.agents import Agent, WorkerOptions, cli

class SimpleAgent(Agent):
    async def on_start(self):
        print("Agent started successfully")

    async def on_message(self, message):
        print("Received:", message)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(agent_cls=SimpleAgent))
