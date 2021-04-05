from datetime import datetime
import pathlib
import json
import glob

jsonData = json.load(open('output.json', encoding='utf-8'))


def _has_backup():
    allBackups = [file for file in glob.glob('backups/*.json')]
    for filePath in allBackups:
        data = json.load(open(filePath, encoding='utf-8'))

        if data == jsonData:
            return True

    return False


def backup():
    if _has_backup():
        return

    p = pathlib.Path('backups')
    p.mkdir(exist_ok=True)
    current_date = datetime.today().replace(microsecond=0)
    backup_name = 'backup_' + \
        str(current_date).replace(' ', '_').replace(':', '꞉') + '.json'

    with open(p / backup_name, 'w+', encoding='utf8') as outfile:
        json.dump(jsonData, outfile, ensure_ascii=False)
