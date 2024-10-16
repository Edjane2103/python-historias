import random

# função que gera a introdução da história
def gerar_introducao():
 introducoes = ["há algum tempo", "no passado", "daqui ha alguns anos"]
 return random.choice(introducoes)

# função que gera o desenvolvimento da história
def gerar_desenvolvimento():
     desenvolvimentos = ["um corajoso menino", "uma mulher guerreira"]