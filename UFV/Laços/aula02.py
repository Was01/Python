# Estrururas de repetição

# Laço while
"""
number=1
while number<=5:
    print(number)
    number+=1
"""



""""
prompt = '\nDiga-me alguma coisa e eu repetir'
prompt+=" ou então digite 'pare' para terminar o programa: "
message=""
while message!='pare':
    message=input(prompt)
    print(message)
"""



"""
prompt = '\nDiga-me alguma coisa e eu repetir'
prompt+=" ou então digite 'pare' para terminar o programa: "
active=True
while active:
    message=input(prompt)
    if message=='pare':
        active=False
    else:
        print(message)
"""



"""""
prompt = '\nInforme o nome de uma cidade que você visitou'
prompt+=" digite 'pare' quando estiver informado a cidade. "
while True:
    city=input(prompt)
    if city=='pare':
        break
    else:
        print(f'Eu gostaria de visitar {city.title()}!')
"""


"""
number=0
while number<10:
    number+=1
    if number % 2==0:
        continue
    print(number)
"""

## Laço for

"""
frutas=['banana','uva','abacaxi','melancia']
for x in frutas:
    print(x)
"""

"""
for i in 'melancia':
    print(i)
"""

"""
for i in range(5):
    print(i)
"""

"""
for i in range(2,6):
    print(i)
"""

# Entrada e saída de arquivos

""""
with open ('nomes.txt','r') as reader:
    print(reader.read())
"""

""""
f=open('nomes.txt')
mylist=f.readlines()
print(mylist)
"""
""""
with open ('nomes.txt','r') as reader:
    line=reader.readline()
    while line != '':
        print(line,end='')
        line=reader.readline()
"""

""""
with open('nomes.txt','r') as reader:
    for line in reader.readlines():
        print (line, end='')
"""


with open ('nomes.txt','r') as reader:
    nomes=reader.readlines()

""""
with open('nomes.txt','w') as writer:
    writer.writelines(reversed(nomes))
"""

with open ('nomes.txt','w') as writer:
    for nome in reversed(nomes):
        writer.write(nome)