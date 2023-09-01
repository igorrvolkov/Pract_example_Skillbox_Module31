import requests
import json

if __name__ == '__main__':
    starship_resp = requests.get('https://swapi.dev/api/starships/10/')
    ss_json = json.loads(starship_resp.text)

    ss_name = ss_json['name']
    ss_max_atm_speed = ss_json['max_atmosphering_speed']
    ss_max_space_speed = ss_json['MGLT']
    ss_model = ss_json['model']
    pilots_url = ss_json['pilots']

    pilots = []
    for pilot in pilots_url:
        p_resp = requests.get(pilot)
        p_json = json.loads(p_resp.text)
        p_hw_url = p_json['homeworld']
        p_hw_resp = requests.get(p_hw_url)
        p_hw_name = json.loads(p_hw_resp.text)['name']
        pilot_info = {
            'name': p_json['name'],
            'height': p_json['height'],
            'weight': p_json['mass'],
            'homeworld name': p_hw_name,
            'homeworld link': p_hw_url
            }
        pilots.append(pilot_info)

    starship_info = {'starship name': ss_name,
                     'maximum atmospheric speed': ss_max_atm_speed,
                     'maximum space speed (MGLT)': ss_max_space_speed,
                     'class': ss_model,
                     'pilots': pilots}

    print(json.dumps(starship_info, indent=4))

    with open('Millennium Falcon info.json', 'w') as file:
        json.dump(starship_info, file, indent=4)
