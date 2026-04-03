import requests, os, json
import pandas as pd
from backend.additional_methods import *


def input_data(data, terminal_output):
#def input_data(data):
    log_event('Policy Generator Started', terminal_output, level='info')
    console_details = data
    apiToken = console_details['api_token']
    consoleUrl = console_details['console_url']
    PARAMS = {
        'Authorization': 'ApiToken '+apiToken,
        'Content-Type': 'application/json'
    }

    #Validate API Token
    if validate_api(consoleUrl, apiToken) == 200:
        log_event('API token valid', terminal_output, level='info')
        create_url(console_details, PARAMS, terminal_output)
    else:
        log_event('API token invalid', terminal_output, level='warning')
        
        #dialogbox for failed attempt

    return console_details

def validate_api(consoleUrl, apiToken):
    url = consoleUrl + '/web/api/v2.1/users/api-token-details'
    data = {
        "data": {
            "apiToken": apiToken
        }
    }
    r = requests.post(url = url, json=data)
    return r.status_code

def create_url(console_details, PARAMS, terminal_output):
    console_details = console_details
    console_url = console_details['console_url']
    account_id = console_details['account_id']
    PARAMS = PARAMS
    #Site details processing
    site_url= console_url+'web/api/v2.1/sites?accountId='+account_id+"&limit=1000"
    r = requests.get(url = site_url, headers = PARAMS)
    site_details = []
    site_request = r.json()
    site_details.append(site_request)
    while site_request['pagination']['nextCursor'] != None:
        site_url= console_url+'web/api/v2.1/sites?accountId='+account_id+'&cursor='+site_request['pagination']['nextCursor']
        r = requests.get(url = site_url, params = PARAMS)
        site_request = r.json()
        site_details.append(site_request)
        #print("Site Details Processing")
        log_event("Site Details Processing", terminal_output, level='info')

    #get Group details	
    group_data = []
    for sites in site_details:
        for siteid in sites['data']['sites']:
            dURL = console_url+"web/api/v2.1/groups?siteIds="+siteid['id']+"&limit=300"	#get groups
            r = requests.get(url = dURL, headers = PARAMS)
            data = r.json()
            data['site_name']=siteid['name']
            data['site_id']=siteid['id']
            group_data.append(data)
            #print("Group Details Processing for site: " + siteid['name'])
            log_event("Group Details Processing for site: " + siteid['name'], terminal_output, level='info')

    #get policies from S1  
    policy_data=[]	
    for i in group_data:
        for j in i['data']:
            group_id = j['id']
            dURL = console_url+'web/api/v2.1/groups/'+group_id+'/policy'
            r = requests.get(url = dURL, headers = PARAMS)
            policy_json = r.json()
            policy_json['data']["groupName"] = j['name']
            policy_json['data']["groupId"] = j['id']
            policy_json['data']["siteName"] = i['site_name']
            policy_json['data']["siteId"] = i['site_id']
            policy_data.append(policy_json)
            #print("Group Policy Processing for site:"+ i['site_name']+" Group Name: "+j['name'])
            log_event("Group Policy Processing for site: "+ i['site_name']+" || Group Name: "+j['name'], terminal_output, level='info')
            #print(policy_data)

    # Flatten the list of dictionaries into a DataFrame
    flattened_df = pd.json_normalize(policy_data)
    flattened_df.columns = [col.replace("data.", "") for col in flattened_df.columns]
    
    #outputfile name = run api to get Account name
    output_filename = console_url+'web/api/v2.1/accounts/'+account_id
    r = requests.get(url = output_filename, headers = PARAMS)
    output_filename = r.json()
    output_filename = output_filename['data']['name'] + "-Policy List.csv"
     
    flattened_df.to_csv(output_filename, index=False)

    log_event("Finished", terminal_output,level='info')
    return

