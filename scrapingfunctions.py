import requests as requ
from bs4 import BeautifulSoup as bs

from urllib.error import *

import os

import threading
import random

import datetime



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


# this function executes the scrape i.e sending the web requests, handling errors and storing the scraped data.
def request_executor(url, params_list:dict, elems_list, req_type):
    # change the format of the parameters list to a string for the verbose output
    v_o_params_list = ' '.join(f'{i}: {j}' for i, j in params_list.items())

    # handle GET requests
    if req_type == 'GET':
        # check for any request parameters
        if params_list['no parameter']['value'] == 'false':
            # catch a connection error
            try:
                start_time = datetime.datetime.now()

                req = requ.get(url=url, headers=params_list['headers'], json=params_list['json'], data=params_list['payload'])
                code = req.status_code
                req = req.content
            except ConnectionError:
                # log the connection error
                error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error='Connection Error', request_type=req_type)
            
            except HTTPError:
                error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error='Site not found Error', request_type=req_type)
                # return the output for a user on the GUI f"Start Time: {start_time} End Time: {str(datetime.datetime.now())}"
                #return [str(datetime.datetime.now()), url, 'ERROR', v_o_params_list, 'Connection Error', 'GET', '-', 'error scrape']

            # scrape and prettify the page with bs4
            page_soup = bs(req, features='html.parser')
            scraped_page = page_soup.prettify()

            # get current working directory
            curr_dir = os.getcwd()

            # check if there are any specific elements to be scraped, else just upload the entire webpage to a file
            if elems_list == []:
                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '')}-web_scraped.txt'

                # open the save file and assign it a unique name
                with open(save_path, 'a', errors='ignore') as f_w:
                    f_w.write(scraped_page)
                    webpage_logger(time=f"Start Time: {start_time}  End Time: {str(datetime.datetime.now())}", url=url, status=code, parameters=params_list, request_type=req_type)

                    finish_time = datetime.datetime.now()
                    diff = finish_time - start_time

                    # return the output for a user on the GUI
                    #return [diff.total_seconds(),  url, 'WEBPAGE', v_o_params_list, 'no errors', 'GET', code, 'pagical scrape']

            else:
                elems = elems_list['elements']
                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '')}-elements_scraped.txt'

                # open the save file and assign it a unique name
                with open(save_path, 'a', errors='ignore') as f_a:
                    elems_logging_list = []

                    for x in elems:
                        element_scraped = page_soup.find_all(x['name'], {x['attribute']: x['attribute value']})
                        
                        for i in element_scraped:
                            # handling html tags not found errors.
                            try:
                                f_a.write(f'{str(i.text).strip()}\n')
                                elems_logging_list.append(f"[{req_type}] [{code}] [Start Time: {start_time}  End Time: {str(datetime.datetime.now())}]  url={url}  elements={x['name']}  parameters={params_list}\n")
                            except AttributeError:
                                error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error=f'{i} was not found on the webpage', request_type=req_type)
                    
                element_logger(elements_logs_list=elems_logging_list)
                            
                            # return the output for a user on the GUI
                            #return [diff.total_seconds(),  url, f"{x['name']}:::{x['attribute']}:::{x['attribute value']}", v_o_params_list, 'no errors', 'GET', code, 'elemental scrape']

        # Similiar working as above, just without any request parameters
        else:
            try:
                start_time = datetime.datetime.now()
                req = requ.get(url=url)
                code = req.status_code
                req = req.content
            except ConnectionError:
                error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error='Connection Error', request_type=req_type)
            except HTTPError:
                error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error='Site not found Error', request_type=req_type)
                # return the output for a user on the GUI
                #return [str(datetime.datetime.now()), url, 'ERROR', v_o_params_list, 'Connection Error', 'GET', '-', 'error scrape']

            page_soup = bs(req, features='html.parser')
            scraped_page = page_soup.prettify()

            curr_dir = os.getcwd()
                
            # check if there are any specific elements to be scraped, else just upload the entire webpage to a file
            if elems_list == []:

                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '')}-web_scraped.txt'

                with open(save_path, 'a', errors='ignore') as f_w:
                    f_w.write(scraped_page)
                    webpage_logger(time=f"Start Time: {start_time}  End Time: {str(datetime.datetime.now())}", url=url, status=code, parameters=params_list, request_type=req_type)

                    # Calculating the time taken to process the request
                    finish_time = datetime.datetime.now()
                    diff = finish_time - start_time

                    # return the output for a user on the GUI
                    #return [diff.total_seconds(),  url, 'WEBPAGE', v_o_params_list, 'no errors', 'GET', code, 'pagical scrape']
                
            else:
                elems = elems_list['elements']
                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '')}-elements_scraped.txt'

                # open the save file and assign it a unique name
                with open(save_path, 'a', errors='ignore') as f_a:
                    elems_logging_list = []

                    for x in elems:
                        element_scraped = page_soup.find_all(x['name'], {x['attribute']: x['attribute value']})
                        
                        for i in element_scraped:
                            # handling html tags not found errors.
                            try:
                                f_a.write(f'{str(i.text).strip()}\n')
                                elems_logging_list.append(f"[{req_type}] [{code}] [Start Time: {start_time}  End Time: {str(datetime.datetime.now())}]  url={url}  elements={x['name']}  parameters={params_list}\n")
                            except AttributeError:
                                error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error=f'{i} was not found on the webpage', request_type=req_type)
                    
                element_logger(elements_logs_list=elems_logging_list)

                            # return the output for a user on the GUI
                            #return [diff.total_seconds(),  url, f"{x['name']}:::{x['attribute']}:::{x['attribute value']}", v_o_params_list, 'no errors', 'GET', code, 'elemental scrape']
                        
    # handle POST requests
    elif req_type == 'POST':
        # catch a connection error
        try:
            start_time = datetime.datetime.now()
            req = requ.post(url=url, headers=params_list['headers'], json=params_list['json'], data=params_list['payload'])
            code = req.status_code
            req = req.content
        except ConnectionError:
            # log the connection error
            error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error='Connection Error', request_type=req_type)
        except HTTPError:
            # log the 404 error, if the site returns it
            error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error='Site not found Error', request_type=req_type)
            # return the output for a user on the GUI
            # return [str(datetime.datetime.now()), url, 'ERROR', v_o_params_list, 'Connection Error', 'GET', '-', 'error scrape']

        page_soup = bs(req, features='html.parser')
        scraped_page = page_soup.prettify()

        curr_dir = os.getcwd()

        if elems_list == []:
            save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '')}-web_scraped.txt'

            with open(save_path, 'a', errors='ignore') as f_w:
                f_w.write(scraped_page)
                # calculating time taken for scrape to 
                finish_time = datetime.datetime.now()
                diff = finish_time - start_time
                webpage_logger(time=f"Start Time: {start_time}  End Time: {str(datetime.datetime.now())}", url=url, status=code, parameters=params_list, request_type=req_type)

                

                # return the output for a user on the GUI
                #return [diff.total_seconds(),  url, 'WEBPAGE', v_o_params_list, 'no errors', 'POST', code, 'pagical scrape']
                
        else:
            elems = elems_list['elements']
            save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '')}-elements_scraped.txt'

                # open the save file and assign it a unique name
            with open(save_path, 'a', errors='ignore') as f_a:
                elems_logging_list = []

                for x in elems:
                    element_scraped = page_soup.find_all(x['name'], {x['attribute']: x['attribute value']})
                        
                    for i in element_scraped:
                            # handling html tags not found errors.
                        try:
                            f_a.write(f'{str(i.text).strip()}\n')
                            elems_logging_list.append(f"[{req_type}] [{code}] [Start Time: {start_time}  End Time: {str(datetime.datetime.now())}]  url={url}  elements={x['name']}  parameters={params_list}\n")
                        except AttributeError:
                            error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error=f'{i} was not found on the webpage', request_type=req_type)
                    
                element_logger(elements_logs_list=elems_logging_list)

                        #finish_time = datetime.datetime.now()
                        #diff = finish_time - start_time
                        
                        # return the output for a user on the GUI
                        #return [diff.total_seconds(),  url, f"{x['name']}:::{x['attribute']}:::{x['attribute value']}", v_o_params_list, 'no errors', 'POST', code, 'elemental scrape']


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


# functions that log their respective logs.
# this logs the output with elements
def element_logger(elements_logs_list:list):
    direc = os.getcwd()
    with open(f'{direc}\\logs\\element-log__{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}__{random.randint(0, 1000)}.txt', 'a') as logs:
        #logs.write(f'[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} elements={kwargs['element']} parameters={kwargs['parameters']}')
        for elem_log in elements_logs_list:
            logs.write(elem_log)

# this logs the output with the entire webpage
def webpage_logger(**kwargs):
    direc = os.getcwd()
    with open(f'{direc}\\logs\\webpage-log__{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}__{random.randint(0, 1000)}.txt', 'a') as logs:
        logs.write(f'[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} parameters={kwargs['parameters']}')

# this logs errors
def error_logger(**kwargs):
    direc = os.getcwd()
    with open(f'{direc}\\logs\\error-log__{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}__{random.randint(0, 1000)}.txt', 'a') as logs:
        logs.write(f'[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} error={kwargs['error']}')