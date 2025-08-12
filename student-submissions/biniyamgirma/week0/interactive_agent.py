import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

class GeminiChatAgent:
    """Interactive chat agent using Gemini with conversation memory"""
    
    def __init__(self, model_name='gemini-1.5-flash-latest'):
        # Configure the Gemini API
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Initialize the model
        self.model = genai.GenerativeModel(
            model_name,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 1000,
            },
            system_instruction="You are a helpful, friendly AI assistant. Keep responses concise and human-like."
        )
        
        # Start the chat session
        self.chat = self.model.start_chat(history=[])
    
    def generate_response(self, user_input, max_retries=3):
        """Generate response with conversation history"""
        for attempt in range(max_retries):
            try:
                response = self.chat.send_message(user_input)
                return response.text
            except Exception as e:
                if "quota" in str(e).lower() and attempt < max_retries - 1:
                    wait_time = 60 * (attempt + 1)
                    print(f"Waiting {wait_time} seconds due to rate limits...")
                    time.sleep(wait_time)
                    continue
                print(f"Error details: {e}")  # More detailed error reporting
                raise e

def chat_interface():
    """Interactive chat interface"""
    
    print("🤖 Interactive AI Agent (Gemini)")
    print("Type 'quit' to exit\n")
    
    # Create the agent
    try:
        agent = GeminiChatAgent()
    except Exception as e:
        print(f"Failed to initialize agent: {e}")
        return
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for quit command
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! 👋")
                break
            
            # Skip empty input
            if not user_input:
                continue
            
            # Get response from agent
            response = agent.generate_response(user_input)
            print(f"AI: {response}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    chat_interface()