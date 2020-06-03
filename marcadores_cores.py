import matplotlib.pyplot as plt

titulo = "Comparando barras"
eixox = 'Eixo X'
eixoy = 'Eixo Y'

x = [1,3,5,7,9]
y = [2,3,4,5,1]

# Legendas
plt.title(titulo)
plt.xlabel(eixoy)
plt.ylabel(eixox)

plt.scatter(x,y, label = "Meus pontos", color = "r")
plt.legend()
plt.plot(x,y, color = "k", linestyle="--")
plt.show()


