# main.py
# Enhanced Hotel Booking Chatbot using Ollama and Llama3
# Author: Cyril Robinson Azariah John Chelliah
# Student ID: 3207053
# Module: AI Use Case (DLMAIPAIUC01)

import re
import random
import time
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Define mandatory and optional questions
mandatory_questions = [
    "What is your name?",
    "What is your check-in and check-out date?",
    "How many guests will be staying?"
]

optional_questions = [
    "Would you like to include breakfast in your stay?",
    "What type of room would you prefer? (Standard, Deluxe, Suite)?",
    "How would you like to make the payment? (Credit Card, Debit Card, Cash, Online)?",
    "Can I have your contact number for confirmation?"
]

# Configuration settings
CONFIG = {
    "hotel_name": "Grand Azure Hotel",
    "temperature": 0.1,       # Lower values make responses more consistent
    "use_llm": True,          # Set to False to disable LLM responses
    "show_progress": True     # Show progress indicators during booking
}

def format_progress(booking_details):
    """Format the current booking progress with visual indicators"""
    progress = []
    all_questions = mandatory_questions + optional_questions
    
    for i, q in enumerate(all_questions, 1):
        if q in booking_details:
            progress.append(f"{i}. {q} - ✅ {booking_details[q]}")
        else:
            progress.append(f"{i}. {q} - ❌ Pending")
    return "\n".join(progress)

def generate_booking_id():
    """Generate a unique booking reference number"""
    return f"GAH-{random.randint(100000, 999999)}"

def validate_input(question, user_input):
    """Basic validation of user input based on question type"""
    if not user_input:
        return False, "Please provide a response."
        
    if "date" in question.lower():
        # Check if input contains something that looks like a date
        if not re.search(r'\d{1,4}[-/]\d{1,2}[-/]\d{1,4}|\d{1,2}[-/]\d{1,2}|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec', 
                         user_input.lower()):
            return False, "I couldn't identify a date in your response. Please try again with a date format (e.g., July 15-20, 2025)."
    
    elif "guests" in question.lower():
        # Check if input contains a number
        if not re.search(r'\d+', user_input):
            return False, "Please specify the number of guests with a digit (e.g., 2)."
    
    elif "contact number" in question.lower():
        # Check if input contains a sequence of digits that could be a phone number
        if not re.search(r'\d{5,}', user_input):
            return False, "Please provide a valid contact number with at least 5 digits."
    
    # Default case: input is valid
    return True, user_input

def display_confirmation(details):
    """Display a clean booking summary with Booking ID"""
    booking_id = generate_booking_id()

    print("\n🎉 Yay!!! Your Booking is Confirmed!! 🎉\n")
    print("=".center(50, "="))
    print(f"{'🏨 ' + CONFIG['hotel_name'] + ' Booking Confirmation 🏨'.center(50)}")
    print("=".center(50, "="))
    print(f"📌 Booking ID: {booking_id}")
    print(f"📅 Check-in & Check-out: {details.get('What is your check-in and check-out date?', 'N/A')}")
    print(f"👥 Total Guests: {details.get('How many guests will be staying?', 'N/A')}")
    print(f"🍽️ Breakfast Included: {details.get('Would you like to include breakfast in your stay?', 'No')}")
    print(f"🛏️ Room Type: {details.get('What type of room would you prefer? (Standard, Deluxe, Suite)?', 'Standard')}")
    print(f"💳 Payment Method: {details.get('How would you like to make the payment? (Credit Card, Debit Card, Cash, Online)?', 'N/A')}")
    print(f"📞 Contact Number: {details.get('Can I have your contact number for confirmation?', 'N/A')}")
    print("=".center(50, "="))
    print("\n📩 A confirmation email & SMS will be sent to you shortly.")
    print(f"Thank you for choosing {CONFIG['hotel_name']}! Have a pleasant stay. 😊")

def handle_conversation():
    """Main conversation handler with LLM integration"""
    # Initialize Ollama with Llama3
    llm = None
    if CONFIG["use_llm"]:
        try:
            llm = OllamaLLM(model="llama3", temperature=CONFIG["temperature"])
            output_parser = StrOutputParser()
            print("AI enhancement active")
        except Exception as e:
            print(f"Could not initialize language model: {e}")
            print("Continuing with standard conversation flow.")
    
    # Initialize conversation
    booking_details = {}  # Store user responses
    conversation_history = []  # Track conversation for context
    question_list = mandatory_questions + optional_questions  # Merge all questions
    question_index = 0  

    print(f"\nWelcome to {CONFIG['hotel_name']} Reservation ChatBot! Type 'exit' to quit.\n")
    print(f"Bot: Hello! I'm the {CONFIG['hotel_name']} reservation assistant. How can I help you today?")
    
    # First user input
    user_input = input("You: ").strip()
    
    if user_input.lower() == "exit":
        print(f"Bot: Thank you for using our service. Have a great day!")
        return
    
    # Add to conversation history
    conversation_history.append(f"User: {user_input}")
    
    # Welcome message
    welcome_message = f"Great! I'd be happy to help you book a room. Let's get started with your information."
    print(f"\nBot: {welcome_message}")
    conversation_history.append(f"Bot: {welcome_message}")
    
    # Show initial progress if enabled
    if CONFIG["show_progress"]:
        print("\n--- Current Booking Progress ---")
        print(format_progress(booking_details))
        print("-------------------------------\n")
    
    # Main conversation loop
    while question_index < len(question_list):
        current_q = question_list[question_index]

        print(f"\nBot: {current_q}")
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print(f"Bot: Thank you for using our service. Have a great day!")
            return
        
        # Validate input
        is_valid, validation_message = validate_input(current_q, user_input)
        if not is_valid:
            print(f"\nBot: {validation_message}")
            continue
        
        # Store valid response
        booking_details[current_q] = user_input
        conversation_history.append(f"User: {user_input}")
        
        # Move to next question
        question_index += 1
        
        # Show updated progress if enabled
        if CONFIG["show_progress"]:
            print("\n--- Current Booking Progress ---")
            print(format_progress(booking_details))
            print("-------------------------------\n")
        
        # Special message after mandatory questions
        if question_index == len(mandatory_questions):
            print("\nBot: Great! I have collected all the necessary details. Let's finalize your booking with a few more optional preferences.")        
        
        # Generate AI response for next question if available
        elif question_index < len(question_list) and llm is not None:
            try:
                # Get next question
                next_q = question_list[question_index]
                
                # Build the prompt for LLM
                prompt_template = PromptTemplate.from_template("""
You are an AI Hotel Reservation Bot for '{hotel_name}'. 
You are collecting booking information step by step.

Current booking progress:
{progress}

Recent conversation:
{conversation}

You just asked: "{current_question}" 
and the user responded: "{user_input}"

Now ask the next question politely: "{next_question}"
Make it conversational and friendly but keep it brief.
                """)
                
                # Create chain
                chain = (
                    {"progress": lambda x: format_progress(booking_details),
                     "conversation": lambda x: "; ".join(conversation_history[-3:]),
                     "current_question": lambda x: current_q,
                     "user_input": lambda x: user_input,
                     "next_question": lambda x: next_q,
                     "hotel_name": lambda x: CONFIG["hotel_name"]}
                    | prompt_template
                    | llm
                    | output_parser
                )
                
                # Get LLM response
                response = chain.invoke({})
                bot_response = response.strip()
                
                # Fallback if response is empty or too short
                if not bot_response or len(bot_response) < 5:
                    bot_response = f"Great! Now, {next_q}"
                
                print(f"\nBot: {bot_response}")
                conversation_history.append(f"Bot: {bot_response}")
                
            except Exception as e:
                # Fail silently - next loop will continue normally
                pass
            
    # Display final confirmation
    display_confirmation(booking_details)

if __name__ == "__main__":
    try:
        handle_conversation()
    except KeyboardInterrupt:
        print("\nBot: Booking process interrupted. Thank you for your interest!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try again later.")
