from pickle import TRUE
from pprint import pprint
import requests


def hero_request(name):
# Получение данных по запросу
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    heroes = response.json()
    for hero in heroes:
        if hero['name'] == name:
            intelligence = hero['powerstats']['intelligence']
    return intelligence

def rating_intelligence(hero_dict):
#Функция сортировки и определения рейтинга по интеллекту       
    sorted_values = sorted(hero_dict.values(), reverse=True)
    sorted_dict = {}

    for hero_intell in hero_dict.items():
        if hero_intell[1] == sorted_values[0]:
            # print(hero_intell[0])
            first_hero =  hero_intell[0]
    return first_hero
            

if __name__ == '__main__':    
    name_hero = ['Hulk', 'Captain America', 'Thanos']
    
    hero_intelligence_dict = {}
    for hero in name_hero:
        hero_intelligence_dict[hero] =  hero_request(hero)

print(f'Наиболее высокий интеллект у {rating_intelligence(hero_intelligence_dict)}')
        




