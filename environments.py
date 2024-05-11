import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa a chave MY_KEY do arquivo .env
ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_KEY")