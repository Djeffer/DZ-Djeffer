import json
from random import choice, randint


def gen_person():
    name = ''
    tel = ''

    letters = list("abcdefeg")['a', 'b', 'b', 'd', 'e', 'f', 'e', 'g']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


def write_json(person_dict, num):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict

    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)

# for i in range(5):
#     write_json(gen_person())


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])

with open('persons.json', 'r') as f:
    print(json.load(f))
