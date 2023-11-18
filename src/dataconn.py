import io
import json
import os
from tabs.item import Item
from utils import file_search

datafile = file_search("data.json")
settingfile = file_search("setting.json") 

def save_drop_schema(drops:dict)->dict:
    current_drop = {}
    current_drop["pbhl"] = {
        'raid': drops.get("pbhl",{}).get("raid",0),
        'noblue': drops.get("pbhl",{}).get("noblue",0),
        'coronaring': drops.get("pbhl",{}).get("coronaring",0),
        'lineagering': drops.get("pbhl",{}).get("lineagering",0),
        'intricacyring': drops.get("pbhl",{}).get("intricacyring",0),
        'goldbar': drops.get("pbhl",{}).get("goldbar",0),
        'hornbefore':drops.get("pbhl",{}).get("hornbefore",0),
        'hornafter':drops.get("pbhl",{}).get("hornafter",0)
    }
    current_drop['akasha'] = {
        'raid': drops.get("akasha",{}).get("raid",0),
        'hollowkey': drops.get("akasha",{}).get("hollowkey",0),
        'coronaring': drops.get("akasha",{}).get("coronaring",0),
        'lineagering': drops.get("akasha",{}).get("lineagering",0),
        'intricacyring': drops.get("akasha",{}).get("intricacyring",0),
        'goldbar': drops.get("akasha",{}).get("goldbar",0),
        'keybefore': drops.get("akasha",{}).get("keybefore",0),
        'keyafter': drops.get("akasha",{}).get("keyafter",0)
    }
    current_drop['gohl'] = {
        'raid': drops.get("raid",0),
        'azurite': drops.get("azurite",0),
        'coronaring': drops.get("coronaring",0),
        'lineagering': drops.get("lineagering",0),
        'intricacyring': drops.get("intricacyring",0),
        'goldbar': drops.get("goldbar",0),
        'azuritebefore': drops.get("azuritebefore",0),
        'azuriteafter': drops.get("azuritebefore",0)
    }
    current_drop['dragon'] = {
        'raid': drops.get("dragon",{}).get("raid",0),
        'trash': drops.get("dragon",{}).get("trash",0),
        'earring': drops.get("dragon",{}).get("earring",0),
        'sand': drops.get("dragon",{}).get("sand",0),
        'animabefore': drops.get("dragon",{}).get("animabefore",0),
        'animaafter': drops.get("dragon",{}).get("animaafter",0)
    }
    current_drop['revans'] = {
        'raid': drops.get("revans",{}).get("raid",0),
        'trash': drops.get("revans",{}).get("trash",0),
        'weapon': drops.get("revans",{}).get("weapon",0),
        'sand': drops.get("revans",{}).get("sand",0),
        'animabefore': drops.get("revans",{}).get("animabefore",0),
        'animaafter': drops.get("revans",{}).get("animaafter",0)
    }
    current_drop['subhl'] = {
        'raid': drops.get("subhl",{}).get("raid",0),
        'trash': drops.get("subhl",{}).get("trash",0),
        'sand': drops.get("subhl",{}).get("sand",0),
        'animabefore': drops.get("subhl",{}).get("animabefore",0),
        'animaafter': drops.get("subhl",{}).get("animaafter",0)
    }
    current_drop['custom1'] = {
        'raid': drops.get("custom1",{}).get("raid",0),
        'mat1': drops.get("custom1",{}).get("mat1",0),
        'mat2': drops.get("custom1",{}).get("mat2",0),
        'mat3': drops.get("custom1",{}).get("mat3",0),
        'mat4': drops.get("custom1",{}).get("mat4",0),
        'mat5': drops.get("custom1",{}).get("mat5",0),
        'animabefore': drops.get("custom1",{}).get("animabefore",0),
        'animaafter': drops.get("custom1",{}).get("animaafter",0)
    }
    current_drop['custom2'] = {
        'raid': drops.get("custom2",{}).get("raid",0),
        'mat1': drops.get("custom2",{}).get("mat1",0),
        'mat2': drops.get("custom2",{}).get("mat2",0),
        'mat3': drops.get("custom2",{}).get("mat3",0),
        'mat4': drops.get("custom2",{}).get("mat4",0),
        'mat5': drops.get("custom2",{}).get("mat5",0),
        'animabefore': drops.get("custom2",{}).get("animabefore",0),
        'animaafter': drops.get("custom2",{}).get("animaafter",0),
    }
    current_drop['custom3'] = {
        'raid': drops.get("custom3",{}).get("raid",0),
        'mat1': drops.get("custom3",{}).get("mat1",0),
        'mat2': drops.get("custom3",{}).get("mat2",0),
        'mat3': drops.get("custom3",{}).get("mat3",0),
        'mat4': drops.get("custom3",{}).get("mat4",0),
        'mat5': drops.get("custom3",{}).get("mat5",0),
        'animabefore': drops.get("custom3",{}).get("animabefore",0),
        'animaafter': drops.get("custom3",{}).get("animaafter",0),
    }
    current_drop['custom4'] = {
        'raid': drops.get("custom4",{}).get("raid",0),
        'mat1': drops.get("custom4",{}).get("mat1",0),
        'mat2': drops.get("custom4",{}).get("mat2",0),
        'mat3': drops.get("custom4",{}).get("mat3",0),
        'mat4': drops.get("custom4",{}).get("mat4",0),
        'mat5': drops.get("custom4",{}).get("mat5",0),
        'animabefore': drops.get("custom4",{}).get("animabefore",0),
        'animaafter': drops.get("custom4",{}).get("animaafter",0),
    }
    with open(datafile,'w') as file:
        json.dump(current_drop,file, indent=4)
    return current_drop

def save_setting_schema(settings:dict)->dict:
    current_setting = {}
    current_setting["theme"] = settings.get("theme")
    current_setting["active_tab"] = {
        "resource_tab" : settings.get("active_tab",{}).get("resource_tab"),
        "goldbar_tab" : settings.get("active_tab",{}).get("goldbar_tab"),
        "sand_tab": settings.get("active_tab",{}).get("sand_tab"),
        "custom_tab": settings.get("active_tab",{}).get("custom_tab")
    }
    with open(settingfile,'w') as file:
        json.dump(settings,file,indent=4)
    
    return current_setting

def load_data()->dict:
    if (not(os.path.isfile(datafile))):
        save_drop_schema({})

    with open(datafile) as file:
        try:
            return json.load(file) 
        except(json.JSONDecodeError):
            return {}

def load_setting()->dict:
    if (not(os.path.isfile(settingfile))):
        save_setting_schema({})

    with open(settingfile) as file:
        try:
            return json.load(file) 
        except(json.JSONDecodeError):
            return {}

drops = load_data()
settings = load_setting()

def get_data(raid:str,item:str) -> str|int:
    return drops.get(raid).get(item) 

def save_data(raid:str,*data:Item) -> None:
    for item in data:
        if (drops.get(raid) is None):
            drops[raid] = {}
        drops[raid][item.name] = item.count.get()

    with open(datafile,'w') as file:
        json.dump(drops,file, indent=4)

def get_setting(key:str,default:str=None):
    if(default):
        return settings.get(key,default)
    else:
        return settings.get(key)

def save_setting(key:str,value:str)->None: 
    global settings   
    settings[key] = value
    settings = save_setting_schema(settings)

def get_active_tab(tab:str)->str:
    return settings.get("active_tab",{}).get(tab,"")

def save_active_tab(tab:str,value:str)->None:
    global settings

    if(settings.get("active_tab") is None):
        settings["active_tab"] = {}
    
    settings["active_tab"][tab] = value
    settings = save_setting_schema(settings)