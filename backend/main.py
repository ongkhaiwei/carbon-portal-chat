from dotenv import load_dotenv
import os

from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import StreamingResponse
from fastapi import Depends, FastAPI, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# Initialize FastAPI

app = FastAPI()
security = HTTPBasic()

# Allow CORS site
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Admin crendential
users = {
    "admin": {
        "password": "password",
        "token": "",
        "priviliged": True
    }
}

# User Verification Function
def verification(creds: HTTPBasicCredentials = Depends(security)):
    print('u:'+creds.username)
    username = creds.username
    password = creds.password
    if username in users and password == users[username]["password"]:
        print("User access is validated.")
        return True
    else:
        # From FastAPI 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Basic"},
        )

load_dotenv()

api_endpoint = os.environ['WATSONX_URL']
api_key = os.environ['WATSONX_KEY']
project_id = os.environ['PROJECT_ID']
model_id = ModelTypes.LLAMA_2_70B_CHAT

# Define wml credentials
credentials = {
    "url": api_endpoint,
    "apikey": api_key
}

# define model parameters
parameters = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 500
}

# initialize model
model = Model(
    model_id=model_id, 
    params=parameters, 
    credentials=credentials,
    project_id=project_id)

system_prompt = """[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.<</SYS>> 

{question} [/INST]
"""

@app.post("/chat")
async def api(request: Request, Verifcation = Depends(verification)):
    #If The Verification Function Successfuylly Authenticates The User Then It Will Run The Below Code
    if Verifcation:
        payload = await request.json()
        print("message = " + payload["message"])
        return StreamingResponse(model.generate_text_stream(prompt=system_prompt.replace("{question}",payload["message"])), media_type='text/event-stream')
    else:
        return {"output": "Not authenticated"}
