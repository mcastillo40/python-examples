# Ask the user for a list of 3 friends
user_names = ""  # input("3 Names: ")
names = user_names.split(',')

# For each friend, we'll tell the user whether they are nearby
nearby_list = []
people_file = open('people.txt', 'r')

people_nearby = [line.strip().lower() for line in people_file.readlines()]

# for line in people_file.readlines():
#    for name in names:
#        if name.lower() == line.strip().lower():
#            nearby_list.append(name.capitalize())
#            names.remove(name)
people_file.close()

nearby_set = set(people_nearby)
friends_set = set(names)

add_list = friends_set.intersection(nearby_set)

# For each nearby friend, we'll save their name to `nearby_friends.txt`
people_file = open('nearby_friends.txt', "w")
for count, nearby in enumerate(add_list):
    people_file.write(nearby.capitalize())
    if count < len(add_list) - 1:
        people_file.write('\n')

people_file.close()

correct = 0
total_question = 0

quiz = open("questions.txt", "r")
questions = [question.strip() for question in quiz.readlines()]
quiz.close()

total_question = len(questions)

for question in questions:
    new_question, answer = question.split('=')
    response = input(new_question + "=")

    if int(response) == int(answer):
        correct += 1

final = open("result.txt", 'w')
final.write("Your final score is {correct}/{total_questions}.".format(correct=correct, total_questions=total_question))
final.close()
