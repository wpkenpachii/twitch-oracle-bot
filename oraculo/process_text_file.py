import re
file = open('data/pokemon-dataset.txt', 'r', encoding="utf-8")
new_file = open('data/dataset.txt', 'a', encoding="utf-8")
while True:
    line = file.readline()
    if not line:
        break
    new_values = {}
    splitted = line.split('|')

    try:
        [id, description] = splitted[0].split(':')
    except:
        continue

    matches = ['description', 'tier', 'types', 'immune', 'takes', 'weak', 'weight', 'stats', 'effective']

    for idx, spl in enumerate(splitted):
        print(idx)
        if idx < 1:
            id, description = splitted[idx].split(':')
            new_values['id'] = id
            new_values['description'] = description
        if re.search(f"{matches[idx]}", spl, re.IGNORECASE):
            new_values[  matches[idx]  ] = spl
        else:
            new_values[  matches[idx]  ] = 'none'

    for attr in ['id', 'description', 'tier', 'types', 'immune', 'takes', 'weak', 'weight', 'stats', 'effective']:
        if attr not in new_values.keys():
            new_values[attr] = 'none'

    print(new_values)

    new_file.write(f"This is {description} and he/she has {id}. {description} is from{new_values['tier']}. {description} is from following types{new_values['types']}. {description} is immune against{new_values['immune']}. {description},{new_values['takes']}. {description} have{new_values['weight']},{new_values['stats']}. The most effective balls to catch {description} is{new_values['effective']}\n")

    
