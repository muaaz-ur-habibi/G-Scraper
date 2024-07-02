import unittest

# import the functions to run the tests on
from core.inputDataCleaners import clean_input_elements_list, clean_input_payloads_list


class TestingDataCleanersOutput(unittest.TestCase):
    global test_payload_data_1, test_url_data_1, test_element_data_1, test_payload_data_2, test_url_data_2, test_element_data_2

    test_payload_data_1 = [{'for site': 'https://huggingface.co/models?search=rubert', 'type': 'no parameter', 'param': '', 'param value': ''}]
    test_payload_data_2 = [{'for site': 'https://pytorch.org/tutorials/beginner/chatbot_tutorial.html#define-models', 'type': 'headers', 'param': 'Cookie', 'param value': '_fbp=fb.1.1712907696429.2055526304; hubspotutk=8da0d66ba9d4e77efc22a2a2a8c534c1; __hssrc=1; _ga_H7XD4VJ0CX=GS1.1.1715948892.2.1.1715949480.60.0.0; _ga=GA1.1.1099604727.1712907698; _gcl_au=1.1.2145983265.1719729679; _ga_469Y0W5V62=GS1.1.1719916318.7.0.1719916318.0.0.0; _ga_VWZ4V8CGRF=GS1.1.1719916360.5.0.1719916360.0.0.0; __hstc=132719121.8da0d66ba9d4e77efc22a2a2a8c534c1.1712907736757.1719902878361.1719916376818.6; __hssc=132719121.1.1719916376818'}]

    test_element_data_1 = [{'name': 'h4', 'attribute': 'class', 'attribute value': 'text-md truncate font-mono text-black dark:group-hover/repo:text-yellow-500 group-hover/repo:text-indigo-600 text-smd', 'for site': 'https://huggingface.co/models?search=rubert'}]
    test_element_data_2 = [{'name': 'h3', 'attribute': '', 'attribute value': '', 'for site': 'https://pytorch.org/tutorials/beginner/chatbot_tutorial.html#define-models'}]

    test_url_data_1 = [{'url': 'https://huggingface.co/models?search=rubert', 'request type': 'GET'}]
    test_url_data_2 = [{'url': 'https://pytorch.org/tutorials/beginner/chatbot_tutorial.html#define-models', 'request type': 'GET'}]


    def test_payload_input_cleaner_case1(self):
        self.assertIsInstance(clean_input_payloads_list(payload_list=test_payload_data_1), list)
        self.assertEqual(clean_input_payloads_list(payload_list=test_payload_data_1), [{'for site': 'https://huggingface.co/models?search=rubert', 'no parameter': {'value': 'true'}}])

    def test_payload_input_cleaner_case2(self):
        self.assertIsInstance(clean_input_payloads_list(payload_list=test_payload_data_1), list)
        self.assertEqual(clean_input_payloads_list(payload_list=test_payload_data_2), [{'for site': 'https://pytorch.org/tutorials/beginner/chatbot_tutorial.html#define-models', 'headers': {'Cookie': '_fbp=fb.1.1712907696429.2055526304; hubspotutk=8da0d66ba9d4e77efc22a2a2a8c534c1; __hssrc=1; _ga_H7XD4VJ0CX=GS1.1.1715948892.2.1.1715949480.60.0.0; _ga=GA1.1.1099604727.1712907698; _gcl_au=1.1.2145983265.1719729679; _ga_469Y0W5V62=GS1.1.1719916318.7.0.1719916318.0.0.0; _ga_VWZ4V8CGRF=GS1.1.1719916360.5.0.1719916360.0.0.0; __hstc=132719121.8da0d66ba9d4e77efc22a2a2a8c534c1.1712907736757.1719902878361.1719916376818.6; __hssc=132719121.1.1719916376818'}, 'files': {}, 'payload': {}, 'json': {}, 'no parameter': {'value': 'false'}}])

    def test_elements_input_cleaner_case1(self):
        pass

    def test_elements_input_cleaner_case2(self):
        pass