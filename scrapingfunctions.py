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

    # cleaning and prettifying the payload data
    grouped_data_element_payload = {}

    # Process the list
    for entry in payload_list:
        site = entry['for site']
        entry_type = entry['type']
        if entry_type.lower() != 'no parameter':
            param = entry['param']
            param_value = entry['param value']

            # Initialize the site entry if it doesn't exist
            if site not in grouped_data_element_payload:
                grouped_data_element_payload[site] = {
                    'for site': site,
                    'headers': {},
                    'files': {},
                    'payload': {},
                    'json': {},
                    'no parameter': {'value': 'false'}
                }

            # Add the param and param value to the appropriate type
            grouped_data_element_payload[site][entry_type][param] = param_value
        else:
            if site not in grouped_data_element_payload:
                grouped_data_element_payload[site] = {
                    'for site': site,
                    'no parameter': {},
                }

            # Add the param and param value to the appropriate type
            grouped_data_element_payload[site][entry_type]['value'] = 'true'

    # Convert the grouped data into the desired format
    url_param_list = list(grouped_data_element_payload.values())


    grouped_data_element = {}

# Group the elements by 'for site'
    for entry in element_list:
        site = entry['for site']
        element = {k: v for k, v in entry.items() if k != 'for site'}

        if site not in grouped_data_element:
            grouped_data_element[site] = []

        grouped_data_element[site].append(element)

    # Convert the dictionary to the desired list of dictionaries format
    print(url_list)
    element_with_url_list = [{'url': site, 'elements': elements} for site, elements in grouped_data_element.items()]

    element_with_url_list = sorted(element_with_url_list, key=lambda x: [i['url'] for i in url_list].index(x['url']))

    
    for n in range(len(url_param_list)):
        print('getting url')
        url = url_list[n]['url']
        req_type = url_list[n]['request type']

        print(url)
        print(req_type)

        if url_param_list[n]['for site'] == url:
                print(url_param_list[n])
                if url_param_list[n]['no parameter']['value'] == 'false':
                    print('parameters are defined')
                    print('sending request with data')
                    element_with_url_list = element_with_url_list[n] if element_with_url_list != [] else []
                    print(element_with_url_list)
                    r = threading.Thread(target=request_executor, args=(url, url_param_list[n], element_with_url_list, req_type))
                    r.start()
                elif url_param_list[n]['no parameter']['value'] == 'true':
                    print('no parameters')
                    if req_type == 'GET':
                        print('sending get request without data')
                        r = threading.Thread(target=request_executor, args=(url, url_param_list[n], element_with_url_list, req_type))
                        r.start()
                    elif req_type == 'POST':
                        return error_handler('no payloads for post')



def request_executor(url, params_list, elems_list, req_type):
    if req_type == 'GET':
        print('GET request')
        if params_list['no parameter']['value'] == 'false':
            try:
                req = requ.get(url=url, headers=params_list['headers'], json=params_list['json'], data=params_list['payload'])
                print(req.status_code)
            except:
                print('connection error')
                error_handler('connection error')
        else:
            try:
                req = requ.get(url=url)
                print(req.status_code)
            except ConnectionError:
                print('connection error')
                error_handler('connection error')
    elif req_type == 'POST':
        print('POST request')
        pass



def error_handler(type_of_error:str):
    if type_of_error == 'no urls':
        return 'show nan_url error'
    
    elif type_of_error == 'no elements':
        return 'show nan_elems error'
    
    elif type_of_error == 'no payloads':
        return 'show nan_payls error'
    
    elif type_of_error == 'no payloads for post':
        return 'show post_without_payload error'


def status_returner():
    pass


def logger(**kwargs:list):
    pass