# hubspot.py

import json
import secrets
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
import httpx
import asyncio
import base64
import requests
from integrations.integration_item import IntegrationItem

from redis_client import add_key_value_redis, get_value_redis, delete_key_redis

CLIENT_ID = 'XXX'
CLIENT_SECRET = 'XXX'

REDIRECT_URI = 'http://localhost:8000/integrations/hubspot/oauth2callback'
authorization_url = f'https://app.hubspot.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fintegrations%2Fhubspot%2Foauth2callback&scope=crm.objects.contacts.read%20crm.objects.companies.read%20crm.objects.deals.read'

async def authorize_hubspot(user_id, org_id):
    state_data = {
        'state': secrets.token_urlsafe(32),
        'user_id': user_id,
        'org_id': org_id
    }
    encoded_state = base64.urlsafe_b64encode(json.dumps(state_data).encode('utf-8')).decode('utf-8')
    
    auth_url = f'{authorization_url}&state={encoded_state}'
    await add_key_value_redis(f'hubspot_state:{org_id}:{user_id}', json.dumps(state_data), expire=600)

    return auth_url

async def oauth2callback_hubspot(request: Request):
    if request.query_params.get('error'):
        raise HTTPException(status_code=400, detail=request.query_params.get('error_description'))
    code = request.query_params.get('code')
    encoded_state = request.query_params.get('state')
    state_data = json.loads(base64.urlsafe_b64decode(encoded_state).decode('utf-8'))

    original_state = state_data.get('state')
    user_id = state_data.get('user_id')
    org_id = state_data.get('org_id')

    saved_state = await get_value_redis(f'hubspot_state:{org_id}:{user_id}')

    if not saved_state or original_state != json.loads(saved_state).get('state'):
        raise HTTPException(status_code=400, detail='State does not match.')

    async with httpx.AsyncClient() as client:
        response, _ = await asyncio.gather(
            client.post(
                'https://api.hubapi.com/oauth/v1/token',
                data={
                    'grant_type': 'authorization_code',
                    'code': code,
                    'redirect_uri': REDIRECT_URI,
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                },
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
            ),
            delete_key_redis(f'hubspot_state:{org_id}:{user_id}'),
        )

    await add_key_value_redis(f'hubspot_credentials:{org_id}:{user_id}', json.dumps(response.json()), expire=600)
    
    close_window_script = """
    <html>
        <script>
            window.close();
        </script>
    </html>
    """
    return HTMLResponse(content=close_window_script)

async def get_hubspot_credentials(user_id, org_id):
    credentials = await get_value_redis(f'hubspot_credentials:{org_id}:{user_id}')
    if not credentials:
        raise HTTPException(status_code=400, detail='No credentials found.')
    credentials = json.loads(credentials)
    await delete_key_redis(f'hubspot_credentials:{org_id}:{user_id}')

    return credentials

def create_integration_item_metadata_object(
    response_json: dict, item_type: str
) -> IntegrationItem:
    """Creates an integration metadata object from the HubSpot response"""
    integration_item_metadata = IntegrationItem(
        id=str(response_json.get('id', None)),
        name=response_json.get('properties', {}).get('firstname', '') + ' ' + response_json.get('properties', {}).get('lastname', '') if item_type == 'Contact' 
              else response_json.get('properties', {}).get('name', '') if item_type == 'Company'
              else response_json.get('properties', {}).get('dealname', ''),
        type=item_type,
        creation_time=response_json.get('createdAt', None),
        last_modified_time=response_json.get('updatedAt', None),
    )

    return integration_item_metadata

async def get_items_hubspot(credentials) -> list[IntegrationItem]:
    """Aggregates all metadata relevant for a HubSpot integration"""
    credentials = json.loads(credentials)
    access_token = credentials.get('access_token')
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    
    list_of_integration_item_metadata = []
    
    # Fetch Contacts
    try:
        contacts_response = requests.get(
            'https://api.hubapi.com/crm/v3/objects/contacts',
            headers=headers,
        )
        if contacts_response.status_code == 200:
            contacts = contacts_response.json().get('results', [])
            for contact in contacts:
                list_of_integration_item_metadata.append(
                    create_integration_item_metadata_object(contact, 'Contact')
                )
    except Exception as e:
        print(f'Error fetching contacts: {e}')
    
    # Fetch Companies
    try:
        companies_response = requests.get(
            'https://api.hubapi.com/crm/v3/objects/companies',
            headers=headers,
        )
        if companies_response.status_code == 200:
            companies = companies_response.json().get('results', [])
            for company in companies:
                list_of_integration_item_metadata.append(
                    create_integration_item_metadata_object(company, 'Company')
                )
    except Exception as e:
        print(f'Error fetching companies: {e}')
    
    # Fetch Deals
    try:
        deals_response = requests.get(
            'https://api.hubapi.com/crm/v3/objects/deals',
            headers=headers,
        )
        if deals_response.status_code == 200:
            deals = deals_response.json().get('results', [])
            for deal in deals:
                list_of_integration_item_metadata.append(
                    create_integration_item_metadata_object(deal, 'Deal')
                )
    except Exception as e:
        print(f'Error fetching deals: {e}')

    print(f'list_of_integration_item_metadata: {list_of_integration_item_metadata}')
    return list_of_integration_item_metadata