# this module basically converts all the input data to a much more easy-to-process format

def clean_input_payloads_list(payload_list:list):
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
            if entry_type != "files":
                grouped_data_element_payload[site][entry_type][param] = str(param_value).replace('\n', '')
            else:
                grouped_data_element_payload[site][entry_type][param] = str(clean_files_data(file_path=param_value))
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

    print(url_param_list)

    return url_param_list

def clean_input_elements_list(element_list:list, url_list:list):
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

    return element_with_url_list

def clean_files_data(file_path:str):
    with open(file_path, 'rb') as file_reader:
        return file_reader.read()