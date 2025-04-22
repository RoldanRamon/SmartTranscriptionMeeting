from pydub import AudioSegment

# Tente carregar um arquivo de áudio para verificar se o FFmpeg está funcionando
audio = AudioSegment.from_file("reuniao.mp3")
print("FFmpeg está funcionando corretamente!")
