# Dictionary is the Key and value pair

data = {1: 'Manju', 2: 'Kiran', 4: 'Harsha'}

print(data.get(1))
print(data.get(3, "Not Found"))
keys = ['Manju', 'Mahi', 'Ravi']
values = ['python', 'java', 'devops']

prog = dict(zip(keys, values))
print(prog)

prog['Sra'] = 'c#'

print(prog)

proIDE = {'JS': 'VSCode', 'Python': ['PYCharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}

print(proIDE['JS'])
print(proIDE['Python'][0])
print(proIDE['Python'][1])
print(proIDE['Java']['JSE'])
print(proIDE['Java']['JEE'])
