from openai import OpenAI

from config.settings import GROQ_API_KEY


client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)


def transcribe_audio(audio_path):

    with open(audio_path, "rb") as audio_file:

        transcript = (
            client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3"
            )
        )

    return transcript.text