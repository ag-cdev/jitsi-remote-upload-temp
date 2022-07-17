import json

CONFIG_FIlE = "config.json"
# can use here env var
class config:
    def __init__(self,config_f):
        with open(config_f) as data:
            global config_v = json.load(data)
    
def main():
    configs = config(CONFIG_FIlE)
  

if __name__=="__main__":
    main()