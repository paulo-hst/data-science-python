import matplotlib.pyplot as plt

titulo = "Gráfico de barras"

x = [1,2.3]
y = [50,30,40]

plt.title(titulo)
plt.xlabel('Barras')
plt.ylabel('Valores')

plt.bar(x,y)
plt.show()