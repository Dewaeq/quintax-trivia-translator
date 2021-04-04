import json
import backup as backup

backup.backup()

jsonData = json.load(open('output.json', encoding="utf-8"))

for language in jsonData['all_questions']:
    index = 0
    for x in jsonData['all_questions'][language]:
        jsonData['all_questions'][language][index]['id'] = index
        index += 1

with open('output.json', 'w+', encoding='utf8') as outfile:
    json.dump(jsonData, outfile, ensure_ascii=False)
