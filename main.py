from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
	title='My API',
	description='My new API',
	version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/hello')
def hello():
   return {'message': 'Привет'}