import pandas as pd 
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

# Lista dos arquivos de áudio que você deseja transcrever
audio_files = ["segment_0.mp3"]

# Dicionário para armazenar as transcrições
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

# Combina todas as transcrições em um único texto
full_transcription = "\n\n".join(transcriptions.values())

# Salva a transcrição completa em um arquivo de texto
with open("transcricao_completa.txt", "w", encoding='utf-8') as f:
    f.write(full_transcription)
print("Transcrição completa salva em transcricao_completa.txt.")

# Agora, use o modelo GPT para gerar a ata da reunião
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente que cria atas de reuniões de forma clara e concisa."},
        {"role": "user", "content": f"Aqui está a transcrição completa da reunião:\n\n{full_transcription}\n\nPor favor, crie a ata da reunião com base nessa transcrição, destacando os pontos principais, decisões tomadas e próximas ações."}
    ],
    temperature=0.7,
    max_tokens=1500
)

meeting_minutes = response.choices[0].message.content

# Imprime ou salva a ata da reunião
print("Ata da Reunião:")
print(meeting_minutes)

# Salva a ata em um arquivo de texto
with open("ata_da_reuniao.txt", "w", encoding='utf-8') as f:
    f.write(meeting_minutes)
