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

