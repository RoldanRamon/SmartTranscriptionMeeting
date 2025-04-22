from pydub import AudioSegment
import math
import os

def split_audio(file_path, max_size_mb=25):
    audio = AudioSegment.from_file(file_path)
    total_length = len(audio)  # Duration in milliseconds
    avg_size_per_ms = os.path.getsize(file_path) / total_length
    max_size_bytes = max_size_mb * 1024 * 1024
    max_length = max_size_bytes / avg_size_per_ms

    segments = []
    for i in range(math.ceil(total_length / max_length)):
        start = i * max_length
        end = min((i + 1) * max_length, total_length)
        segment = audio[start:end]
        segment_path = f"segment_{i}.mp3"
        segment.export(segment_path, format="mp3", bitrate="64k")  # Adjust the bitrate as needed
        segments.append(segment_path)

    return segments

# Example usage
file_path = "reuniao.mp3"  # Use the previously converted file
segments = split_audio(file_path)
print(f"Audio split into {len(segments)} segments.")
