import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

# List of audio files to transcribe
audio_files = ["segment_0.mp3"]

# Dictionary to store transcriptions
transcriptions = {}

for file_name in audio_files:
    with open(file_name, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="pt",
            temperature=0
        )
        transcriptions[file_name] = transcription.text

# Combine all transcriptions into a single text
full_transcription = "\n\n".join(transcriptions.values())

# Save the complete transcription to a text file
with open("transcricao_completa.txt", "w", encoding='utf-8') as f:
    f.write(full_transcription)
print("Complete transcription saved to transcricao_completa.txt.")

# Now, use the GPT model to generate the meeting minutes
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that creates meeting minutes clearly and concisely."},
        {"role": "user", "content": f"Here is the complete meeting transcription:\n\n{full_transcription}\n\nPlease create the meeting minutes based on this transcription, highlighting the main points, decisions made, and next steps."}
    ],
    temperature=0.7,
    max_tokens=1500
)

meeting_minutes = response.choices[0].message.content

# Print or save the meeting minutes
print("Meeting Minutes:")
print(meeting_minutes)

# Save the meeting minutes to a text file
with open("ata_da_reuniao.txt", "w", encoding='utf-8') as f:
    f.write(meeting_minutes)
