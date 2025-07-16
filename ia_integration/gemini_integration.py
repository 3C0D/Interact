import google.generativeai as genai
import io
import base64
from PIL import Image


class GeminiIntegration:
    """
    Class to handle integration with Gemini API
    """

    def __init__(self, api_key: str, model_name: str = "gemma-3-27b"):
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)
        self.model_options = {
            "gemini-2.5-pro-exp-03-25": {
                "rpm": 5,
                "rpd": 25,
            },  # 5 requests per minute, 25 requests per day (free tier)
            "gemini-2.5-flash": {
                "rpm": 500,
                "rpd": 1500,
            },  # Example: 500 RPM, 1500 RPD (free tier, check actual limits)
            "gemma-3-27b": {
                "rpm": 10,
                "rpd": 50,
            },  # Modèle Gemma 3 (27B) - 10 RPM, 50 RPD
            "gemma-3-12b": {
                "rpm": 15,
                "rpd": 75,
            },  # Modèle Gemma 3 (12B) - 15 RPM, 75 RPD
            "gemma-3-4b": {
                "rpm": 20,
                "rpd": 100,
            },  # Modèle Gemma 3 (4B) - 20 RPM, 100 RPD
            "gemini-2.0-flash-lite-preview-02-05": {"rpm": 30},  # uses per minute
            "gemini-2.0-flash": {"rpm": 15},
            "gemini-2.0-flash-thinking-exp-01-21": {"rpm": 10},
            "gemini-2.0-pro-exp-02-05": {"rpm": 2},
        }

    def generate_content(self, prompt, chat_history=None):
        try:
            # Normalize prompt to list format
            contents = []

            if isinstance(prompt, str):
                contents.append(prompt)
            elif isinstance(prompt, list):
                for item in prompt:
                    if isinstance(item, str):
                        contents.append(item)
                    elif (
                        isinstance(item, dict)
                        and "data" in item
                        and "mime_type" in item
                    ):
                        # Handle image data: convert base64 to PIL Image
                        try:
                            image_data = base64.b64decode(item["data"])
                            image = Image.open(io.BytesIO(image_data))
                            contents.append(image)
                        except Exception:
                            contents.append(f"Error: Unable to process image")
            else:
                contents.append(str(prompt))

            if chat_history:
                chat = self.model.start_chat(history=chat_history)
                response = chat.send_message(contents)
            else:
                response = self.model.generate_content(contents)

            return response.text
        except Exception as e:
            return f"Error: {e}"
