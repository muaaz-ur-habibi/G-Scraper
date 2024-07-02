# for seperate threads
import threading

# import the request executor function
from request_executor import request_executor


# A custom thread class that incorporates returning a value since the original one doesnt (currently not using the return so :\ )
class CustomThread(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return



# the main function that performs all the checks, calls other functions and executes them. Basically the core.
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

        # Cleaning and prettifying the payload data
    grouped_data_element_payload = {}

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

        # Convert the grouped data into a list
    url_param_list = list(grouped_data_element_payload.values())

    grouped_data_element = {}

    # Group the elements by URLs
    for entry in element_list:
        site = entry['for site']
        element = {k: v for k, v in entry.items() if k != 'for site'}

        if site not in grouped_data_element:
            grouped_data_element[site] = []

        grouped_data_element[site].append(element)

    # Convert the dictionary to the desired list of dictionaries format
    element_with_url_list = [{'url': site, 'elements': elements} for site, elements in grouped_data_element.items()]

    element_with_url_list = sorted(element_with_url_list, key=lambda x: [i['url'] for i in url_list].index(x['url']))

    # iterate through the amount of urls
    for n in range(len(url_param_list)):
        # get the url at the url index
        url = url_list[n]['url']
        # get url request type
        req_type = url_list[n]['request type']

        # check if the two url names match
        if url_param_list[n]['for site'] == url:
            # set element list as empty if no elements are found
            element_with_url_list = element_with_url_list[n] if element_with_url_list != [] else []
            if url_param_list[n]['no parameter']['value'] == 'false':
                # start the thread without any request parameters
                r = CustomThread(target=request_executor, args=(url, url_param_list[n], element_with_url_list, req_type))
                r.start()
                # Wait till a response is recieved, then send that response back to the gui
                #return r.join()
            elif url_param_list[n]['no parameter']['value'] == 'true':
                if req_type == 'GET':
                    # start the thread and pass parameters as args
                    r = CustomThread(target=request_executor, args=(url, url_param_list[n], element_with_url_list, req_type))
                    r.start()
                    # Wait till a response is recieved, then send that response back to the gui
                    #return r.join()
                
                # if the request type is a POST and no parameters are found throw an error
                elif req_type == 'POST':
                    return error_handler('no payloads for post')


# takes an error as parameter and returns appropriate error message
def error_handler(type_of_error:str):
    if type_of_error == 'no urls':
        return 'show nan_url error'
    
    elif type_of_error == 'no elements':
        return 'show nan_elems error'
    
    elif type_of_error == 'no payloads':
        return 'show nan_payls error'
    
    elif type_of_error == 'no payloads for post':
        return 'show post_without_payload error'