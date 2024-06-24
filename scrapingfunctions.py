import requests as requ
from bs4 import BeautifulSoup as bs

import time

import threading


# the main function that will run the scrape
def run(url_list:list,
        element_list:list,
        payload_list:list,
        **kwargs
        ):


    if url_list == []:
        return error_handler('no urls')
    elif element_list == [] and 'nullify_elem_error' not in kwargs.keys():
        return error_handler('no elements')
    elif payload_list == []:
        return error_handler('no payloads')
    else:
        pass
    print('scrape started')

    print('cleaning params data')
    # cleaning and prettifying the payload data
    grouped_data = {}

    print(payload_list)

    # Process the list
    for entry in payload_list:
        site = entry['for site']
        entry_type = entry['type']
        if entry_type.lower() != 'no parameter':
            param = entry['param']
            param_value = entry['param value']

            # Initialize the site entry if it doesn't exist
            if site not in grouped_data:
                grouped_data[site] = {
                    'for site': site,
                    'headers': {},
                    'files': {},
                    'payload': {},
                    'json': {},
                    'no parameter': {'value': 'false'}
                }

            # Add the param and param value to the appropriate type
            grouped_data[site][entry_type][param] = param_value
        else:
            if site not in grouped_data:
                grouped_data[site] = {
                    'for site': site,
                    'no parameter': {},
                }

            # Add the param and param value to the appropriate type
            grouped_data[site][entry_type]['value'] = 'true'

    # Convert the grouped data into the desired format
    url_param_list = list(grouped_data.values())

    
    for n in range(len(url_param_list)):
        print('getting url')
        url = url_list[n]['url']
        req_type = url_list[n]['request type']

        print(url)
        print(req_type)

        #if req_type == 'GET':
        print('get request')
        if url_param_list[n]['for site'] == url:
                if url_param_list[n]['no parameter'] == 'false':
                    print('sending request with data')
                    r = threading.Thread(target=request_executor, args=(url, url_param_list[n], req_type))
                    r.start()

                else:
                    print('sending request without data')
                    r = threading.Thread(target=request_executor, args=(url, url_param_list[n], req_type))
                    r.start()



def request_executor(url, params_list, req_type):
    print(params_list)
    if req_type == 'GET':
        if params_list['no parameter']['value'] == 'false':
            
            req = requ.get(url=url, headers=params_list['headers'], json=params_list['json'], data=params_list['payload'])
        else:
            req = requ.get(url=url)
            print(req.text)
    pass



def error_handler(type_of_error:str):
    if type_of_error == 'no urls':
        return 'show nan_url error'
    
    elif type_of_error == 'no elements':
        return 'show nan_elems error'
    
    elif type_of_error == 'no payloads':
        return 'show nan_payls error'
    
def status_returner():
    pass

def logger():
    pass