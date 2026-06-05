from llm.service import LLMService

llm = LLMService()


def analyze_call(transcript):

    messages = [
        {
            "role": "system",
            "content": """
You are a call analytics assistant.

Analyze the transcript and return:

## Call Summary

## Customer Sentiment

## Customer Intent

## Action Items

## Resolution Status

## Key Discussion Points
"""
        },
        {
            "role": "user",
            "content": transcript
        }
    ]

    return llm.generate(
        messages,
        provider="groq"
    )