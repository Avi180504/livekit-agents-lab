import asyncio
from livekit import rtc

LIVEKIT_URL = "wss://ai-agent-pyb9r7iv.livekit.cloud"
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBUElrd1RIOFpIRkhRZXoiLCJzdWIiOiJweXRob24tdXNlciIsIm5iZiI6MTc3MDIyNzQwNiwiZXhwIjoxNzcwMjMxMDA2LCJ2aWRlbyI6eyJyb29tIjoidGVzdC1yb29tIiwicm9vbUpvaW4iOnRydWUsImNhblB1Ymxpc2giOnRydWUsImNhblN1YnNjcmliZSI6dHJ1ZX19.Sw0ffhq0X_SPuPm2QNg1Zp6m4q-A8x0RlXI9aDu8Vpo"
ROOM_NAME = "test-room"

async def main():
    room = rtc.Room()

    @room.on("connected")
    def on_connected():
        print(f"✅ Connected to room: {ROOM_NAME}")

    @room.on("disconnected")
    def on_disconnected():
        print("❌ Disconnected from room")

    await room.connect(LIVEKIT_URL, TOKEN)

    print("📨 Sending message to agent...")
    await room.local_participant.publish_data(
        b"hello agent",
        reliable=True
    )

    # Keep connection alive so agent can respond
    await asyncio.sleep(15)

    await room.disconnect()

asyncio.run(main())
