from google import genai
from dotenv import load_dotenv
import os


# ==========================================
# 1. Load Environment Variables
# ==========================================

load_dotenv()


# ==========================================
# 2. Get API Key
# ==========================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )


# ==========================================
# 3. Create Gemini Client
# ==========================================

client = genai.Client(
    api_key=api_key
)


# ==========================================
# 4. Create AI Assistant
# ==========================================

chat = client.chats.create(
    model="gemini-3.7-flash",
    config={
        "system_instruction": """
You are a helpful AI Assistant.

Your responsibilities:
- Answer questions clearly.
- Explain difficult topics simply.
- Give examples when useful.
- Help users with Python and AI concepts.
- Do not invent information.
"""
    }
)


# ==========================================
# 5. Start Assistant
# ==========================================

print("=" * 60)
print("                 AI ASSISTANT")
print("=" * 60)

print("Type 'exit' to stop.\n")


while True:

    # ======================================
    # User Prompt
    # ======================================

    user_prompt = input("You: ")


    # ======================================
    # Exit
    # ======================================

    if user_prompt.lower() == "exit":

        print("\nAssistant: Goodbye!")

        break


    try:

        # ==================================
        # Send User Prompt
        # ==================================

        response = chat.send_message(
            user_prompt
        )


        # ==================================
        # Response Handling
        # ==================================

        print("\nAssistant:")
        print(response.text)
        print()


    except Exception as e:

        # ==================================
        # Error Handling
        # ==================================

        print("\nError occurred:")
        print(e)
        print()