csv = open("csv_data.txt", "r")
lines = csv.readlines()
csv.close()

lines = [line.strip() for line in lines[1:]]

print(lines)

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].capitalize()
    degree = person_data[3].title()

    print(f"{name} is {age} studying {degree} at {university}")

list_name = ['Matt', '30', 'OSU', 'Computer Science']
sampleValue = ','.join(list_name)
print(sampleValue)
csv = open("csv_data.txt", "a")
csv.write(sampleValue)
csv.close()
