import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

candidate_name = "Avam" 

candidate_qualifications = (
    "Third-year Software Engineering student; "
    "Proficient in Python for backend development and scripting; "
    "Experienced in modern Web Development frameworks (e.g., React, Node.js) for building interactive UIs; "
    "Strong grasp of data structures and algorithms."
)
prompt = (
    f"You are a helpful AI assistant providing information about a candidate. "
    f"Your interlocutor (the recruiter) is asking about Avam. "
    f"Provide details from Avam's profile and highlight their skills. "
    f"Key areas to focus on: {candidate_qualifications}. "
    f"Always maintain a professional and informative tone, focusing on technical capabilities and project experience."
)

first_message = f"Hello, I'm {candidate_name}'s AI assistant. How can I help you learn more about Avam's background and experience today?"


conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
)

client = ElevenLabs(api_key=API_KEY)
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
)


def print_agent_response(response):
    print(f"Agent: {response}")


def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")


def print_user_transcript(transcript):
    print(f"User: {transcript}")


conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

conversation.start_session()