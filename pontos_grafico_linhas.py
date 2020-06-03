import matplotlib.pyplot as plt

titulo = "Comparando barras"
eixox = 'Eixo X'
eixoy = 'Eixo Y'
z = [200,50,1000,300,200] # Tamanho dos pontos

x = [1,3,5,7,9]
y = [2,3,4,5,1]

# Legendas
plt.title(titulo)
plt.xlabel(eixoy)
plt.ylabel(eixox)

plt.scatter(x,y, label = "Meus pontos", color = "k",s = z) #Alterar tamanho dos pontos
plt.legend()
plt.plot(x,y, color = "#000099", linestyle="-")
plt.show()

