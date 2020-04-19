import random

calculate = {3:"Fizz", 5:"Buzz"}

for num in range(1, 21): 
    phrase = ""
    if(not num % 3):
        phrase += str(calculate[3])
        
    if(not num % 5):
        phrase += str(calculate[5])

    print(phrase or num)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is prime")


numbers = [2, 4, 6, 7]
friends = ["Sam", "Tim", "Matt", "Adrian"]

doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

age_string = [f"This num:  {num}" for num in doubled_numbers]
print(age_string)

long_timers = { 
    friends[i]: numbers[i]
    for i in range(len(friends)) 
}
print(long_timers)

new_dict = dict(zip(friends, doubled_numbers))
print(new_dict)

for counter, friend  in enumerate(friends):
    print(f"{counter}: {friend}")


lottery_numbers = set(random.sample(range(22), 6))
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

numbers_matched = 0 # most matched
current_winner = 0  # index

for index,player in enumerate(players):
    temp = len(lottery_numbers.intersection(player['numbers']))

    if(temp > numbers_matched):
        numbers_matched = temp
        current_winner = index  

winnings = 100 ** numbers_matched
print(f"{players[current_winner]['name']} won {winnings}")
