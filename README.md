To create a .env file because  API keys, and other sensitive information will be stored.

In .env file input the format like 

PLACE=YOUR_PLACE
AI_API_KEY=GEMINI_API_KEY
NEWS_API_KEY=NEWS_API_KEY

To get GEMINI_API_KEY in this link https://aistudio.google.com/app/apikey

To get NEWS-API_KEY in this link https://newsapi.org/

if you choose any different category then change the url in line

like I'm choose techcrunch So, I'm created 

main_url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={news_api_key}'

If you choose other then change it.
