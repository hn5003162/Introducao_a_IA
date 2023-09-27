from kanren import Relation, facts, var, run, lall, lany
from kanren.constraints import neq
mae = Relation()
pai = Relation()
irmao = Relation()
# Família Eric e Carol
facts(mae, ('Carol', 'John'))
facts(pai, ('Eric', 'John'))
facts(mae, ('Carol', 'Julia'))
facts(pai, ('Eric', 'Julia'))
facts(mae, ('Carol', 'Leo'))
facts(pai, ('Eric', 'Leo'))
# Família Thomas e Olga
facts(mae, ('Olga', 'Angela'))
facts(pai, ('Thomas', 'Angela'))
facts(mae, ('Olga', 'Karen'))
facts(pai, ('Thomas', 'Karen'))

# Família Ken e Renata
facts(mae, ('Renata', 'Rodrigo'))
facts(pai, ('Ken', 'Rodrigo'))

# Família Leo e Angela
facts(mae, ('Angela', 'Lisa'))
facts(pai, ('Leo', 'Lisa'))
facts(mae, ('Angela', 'Bia'))
facts(pai, ('Leo', 'Bia'))
facts(mae, ('Angela', 'Arthur'))
facts(pai, ('Leo', 'Arthur'))

# Família Rodrigo e Karen
facts(mae, ('Karen', 'Cris'))
facts(pai, ('Rodrigo', 'Cris'))
facts(mae, ('Karen', 'Silvia'))
facts(pai, ('Rodrigo', 'Silvia'))



def pais(x,pessoa):
    return lany(
        mae(x, pessoa),
        pai(x, pessoa),
    )

def irmaos(x,pessoa):
    return lany(
        mae(x, pessoa),
        pai(x, pessoa),
    )

def avos(x,pessoa):
    return lany(
        mae(x, pessoa),
        pai(x, pessoa),
    )



x = var()

# Mostra quem são os pais de:
print(run(2, x, pais(x, 'John')))
print(run(2, x, pais(x, 'Julia')))
print(run(2, x, pais(x, 'Leo')))

print(run(2, x, pais(x, 'Angela')))
print(run(2, x, pais(x, 'Karen')))

print(run(2, x, pais(x, 'Rodrigo')))

print(run(2, x, pais(x, 'Lisa')))
print(run(2, x, pais(x, 'Bia')))
print(run(2, x, pais(x, 'Arthur')))

print(run(2, x, pais(x, 'Cris')))
print(run(2, x, pais(x, 'Silvia')))




