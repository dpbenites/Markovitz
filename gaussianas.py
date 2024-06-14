import matplotlib.pyplot as plt
import numpy as np

# Definir os parâmetros das distribuições
mean = 0
std_dev1 = 1
std_dev2 = 2

# Gerar os valores das distribuições
x = np.linspace(mean - 3*std_dev2, mean + 3*std_dev2, 1000)
y1 = (1/(std_dev1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev1) ** 2)
y2 = (1/(std_dev2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev2) ** 2)

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='$\sigma_{1}$' + f'= {std_dev1}', color ='red')
plt.plot(x, y2, label='$\sigma_{2}$' + f'= {std_dev2}', color = 'blue')

# Adicionar a legenda
plt.legend()

# Adicionar título e rótulos dos eixos
plt.title('Distribuições Gaussianas e desvios padrões')
plt.xlabel('x')
plt.ylabel('Densidade de probabilidade')
plt.grid(True)
# Salvar a imagem
plt.savefig('gaussian_distributions.png')

# Mostrar o gráfico
plt.show()
