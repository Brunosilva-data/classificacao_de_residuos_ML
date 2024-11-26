import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

# Obtenha o caminho para o diretório em que este arquivo está
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(os.path.join(BASEDIR, '.env'))

# Função para obter uma conexão com o banco de dados Supabase
def get_db_connection():
    # Estabelece a conexão com o banco de dados usando as variáveis de ambiente
    conn = psycopg2.connect(
        host=os.getenv("SUPABASE_HOST"),  
        database=os.getenv("SUPABASE_DB"),  
        user=os.getenv("SUPABASE_USER"),
        password=os.getenv("SUPABASE_PASSWORD"),  
        port=os.getenv("SUPABASE_PORT"),  
        cursor_factory=RealDictCursor 
    )

    # Retorna a conexão aberta
    return conn
