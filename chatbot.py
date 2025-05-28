import random
import nltk
from nltk.stem import PorterStemmer

# Initialize nltk and download required resources
nltk.download("punkt")
nltk.download("punkt_tab")
stemmer = PorterStemmer()

# Sample data structure for the chatbot
data = {
    "greetings": [
        "hello", "hi", "hey", "good morning", "good afternoon", "good evening"
    ],
    "farewells": [
        "goodbye", "bye", "see you later", "farewell", "take care"
    ],
    "questions": [
        "how are you", "what is your name", "who are you", "what can you do"
    ],
    "small_talk": [
        "nice weather", "how's your day", "what's up", "tell me something"
    ],
    "responses": [
        "Hello! How can I help you today?",
        "Hi there! Nice to meet you!",
        "Hello! I'm here to chat with you.",
        "Hey! How are you doing?"
    ],
    "farewell_responses": [
        "Goodbye! Have a wonderful day!",
        "See you later! Take care!",
        "Farewell! It was nice chatting with you!",
        "Bye! Come back anytime!"
    ],
    "question_responses": [
        "I'm doing well, thank you for asking!",
        "I'm a friendly chatbot here to help you.",
        "I can chat with you about various topics!",
        "I'm your AI assistant, ready to help!"
    ],
    "small_talk_responses": [
        "That's interesting! Tell me more.",
        "I'm doing great! How about you?",
        "Not much, just here chatting with you!",
        "That sounds nice! What else is on your mind?"
    ]
}

# Map intent categories to their corresponding response categories
INTENT_RESPONSE_MAP = {
    "greetings": "responses",
    "farewells": "farewell_responses", 
    "questions": "question_responses",
    "small_talk": "small_talk_responses"
}

def preprocess(sentence):
    """Tokenize and stem the input sentence"""
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]

def get_response(user_input):
    """Get appropriate response based on user input"""
    processed_input = preprocess(user_input)
    
    # Check for all the pattern categories
    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            # Check if any words from the pattern match the input
            if any(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])
    
    # Fallback for unknown inputs
    return "I'm not sure how to respond to that. Could you rephrase that?"

def chat():
    """Main chat function"""
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
