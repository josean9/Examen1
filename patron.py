patron = [
          ["A", "B", "C"],
          ["D","E","F"],
          ["G","H","I"]
    ]
def posibilidadesPatron(LetraInicial, patron):
    posibilidades = []
    for i in patron:
        for j in i:
            if j == LetraInicial:
                posibilidades.append((i, j))
print(posibilidadesPatron(0, patron))