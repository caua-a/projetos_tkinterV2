from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyCDPGBuvtBf69NqBnWD3u6dT3jO5N53H-E")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=""
)
print(response.text)