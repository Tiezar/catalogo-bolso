import os  # Para ler variáveis de ambiente
from fastapi import FastAPI
from sqlalchemy import create_engine, text

# --- Configuração do Banco de Dados ---

# 1. Pega a URL secreta que colocamos no Render
#    (Se não achar, usa um banco local sqlite só pra teste)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# 2. Cria o "motor" de conexão com o banco
#    (O 'connect_args' é só pra SQLite, pode ignorar se for Postgres)
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# --- Fim da Configuração ---

# Cria a aplicação FastAPI
app = FastAPI()


# --- Nossas Rotas (Endpoints) ---

@app.get("/")
def ler_raiz():
    # Vamos testar a conexão!
    # A gente abre uma conexão, executa um SQL simples e fecha.
    try:
        with engine.connect() as connection:
            # 'text()' é do SQLAlchemy, pra executar SQL puro
            result = connection.execute(text("SELECT 'Olá, banco de dados!'"))
            message = result.fetchone()[0] # Pega a primeira coluna da primeira linha
            
            return {"Olá": "Mundo!", "Status_do_Banco": message}
            
    except Exception as e:
        # Se der pau na conexão, avisa
        return {"Olá": "Mundo!", "Status_do_Banco": f"Erro ao conectar: {e}"}


@app.get("/items/{item_id}")
def ler_item(item_id: int):
    # (Por enquanto, não vamos usar o banco aqui, só pra manter simples)
    return {"item_id": item_id, "nome": "Item de Teste"}