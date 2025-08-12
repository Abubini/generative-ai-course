import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

class CodeReviewAgent:
    """Specialized agent for code review using Gemini"""
    
    def __init__(self, model_name='gemini-1.5-pro-latest'):
        # Configure the Gemini API
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Initialize the model with specific configuration
        self.model = genai.GenerativeModel(
            model_name,
            generation_config={
                "temperature": 0.3,
                "max_output_tokens": 2000,
            },
            system_instruction="""
            You are an expert code reviewer. When given code to review, provide:
            1. Code quality assessment
            2. Potential issues or bugs
            3. Suggestions for improvement
            4. Security considerations (if applicable)
            
            Be thorough but concise in your reviews.
            """
        )
    
    def review_code(self, code, language="Python"):
        """Review the provided code"""
        try:
            prompt = f"""
            Review the following {language} code:
            
            Code:
            {code}
            
            Please provide your code review:
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error during code review: {e}"

def main():
    """Test the specialized code review agent"""
    
    # Create the agent
    try:
        agent = CodeReviewAgent(model_name='gemini-1.5-flash-latest')
    except Exception as e:
        print(f"Failed to initialize agent: {e}")
        return
    
    # Sample code to review
    sample_code = """
    def calculate_fibonacci(n):
        if n <= 1:
            return n
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
    
    # Test the function
    result = calculate_fibonacci(10)
    print(result)
    """
    
    print("🔍 Code Review Agent Test (Gemini)\n")
    print("Sample Code:")
    print(sample_code)
    print("-" * 50)
    
    # Get review
    review = agent.review_code(sample_code, "Python")
    print("Code Review:")
    print(review)

if __name__ == "__main__":
    main()