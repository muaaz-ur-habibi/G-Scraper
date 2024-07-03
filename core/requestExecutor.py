# file creation/manipulation libraries
import os
import datetime

# webscraping libraries
import requests as requ
from bs4 import BeautifulSoup as bs

# errors library
from urllib.error import *

# custom logging functions
from .loggers import error_logger, element_logger, webpage_logger


# this function executes the scrape i.e sending the web requests, handling errors and storing the scraped data.
def request_executor(url, params_list:dict, elems_list, req_type):
    # change the format of the parameters list to a string for the verbose output
    #v_o_params_list = ' '.join(f'{i}: {j}' for i, j in params_list.items())

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
                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '').replace('?', 'SEARCH_QUERY')}-web_scraped.txt'

                # open the save file and assign it a unique name
                with open(save_path, 'a', errors='ignore') as f_w:
                    f_w.write(scraped_page)
                    webpage_logger(time=f"Start Time: {start_time}  End Time: {str(datetime.datetime.now())}", url=url, status=code, parameters=params_list, request_type=req_type)

                    #finish_time = datetime.datetime.now()
                    #diff = finish_time - start_time

                    # return the output for a user on the GUI
                    #return [diff.total_seconds(),  url, 'WEBPAGE', v_o_params_list, 'no errors', 'GET', code, 'pagical scrape']

            else:
                elems = elems_list['elements']
                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '').replace('?', 'SEARCH_QUERY')}-elements_scraped.txt'

                # open the save file and assign it a unique name
                with open(save_path, 'a', errors='ignore') as f_a:
                    elems_logging_list = []

                    for x in elems:
                        element_scraped = page_soup.find_all(x['name'], {x['attribute']: x['attribute value']})
                        # handling the case where no elements were found
                        if element_scraped == []:
                            error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='NOT FOUND', error=f'Element {x} was not found', request_type=req_type)
                        else:
                            for i in element_scraped:
                                # handling html tags not found errors.
                                try:
                                    f_a.write(f'{str(i.text).strip()}\n')
                                    elems_logging_list.append(f"[{req_type}] [{code}] [Start Time: {start_time}  End Time: {str(datetime.datetime.now())}]  url={url}  elements={x['name']}  parameters={params_list}\n")
                                except AttributeError:
                                    error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error=f'{i} was not found on the webpage', request_type=req_type)
                
                if elems_logging_list != []:
                    element_logger(elements_logs_list=elems_logging_list)
                else:
                    pass
                            
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

                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '').replace('?', 'SEARCH_QUERY')}-web_scraped.txt'

                with open(save_path, 'a', errors='ignore') as f_w:
                    f_w.write(scraped_page)
                    webpage_logger(time=f"Start Time: {start_time}  End Time: {str(datetime.datetime.now())}", url=url, status=code, parameters=params_list, request_type=req_type)

                    # Calculating the time taken to process the request
                    #finish_time = datetime.datetime.now()
                    #diff = finish_time - start_time

                    # return the output for a user on the GUI
                    #return [diff.total_seconds(),  url, 'WEBPAGE', v_o_params_list, 'no errors', 'GET', code, 'pagical scrape']
                
            else:
                elems = elems_list['elements']
                save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '').replace('?', 'SEARCH_QUERY')}-elements_scraped.txt'

                # open the save file and assign it a unique name
                with open(save_path, 'a', errors='ignore') as f_a:
                    elems_logging_list = []

                    for x in elems:
                        element_scraped = page_soup.find_all(x['name'], {x['attribute']: x['attribute value']})
                        # handling the case where no elements were found
                        if element_scraped == []:
                            error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='NOT FOUND', error=f'Element {x} was not found', request_type=req_type)
                        else:
                            for i in element_scraped:
                                # handling html tags not found errors.
                                try:
                                    f_a.write(f'{str(i.text).strip()}\n')
                                    elems_logging_list.append(f"[{req_type}] [{code}] [Start Time: {start_time}  End Time: {str(datetime.datetime.now())}]  url={url}  elements={x['name']}  parameters={params_list}\n")
                                except AttributeError:
                                    error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error=f'{i} was not found on the webpage', request_type=req_type)
                
                if elems_logging_list != []:
                    element_logger(elements_logs_list=elems_logging_list)
                else:
                    pass

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
            save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '').replace('?', 'SEARCH_QUERY')}-web_scraped.txt'

            with open(save_path, 'a', errors='ignore') as f_w:
                f_w.write(scraped_page)
                # calculating time taken for scrape to 
                #finish_time = datetime.datetime.now()
                #diff = finish_time - start_time
                webpage_logger(time=f"Start Time: {start_time}  End Time: {str(datetime.datetime.now())}", url=url, status=code, parameters=params_list, request_type=req_type)

                

                # return the output for a user on the GUI
                #return [diff.total_seconds(),  url, 'WEBPAGE', v_o_params_list, 'no errors', 'POST', code, 'pagical scrape']
                
        else:
            elems = elems_list['elements']
            save_path = f'{curr_dir}\\data\\scraped-data\\{str(datetime.datetime.now()).split('.')[0].replace(" ", '_').replace(':', '-')}--{str(url).replace('/', '=').replace('.', '-').replace(':', '').replace('?', 'SEARCH_QUERY')}-elements_scraped.txt'

                # open the save file and assign it a unique name
            with open(save_path, 'a', errors='ignore') as f_a:
                elems_logging_list = []

                for x in elems:
                    element_scraped = page_soup.find_all(x['name'], {x['attribute']: x['attribute value']})
                    # handling the case where no elements were found
                    if element_scraped == []:
                        error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='NOT FOUND', error=f'Element {x} was not found', request_type=req_type)
                    else:
                        for i in element_scraped:
                            # handling html tags not found errors.
                            try:
                                f_a.write(f'{str(i.text).strip()}\n')
                                elems_logging_list.append(f"[{req_type}] [{code}] [Start Time: {start_time}  End Time: {str(datetime.datetime.now())}]  url={url}  elements={x['name']}  parameters={params_list}\n")
                            except AttributeError:
                                error_logger(url=url, time=f"Start Time: {start_time}   End Time: {str(datetime.datetime.now())}", status='ERROR', error=f'{i} was not found on the webpage', request_type=req_type)
                
                if elems_logging_list != []:
                    element_logger(elements_logs_list=elems_logging_list)
                else:
                    pass

                        #finish_time = datetime.datetime.now()
                        #diff = finish_time - start_time
                        
                        # return the output for a user on the GUI
                        #return [diff.total_seconds(),  url, f"{x['name']}:::{x['attribute']}:::{x['attribute value']}", v_o_params_list, 'no errors', 'POST', code, 'elemental scrape']

