import requests, os
import pandas as pd
from backend.additional_methods import *


def input_data(data, terminal_output):
    log_event('Event Initiated', terminal_output, level='info')
    console_details = data
    api_token = console_details['api_token']
    console_url = console_details['console_url']
    PARAMS = {
        'Authorization': 'ApiToken '+api_token,
        'Content-Type': 'application/json'
    }

    #Validate API Token
    if validate_api(console_url, api_token) == 200:
        log_event('API token valid', terminal_output, level='info')
        create_url(console_details, PARAMS, terminal_output)
    else:
        log_event('API token invalid', terminal_output, level='warning')
    return console_details

def validate_api(console_url, api_token):
    url = console_url + '/web/api/v2.1/users/api-token-details'
    data = {
        "data": {
            "apiToken": api_token
        }
    }
    r = requests.post(url = url, json=data)
    return r.status_code

def create_url(console_details, PARAMS, terminal_output):
    console_details = console_details
    if console_details['select_type'] == 'Account':
        url = 'accountIds='+ console_details['id']
    elif console_details['select_type'] == 'Site':
        url = 'siteIds=' + console_details['id']
    elif console_details['select_type'] == 'Group':
        url = 'groupIds=' + console_details['id']
    base_url = console_details['console_url']+'/web/api/v2.1/agents/passphrases?'
    base_url = base_url + url
    extension = []
    extension.append('&limit=1000') #debug, production value 1000

    if console_details['machine_state'] == 'Decommissioned':
        extension.append('&isDecommissioned=True')

    elif console_details['machine_state'] == 'Visible on console':
        pass

    elif console_details['machine_state'] == 'Uninstalled':
        extension.append('&isUninstalled=True')
    
    elif console_details['machine_state'] == 'Migrated':
        extension.append('&consoleMigrationStatuses=Migrated,N/A,Failed,Pending')

    elif console_details['machine_state'] == 'All Endpoints':
        extension.append('&isDecommissioned=True,False')
        extension.append('&isUninstalled=True,False')
        extension.append('&consoleMigrationStatuses=Migrated,N/A,Failed,Pending')
    
    final_url = base_url + ''.join(extension)
    log_event('Final URL: ' + final_url, terminal_output, level='info')
    passphrase_generate(final_url, PARAMS, terminal_output)
    #print(final_url) #debug
    return

def passphrase_generate(final_url, PARAMS, terminal_output):
    r = requests.get(url=final_url, headers=PARAMS)
    json_file = r.json()['data']
    log_event("Status: " + str(r.status_code), terminal_output, level='info')
    log_event("CSV File Updated", terminal_output,level='info')
    while (r.json()['pagination']['nextCursor']):
        next_cursor_url = final_url + '&cursor='+r.json()['pagination']['nextCursor']
        log_event('Next URL Token: ' + next_cursor_url, terminal_output,level='info')
        r = requests.get(url=next_cursor_url, headers=PARAMS)
        log_event("Status: " + str(r.status_code), terminal_output, level='info')
        json_file = r.json()['data']    
    generate_csv(json_file, final_url,PARAMS, terminal_output)
    return

def generate_csv(json_file, final_url, PARAMS, terminal_output):
    
    # Extract base URL and query parameters
    url, query_string = final_url.split("agents/passphrases")
    query_params = query_string.lstrip("?").split("&")  # Remove "?" and split parameters

    # Extract the first parameter and determine location
    key, value = query_params[0].split("=")
    location = {
        'accountIds': 'accounts',
        'siteIds': 'sites',
    }.get(key, 'groups')  # Default to 'groups' if no match

    # Construct the final result
    final_result = f"{url}{location}/{value}"

    r = requests.get(url = final_result, headers = PARAMS)
    output_filename = r.json()
    output_filename = output_filename['data']['name'] + "-Passphrase List.csv"
    flattened_df = pd.json_normalize(json_file)
    flattened_df.to_csv(output_filename, index=False)

    log_event("CSV File Updated", terminal_output,level='info')
    log_event("Finished", terminal_output,level='info')
    return