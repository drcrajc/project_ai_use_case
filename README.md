# Grand Azure Hotel Booking Chatbot

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/langchain-latest-green.svg)](https://python.langchain.com/)
[![Ollama](https://img.shields.io/badge/ollama-latest-orange.svg)](https://ollama.com/)

A conversational AI chatbot for hotel bookings using LangChain and Ollama with Llama3.

## Project Overview

The Grand Azure Hotel Booking Chatbot provides a natural language interface for hotel reservations. It guides users through a structured booking process while maintaining a conversational feel, collecting all necessary information for a hotel stay.

## Features

- Natural conversation flow for collecting booking details
- Sequential question-answer process with progress tracking
- Visual indicators for completed and pending information
- Attractive formatting for the booking confirmation
- Basic input validation for dates, guest counts, and contact information
- Error handling and graceful recovery mechanisms
- Simple command-line interface with clear visual elements

## Requirements

- Python 3.10 or higher
- [Ollama](https://ollama.com/) installed and running locally
- Llama3 model pulled in Ollama

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hotel-booking-chatbot.git
   cd hotel-booking-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama:**
   - Follow the instructions at [ollama.com/download](https://ollama.com/download)
   - Start the Ollama service according to your OS instructions

4. **Pull the Llama3 model:**
   ```bash
   ollama pull llama3
   ```

## Usage

1. **Start the chatbot:**
   ```bash
   python main.py
   ```

2. **Follow the prompts to book your hotel stay:**
   - The chatbot will guide you through providing your name, dates, guest count, and preferences
   - Type 'exit' at any time to quit the application

3. **Receive your booking confirmation:**
   - Once all information is collected, the chatbot will display a formatted confirmation

## Example Interaction

```
Welcome to Grand Azure Hotel Reservation ChatBot! Type 'exit' to quit.

Bot: Hello! I'm the Grand Azure Hotel reservation assistant. How can I help you today?
You: I want to book a room

Bot: Great! I'd be happy to help you book a room at Grand Azure Hotel. Let's get started with your information.

Bot: What is your name?
You: John Smith

Bot: Thank you, John Smith. What is your check-in and check-out date?
You: July 15-20, 2025

Bot: Perfect! How many guests will be staying?
You: 2

Bot: Would you like to include breakfast in your stay?
You: Yes

Bot: Great choice! What type of room would you prefer? (Standard, Deluxe, Suite)
You: Deluxe

Bot: How would you like to make the payment? (Credit Card, Debit Card, Cash, Online)?
You: Credit Card

Bot: Can I have your contact number for confirmation?
You: 5551234567

🎉 Yay!!! Your Booking is Confirmed!! 🎉

==================================================
      🏨 Grand Azure Hotel Booking Confirmation 🏨      
==================================================
📌 Booking ID: GAH-753862
📅 Check-in & Check-out: July 15-20, 2025
👥 Total Guests: 2
🍳 Breakfast Included: Yes
🛏️ Room Type: Deluxe
💳 Payment Method: Credit Card
📞 Contact Number: 5551234567
==================================================

📩 A confirmation email & SMS will be sent to you shortly.
Thank you for choosing Grand Azure Hotel! Have a pleasant stay. 😊
```

## Project Structure

```
hotel_chatbot/
├── main.py                # Main chatbot application
├── README.md              # This file
├── requirements.txt       # Project dependencies
└── docs/
    ├── Abstract.md        # Project abstract
    └── Technical.md       # Technical breakdown
```

## Configuration

You can modify the configuration variables at the top of `main.py` to adjust:

- Whether to collect contact information
- Temperature setting for the language model
- How many conversation turns to remember
- Hotel name and branding

## Troubleshooting

- **ImportError: cannot import name 'Ollama'**: Make sure you're using the correct import name `OllamaLLM` which matches your version of langchain-ollama
- **Error initializing the language model**: Ensure Ollama is running and the Llama3 model is pulled
- **Slow responses**: Check your system resources, as running LLMs locally can be resource-intensive

## License

[MIT License](LICENSE)

## Author

Cyril Robinson Azariah John Chelliah  
Matriculation ID: 3207053  
AI Use Case (DLMAIPAIUC01)
