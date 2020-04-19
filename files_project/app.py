my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)

name = input('Enter your name: ')

my_file = open('data.txt', 'w')
my_file.write(name)
my_file.close()
