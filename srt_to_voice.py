import srt
import asyncio
import edge_tts

with open("0608(1).srt", "r", encoding="utf-8") as f:
    subtitles = list(srt.parse(f.read()))

text = " ".join([sub.content for sub in subtitles])

async def main():
    communicate = edge_tts.Communicate(text, "vi-VN-HoaiMyNeural")
    await communicate.save("output.mp3")

asyncio.run(main())
