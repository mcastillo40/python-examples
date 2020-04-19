import json

with open("friends_json.txt", "r") as file:
    file_contents = json.load(file)  # read and turn into dictionary

print(file_contents['friends'][0])
cars = []

cars = [
    {'make': 'Chevy', 'model': 'Camaro'},
    {'make': 'Chevy', 'model': 'Colorado'}
]

with open("cars_json.txt", "w") as file:
    json.dump(cars, file)

my_json_string = '[{"name": "Ford", "released": 1950}]'

wrong_car = json.loads(my_json_string)
print(wrong_car[0]['name'])