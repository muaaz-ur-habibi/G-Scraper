import os
import datetime
import random


# functions that log their respective logs.
# this logs the output with elements
def element_logger(elements_logs_list:list):
    direc = os.getcwd()
    with open(f"{direc}\\logs\\element-log__{str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '-')}__{random.randint(0, 1000)}.txt", 'a') as logs:
        #logs.write(f"[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} elements={kwargs['element']} parameters={kwargs['parameters']}"")
        for elem_log in elements_logs_list:
            logs.write(elem_log)

# this logs the output with the entire webpage
def webpage_logger(**kwargs):
    direc = os.getcwd()
    with open(f"{direc}\\logs\\webpage-log__{str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '-')}__{random.randint(0, 1000)}.txt", 'a') as logs:
        logs.write(f"[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} parameters={kwargs['parameters']}")

# this logs errors
def error_logger(**kwargs):
    direc = os.getcwd()
    with open(f"{direc}\\logs\\error-log__{str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '-')}__{random.randint(0, 1000)}.txt", 'a') as logs:
        logs.write(f"[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} error={kwargs['error']}")