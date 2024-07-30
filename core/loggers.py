import os
import datetime
import random

def generate_log_file_path(prefix: str) -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    random_suffix = random.randint(0, 1000)
    log_directory = os.path.join(os.getcwd(), 'logs')
    # create directory if it doesn't exist
    os.makedirs(log_directory, exist_ok=True)
    return os.path.join(log_directory, f"{prefix}__{timestamp}__{random_suffix}.txt")

# functions that log their respective logs.
# this logs the output with elements
def element_logger(elements_logs_list:list):
    log_path = generate_log_file_path("element-log")
    with open(log_path, 'a') as logs:
        #logs.write(f"[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} elements={kwargs['element']} parameters={kwargs['parameters']}"")
        for elem_log in elements_logs_list:
            logs.write(elem_log)

# this logs the output with the entire webpage
def webpage_logger(**kwargs):
    log_path = generate_log_file_path("webpage-log")
    with open(log_path, 'a') as logs:
        logs.write(f"[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} parameters={kwargs['parameters']}")

# this logs errors
def error_logger(**kwargs):
    log_path = generate_log_file_path("error-log")
    with open(log_path, 'a') as logs:
        logs.write(f"[{kwargs['request_type']}] [{kwargs['status']}] [{kwargs['time']}] url={kwargs['url']} error={kwargs['error']}")
