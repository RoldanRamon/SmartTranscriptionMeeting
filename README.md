# TranscribeAudio 📝➡️📄

Transform meeting audios into automated transcriptions and minutes! 🤖✨

## Description
This project uses the power of artificial intelligence to transcribe audio files 🎤 and generate meeting minutes 📑 efficiently. It divides the audio into smaller segments, transcribes each segment using the OpenAI API, and then uses the GPT model to create concise and informative minutes.

## Features
- **Audio Splitting:** Divides large audio files into smaller parts for easier processing. ✂️
- **Automatic Transcription:** Transcribes audio segments using the OpenAI API (Whisper). 🗣️
- **Minutes Generation:** Creates detailed meeting minutes from the transcriptions, highlighting key points, decisions, and next steps. ✍️
- **Formatting:** Formats the minutes in Markdown and converts them to PDF. 🎨

## How to Use
1. **Environment Setup:**
   - Clone this repository: `git clone [Repository URL]`
   - Create a `.env` file in the project root and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_key_here
     ```
   - Install dependencies: `pip install -r requirements.txt`

2. **Audio Preparation:**
   - Place the meeting audio file (e.g., `meeting.mp3`) in the project root.
   - Run the `SplitIntoSmallerParts.py` script to split the audio into smaller segments:
     ```bash
     python SplitIntoSmallerParts.py
     ```

3. **Transcription and Minutes Generation:**
   - Run the `Transcribe.py` script to transcribe the audio segments and generate the meeting minutes:
     ```bash
     python Transcribe.py
     ```
   - The complete transcription will be saved in `transcricao_completa.txt`, and the initial meeting minutes in `ata_da_reuniao.txt`.

4. **Minutes Enhancement:**
   - Run the `GenerateMeetingMinutes.py` script to improve the meeting minutes:
        ```bash
        python GenerateMeetingMinutes.py
        ```
   - The enhanced meeting minutes will be saved in `ata_melhorada_da_reuniao.txt`.

5. **PDF Generation (Optional):**
   - Run the `RenderizarDocxToPDF.py` script to convert the Markdown minutes to PDF format:
     ```bash
     python RenderizarDocxToPDF.py
     ```
   - The PDF minutes will be saved as `resultado.pdf`.

## Important Files
- `SplitIntoSmallerParts.py`: Splits the audio file into smaller segments.
- `Transcribe.py`: Transcribes audio segments and generates the initial meeting minutes.
- `GenerateMeetingMinutes.py`: Enhances the meeting minutes.
- `RenderizarDocxToPDF.py`: Converts the minutes from Markdown to PDF.
- `transcricao_completa.txt`: Contains the complete audio transcription.
- `ata_da_reuniao.txt`: Contains the generated meeting minutes.
- `ata_melhorada_da_reuniao.txt`: Contains the enhanced meeting minutes.
- `resultado.pdf`: Contains the meeting minutes in PDF format (optional).
- `.env`: Configuration file with the OpenAI API key.

## Requirements
- Python 3.6+
- Libraries: `pydub`, `openai`, `python-dotenv`, `markdown`, `weasyprint` (check `requirements.txt`)
- FFmpeg installed for audio manipulation (required for `pydub`)
- A valid OpenAI API key

## Contribution
Contributions are always welcome! Feel free to open issues and submit pull requests. 😊

## License
This project is licensed under the [MIT License](LICENSE).