from fastapi import APIRouter, Request
import json


import requests

router = APIRouter()

from ..schemas import MessageSchema

DIRECT_LINE_SECRET = '3gdVaI2-pJ4.4geNcxbdv3xUOIuSpcbzKYF-MDx9MVkcJbvCqxa0qBA'
BASE_URL = 'https://directline.botframework.com/v3/directline'

headers = {
    'Authorization': f'Bearer {DIRECT_LINE_SECRET}',
    'Content-Type': 'application/json'
}

@router.post("/start_conversation")
def start_conversation():
    response = requests.post(f'{BASE_URL}/conversations', headers=headers)
    return response.json()["conversationId"]

@router.post("/send_message/{conversation_id}")
def send_message(conversation_id: str, message: MessageSchema):
    data = {
        "type": "message",
        "from": {
            "id": "user1"
        },
        "text": message.message
    }
    response = requests.post(f'{BASE_URL}/conversations/{conversation_id}/activities', headers=headers, data=json.dumps(data))
    response = requests.get(f'{BASE_URL}/conversations/{conversation_id}/activities', headers=headers)
    return response.json()["activities"][-1]["text"]

@router.get("/receive_message/{conversation_id}")
def receive_message(conversation_id: str):
    response = requests.get(f'{BASE_URL}/conversations/{conversation_id}/activities', headers=headers)    
    return response.json()["activities"][-1]["text"]