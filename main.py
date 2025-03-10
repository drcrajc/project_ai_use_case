from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are an AI Hotel Reservation Bot for 'Grand Azure Hotel'. 
Your goal is to collect the required booking details step by step.
Keep track of the conversation, but do NOT repeat questions already answered.

Ask the following questions in order, one at a time:

{question_list}

Important Rules:
- **DO NOT show the conversation history or tracking data** in your response.
- **DO NOT repeat questions that have already been answered.**
- If all questions are answered, confirm the booking and end the conversation.
- Your response MUST be the next question prefixed by its number (e.g., '3. How many guests...'), 
  or the confirmation message if all questions are answered.

Current booking progress:
{progress}

User's latest input:
{question}

AI response (next question or confirmation):
"""

model = OllamaLLM(model="llama3")
questions = [
    "What is your name?",
    "What is your check-in and check-out date?",
    "How many guests will be staying?",
    "Would you like to include breakfast in your stay?",
    "What type of room would you prefer? (Standard, Deluxe, Suite)",
    "Do you have any special requests or preferences?",
    "How would you like to make the payment? (Credit Card, Debit Card, Cash, Online)?",
    "Can I have your contact number for confirmation?",
    "Do you need airport pickup service?",
    "Would you like a reminder message before your stay?"
]

def format_progress(booking_details):
    """Format current progress for the AI to understand"""
    progress = []
    for i, q in enumerate(questions, 1):
        status = "✔️" if q in booking_details else "❌"
        progress.append(f"{i}. {q} {status}")
    return "\n".join(progress)

def display_confirmation(details):
    print("\n🎉 Yay!!! Your Booking is Confirmed!! 🎉\n")
    print("Here are the details of your booking:\n")
    print("=".center(50, "="))
    print(f"{'🏨 Grand Azure Hotel Booking Confirmation 🏨'.center(50)}")
    print("=".center(50, "="))
    for i, question in enumerate(questions):
        print(f"{questions[i]}: {details.get(question, 'N/A')}")
    print("=".center(50, "="))
    print("\n📩 A confirmation email & SMS will be sent to you shortly.")
    print("Thank you for choosing Grand Azure Hotel! Have a pleasant stay. 😊")

def handle_conversation():
    booking_details = {}
    print("Welcome to Grand Azure Hotel Reservation ChatBot! Type 'exit' to quit.\n")
    
    while True:
        # Format progress to show answered/pending questions
        progress = format_progress(booking_details)
        
        # Find next unanswered question
        next_q_index = next((i for i, q in enumerate(questions) 
                            if q not in booking_details), None)
        
        # All questions answered
        if next_q_index is None:
            display_confirmation(booking_details)
            return
        
        # Prepare prompt and chain
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | model
        
        # Generate AI response
        response = chain.invoke({
            "question_list": "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)]),
            "progress": progress,
            "question": "start" if not booking_details else list(booking_details.values())[-1]
        }).strip()
        
        # Validate AI response format
        if response.lower().startswith("confirmed"):
            display_confirmation(booking_details)
            return
        
        # Parse AI's next question
        try:
            q_num = int(response.split('.')[0])
            current_q = questions[q_num-1]
        except (ValueError, IndexError):
            print("Bot: I encountered an error. Let me retry...")
            continue
        
        # Ask the question
        print(f"\nBot: {current_q}")
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Bot: Thank you for using our service. Have a great day!")
            return
        
        # Store response
        booking_details[current_q] = user_input

if __name__ == "__main__":
    handle_conversation()