"""
Izmantojot map() funkciju izveidot no diviem sarakstiem saliktnei.


"""
saraksts1 = [1, 2, 3]
saraksts2 = ['a', 'b', 'c']
parejie = list(map(lambda x, y: str(x) + y, saraksts1, saraksts2))
print(parejie)