from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

apy_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=apy_key)

material = open("transcricao_completa.txt", "r").read()

prompt = f"""
You are an assistant and need to create meeting minutes, using exclusively this material: {material}
and you need to list in detail, using bullet points, what activities Ramon needs to perform.
"""

llm = client.chat.completions.create(
    model='gpt-4o-mini',
    temperature=0,
    messages=[
        {'role': 'assistant', 'content': prompt},
    ]
)

ata = llm.choices[0].message.content

print(ata)

# Salva a ata em um arquivo de texto
with open("ata_melhorada_da_reuniao.txt", "w", encoding='utf-8') as f:
    f.write(ata)
