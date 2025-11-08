from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "nom": "Andry", "age": 23},
    {"id": 2, "nom": "Tsanta", "age": 24},
    {"id": 3, "nom": "Leon", "age": 30}
]

@app.get('/users')
def get_all_users():
    return {"data": users, "msg": "displayed successfully", "code": 200}
