from pydub import AudioSegment

# Try to load an audio file to verify if FFmpeg its working
audio = AudioSegment.from_file("reuniao.mp3")
print("FFmpeg its working!")
