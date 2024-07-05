import sqlite3
import os

from inputDataCleaners import clean_input_elements_list, clean_input_payloads_list

def create_preset(preset_name:str, url:str, elements:list, payloads:list):
    cur_dir = os.getcwd().replace('\\core', '')
    try:
        db = sqlite3.connect(f"{cur_dir}\\data\\presets\\presets.db")
    except:
        open(f"{cur_dir}\\data\\presets\\presets.db")
    
    c = db.cursor()

    check_preset_exists = c.execute(f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{preset_name}';
              """).fetchall()
    # checking if the preset already exists. if it does, return an error, else create the preset
    if check_preset_exists == []:

        c.execute(f"""CREATE TABLE {preset_name} 
                  (url VARCHAR(1500),
                  element VARCHAR(700),
                  payload VARCHAR(2000))
                  """)
        print("table created")

        

        
    else:
        print("preset already exists")

def load_preset(preset_name:str):
    pass


create_preset(preset_name='muaaz', url='www.someurl.com', elements=['div|someclass|someattribute', 'p||', 'h1|someid|nani'], payloads=['Cookie|nah_i_prefer_biscuits'])