import sqlite3
import os

from inputDataCleaners import clean_input_elements_list, clean_input_payloads_list

def create_preset(preset_name:str, url:str, elements:list, payloads:list):
    cur_dir = os.curdir
    db = sqlite3.connect(f"{cur_dir}\\data\\presets\\presets.db")
    c = db.cursor()

    

    #c.execute(f"""CREATE TABLE {preset_name} 
    #          (url VARCHAR(1000))
    #          element VARCHAR(600)
    #          payload VARCHAR(700)
    #          """)


def load_preset(preset_name:str):
    pass