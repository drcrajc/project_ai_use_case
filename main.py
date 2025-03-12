import random
from langchain_ollama import OllamaLLM

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

def generate_booking_id():
    """Generate a unique booking reference number"""
    return f"GAH-{random.randint(100000, 999999)}"

def display_confirmation(details):
    """Display a clean booking summary with Booking ID"""
    booking_id = generate_booking_id()

    print("\n🎉 Yay!!! Your Booking is Confirmed!! 🎉\n")
    print("=".center(50, "="))
    print(f"{'🏨 Grand Azure Hotel Booking Confirmation 🏨'.center(50)}")
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
    print("Thank you for choosing Grand Azure Hotel! Have a pleasant stay. 😊")

def handle_conversation():
    model = OllamaLLM(model="llama3")  # Initialize AI Model
    
    booking_details = {}  # Store user responses
    question_list = mandatory_questions + optional_questions  # Merge all questions
    question_index = 0  

    print("\nWelcome to Grand Azure Hotel Reservation ChatBot! Type 'exit' to quit.\n")
    
    while question_index < len(question_list):
        current_q = question_list[question_index]

        print(f"\nBot: {current_q}")
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Thank you for using our service. Have a great day!")
            return
        
        booking_details[current_q] = user_input  # Store response
        question_index += 1  # Move to next question

        if question_index == len(mandatory_questions):
            print("\nBot: Great! I have collected all the necessary details. Let’s finalize your booking with a few more optional preferences.")        

    display_confirmation(booking_details)  # Show booking confirmation

if __name__ == "__main__":
    handle_conversation()
