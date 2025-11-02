# Importa o FastAPI
from fastapi import FastAPI

# Cria a "aplicação" FastAPI
app = FastAPI()

# Define a rota principal (o "/")
# Quando alguém acessar "http://...", vai rodar essa função
@app.get("/")
def ler_raiz():
    # Retorna um JSON (dicionário python)
    return {"Olá": "Mundo!"}

# Uma rota de exemplo (pra gente testar depois)
@app.get("/items/{item_id}")
def ler_item(item_id: int):
    # O item_id vem da URL
    return {"item_id": item_id, "nome": "Item de Teste"}