import matplotlib.pyplot as plt

titulo = "Comparando barras"

x1 = [1,3,5,7,9]
y1 = [2,3,4,5,6]

x2 = [2,4,6,8,10]
y2 = [10,5,12,4,7]

# Legendas
plt.title(titulo)
plt.xlabel('Eixo Y')
plt.ylabel('Eixo X')

plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.legend()
plt.show()



