from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello world!'}

@app.get('/blog/all')
def get_all_blogs():
    return {"message": "All blogs"}

@app.get('/blog/{id}')
def get_blog(id:int):
    return {"message": f"Blog with id {id}"}
