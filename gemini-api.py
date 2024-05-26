# pip install google-generativeai
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY") # Replace with your API Key

# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel

# Configurations
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Safety measures
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

# Creating the model
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash", # Using flash model, You can also use Pro
  safety_settings=safety_settings,
  generation_config=generation_config,
)

# Start a new session
chat_session = model.start_chat(
  history=[
  ]
)

# Prompts
while True:
    inp = input("Enter a prompt: ")
    response = chat_session.send_message(f"{inp}")
    print(response.text)

    ans = input("Would you like to stop? Press 'Y' for Yes and 'N' for No: ")
    match(ans):   
        case 'Y': 
          print("Thank You!")
          break
        case 'N': 
            continue
    