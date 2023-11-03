"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""


saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
saraksts2=["Dr." + saraksts1 for saraksts1 in saraksts1]

print(saraksts2)