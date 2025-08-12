import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

def create_simple_agent(model_name='gemini-1.5-flash-latest'):
    """Create a simple AI agent using Google Gemini"""
    
    # Configure the Gemini API
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Initialize the Gemini model
    model = genai.GenerativeModel(model_name)
    
    return model

def generate_response(model, question, max_retries=3, delay=60):
    """Generate a response with retry logic"""
    for attempt in range(max_retries):
        try:
            response = model.generate_content(
                f"You are a helpful AI assistant. Answer the following question:\n\nQuestion: {question}\n\nAnswer:",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    max_output_tokens=1000,
                )
            )
            return response.text
        except Exception as e:
            if "quota" in str(e).lower() and attempt < max_retries - 1:
                wait_time = delay * (attempt + 1)
                print(f"Quota exceeded. Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
                continue
            raise e

def main():
    """Main function to test the agent"""
    
    # Try with different models in order
    model_names = [
        'gemini-1.5-flash-latest',  # Faster, lower cost
        'gemini-1.5-pro-latest',    # More capable
        'gemini-pro'                # Legacy
    ]
    
    test_questions = [
        "What is generative AI?",
        "Explain the difference between supervised and unsupervised learning",
        "What are the main challenges in AI deployment?"
    ]
    
    print("\n🤖 Simple AI Agent Test (Google Gemini)\n")
    
    for model_name in model_names:
        print(f"\nTrying model: {model_name}")
        try:
            agent = create_simple_agent(model_name)
            
            for i, question in enumerate(test_questions, 1):
                print(f"\nQuestion {i}: {question}")
                try:
                    response = generate_response(agent, question)
                    print(f"Answer: {response}")
                except Exception as e:
                    print(f"Error with model {model_name}: {str(e)}")
                
                print("-" * 50)
                
            break  # Stop if we found a working model
            
        except Exception as e:
            print(f"Failed to initialize model {model_name}: {str(e)}")
            continue

if __name__ == "__main__":
    main()