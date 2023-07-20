from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.index import router as main_router
import uvicorn

load_dotenv()

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],  
)

app.include_router(main_router)


if __name__ == '__main__':
  uvicorn.run('app:app', host='localhost', port=5001, reload=True)
