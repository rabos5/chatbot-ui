import logging
import os
import requests
from datetime import datetime
from fastapi import APIRouter, HTTPException


logger = logging.getLogger('chatbot_ui_logger')
api_router = APIRouter()


@api_router.post('/api/chat')
async def api_chat(request: dict):
    response_status = 'success'
    response_message = 'success'
    # todo: why is 'response' an array but later on if success it's a json {} object; inconsistent for client
    response_data = {
        'response': []
    }
    response_errors = []

    message = request.get('message').strip()
    if not message:
        detail = "'message' not found in the request body"
        logger.debug(detail)
        raise HTTPException(
            status_code=400,
            detail=detail
        )
    
    sender = request.get('message').strip()
    if not sender:
        sender = f'chatbot_ui_sandbox_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

    metadata = request.get('metadata', {})

    url = os.environ['CHATBOT_API_PROTO'] + '://' + os.environ['CHATBOT_API_HOST'] + ':' + os.environ['CHATBOT_API_PORT'] + os.environ['CHATBOT_API_WEBHOOKS_PATH']
    headers = {
        'content-type': 'application/json'
    }
    request_body = {
        'message': message,
        'sender': sender,
        'metadata': metadata
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=request_body
        )
        if response.status_code != 200:
            logger.debug(f'Error -> response status code -> {response.status_code}')
            logger.debug(f'Error -> response body -> {response.text}')
            print(f'Error -> response status code -> {response.status_code}')
            print(f'Error -> response body -> {response.text}')
            # todo: why am i appending this message to response_data but if success it's a json {} object; inconsistent for client
            response_data.append("I'm sorry but I've experienced an error :( please try again soon...")
            response_errors.append(f'Error -> response status code -> {response.status_code}')
            response_errors.append(f'Error -> response body -> {response.text}')
        else:
            response_data['response'] = response.json()
    except Exception as e:
        logger.debug(f'Error -> response status code -> {response.status_code}')
        logger.debug(f'Error -> response body -> {response.text}')
        logger.debug(e)
        print(f'Error -> response status code -> {response.status_code}')
        print(f'Error -> response body -> {response.text}')
        print(e)
        response_data.append("I'm sorry but I've experienced an error :( please try again soon...")
        response_errors.append(f'Error -> response status code -> {response.status_code}')
        response_errors.append(f'Error -> response body -> {response.text}')
        response_errors.append(e)

    response = {
        'status': response_status,
        'message': response_message,
        'data': response_data,
        'errors': response_errors
    }

    return response


@api_router.get('/api/status')
def api_status():
    response_status = 'success'
    response_message = 'success'
    response_data = 'up'
    response_errors = []

    response = {
        'status': response_status,
        'message': response_message,
        'data': response_data,
        'errors': response_errors
    }

    return response


@api_router.get('/api/version')
def api_version():
    response_status = 'success'
    response_message = 'success'
    response_data = {}
    response_errors = []

    version = '0.0.1'
    response_data = {
        'version': version
    }

    response = {
        'status': response_status,
        'message': response_message,
        'data': response_data,
        'errors': response_errors
    }

    return response