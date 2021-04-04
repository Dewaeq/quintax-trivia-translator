from datetime import datetime
import json

jsonData = json.load(open('output.json', encoding="utf-8"))

def backup():
    current_date = datetime.today().replace(microsecond=0)
    backup_name = 'backup_' + str(current_date).replace(' ', '_').replace(':', '꞉') + '.json'
    print(backup_name)
    
    with open(backup_name, 'w+', encoding='utf8') as outfile:
        json.dump(jsonData, outfile, ensure_ascii=False)