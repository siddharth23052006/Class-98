f = open("test.txt")
#print(f.read())
fileLines = f.readlines()
for line in fileLines:
  print(line)

#String functions
introString = 'My name is Siddharth, I am 15 years old.'
words = introString.split(',')
print(words)

def greet(name):
  print("Hello " + name + ". How are you?")

greet("Siddharth")
