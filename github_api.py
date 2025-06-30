import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

def get_repositories(query="language:python"):
    url = "https://api.github.com/search/repositories"
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"}  # Token seguro!
    response = requests.get(url, headers=headers, params={"q": query})
    return response.json()
