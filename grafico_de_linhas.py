import matplotlib.pyplot as plt

label = ['Ordenadas', 'Abscissas'] # Lista de rótulos

plt.xlabel(label[0]) # Rotular eixo X
plt.ylabel(label[1]) # Rotular eixo Y

x = [1,2,3] # definir valores para eixo X
y = [4,5,6] # definir valores para eixo Y

plt.plot(x,y)
plt.show()
