import sqlite3
import os

from .inputDataCleaners import clean_input_elements_list, clean_input_payloads_list

# web parameter formatting was quite large, due to which needed a seperate function. for easiness in maintenance
def format_to_string_params(params_list:list):
    formatted_data = []
    for item in params_list:
        for key, inner_dict in item.items():
            for inner_key, inner_value in inner_dict.items():
                formatted_data.append(f"{key}|||{inner_key}|||{inner_value}")
    return formatted_data


# function that creates presets
def create_preset(preset_name:str,
                  url_list:list,
                  elements:list,
                  payloads:list):
    cur_dir = os.getcwd().replace('\\core', '')

    # initializing the connection and the cursor
    db = sqlite3.connect(f"{cur_dir}\\data\\presets\\presets.db")
    c = db.cursor()

    cleaned_elements_list = clean_input_elements_list(element_list=elements, url_list=url_list)
    cleaned_parameters_list = clean_input_payloads_list(payload_list=payloads)

    for item in cleaned_parameters_list:
        del item['for site']
        
    cleaned_parameters_list = format_to_string_params(cleaned_parameters_list)

    # iterate over the dictionary recieved by the cleaned elements
    for item in cleaned_elements_list:
        url = item['url']
        elems = item['elements']
        elems = [f"{i['name']}|{i['attribute']}|{i['attribute value']}" for i in elems]

        print(url)
        print(elems)
        print(cleaned_parameters_list)
    

def load_preset(preset_name:str):
    pass


create_preset(preset_name='muaaz_k',
              url_list=[{'url': 'https://python.langchain.com/v0.2/docs/tutorials/chatbot/', 'request type': 'GET'}],
              elements=[{'name': 'code', 'attribute': 'class', 'attribute value': 'codeBlockLines_e6Vv', 'for site': 'https://python.langchain.com/v0.2/docs/tutorials/chatbot/'}, {'name': 'h3', 'attribute': 'class', 'attribute value': 'anchor anchorWithStickyNavbar_LWe7', 'for site': 'https://python.langchain.com/v0.2/docs/tutorials/chatbot/'}],
              payloads=[{'for site': 'https://python.langchain.com/v0.2/docs/tutorials/chatbot/', 'type': 'headers', 'param': 'Referer', 'param value': 'https://github.com/langchain-ai/langchain\n'}, {'for site': 'https://python.langchain.com/v0.2/docs/tutorials/chatbot/', 'type': 'headers', 'param': 'User-Agent', 'param value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}, {'for site': 'https://python.langchain.com/v0.2/docs/tutorials/chatbot/', 'type': 'headers', 'param': 'Cookie', 'param value': '_ga=GA1.1.1743566515.1720166178; _ga_9B66JQQH2F=GS1.1.1720178018.3.0.1720178018.0.0.0'}])