import re


text = input("Enter a word:\n")

compiled = re.compile (r'%quit')

if compiled.findall(text) == ['%quit']:
    file = open('/home/andrew/Documents/new', 'a')
    file.write(re.sub('%quit','', text))
    file.close()
    file = open ('/home/andrew/Documents/new', 'r')
    print(file.read())

