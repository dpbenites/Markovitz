import numpy as np
import matplotlib.pyplot as plt

# Definindo os retornos e desvios padrão dos ativos
retorno_A = 0.6
retorno_B = 0.4
desvio_padrao_A = 0.3
desvio_padrao_B = 0.1

# Função para calcular o retorno do portfólio
def calcular_retorno_portfolio(w_a, w_b, retorno_a, retorno_b):
    return w_a * retorno_a + w_b * retorno_b

# Função para calcular o risco (desvio padrão) do portfólio
def calcular_risco_portfolio(w_a, w_b, desvio_padrao_a, desvio_padrao_b, correlacao):
    return np.sqrt((w_a**2 * desvio_padrao_a**2) +
                   (w_b**2 * desvio_padrao_b**2) +
                   (2 * w_a * w_b * correlacao * desvio_padrao_a * desvio_padrao_b))

# Pesos dos ativos no portfólio
pesos = np.linspace(0, 1, 100)

# Correlações a serem consideradas
correlacoes = [-1, -0.5, -0.2 ,  0, 0.5, 1]

# Plotando as curvas de risco e retorno
plt.figure(figsize=(10, 6))

for correlacao in correlacoes:
    retornos_portfolio = []
    riscos_portfolio = []
    
    for w_a in pesos:
        w_b = 1 - w_a
        retorno_p = calcular_retorno_portfolio(w_a, w_b, retorno_A, retorno_B)
        risco_p = calcular_risco_portfolio(w_a, w_b, desvio_padrao_A, desvio_padrao_B, correlacao)
        
        retornos_portfolio.append(retorno_p*100)
        riscos_portfolio.append(risco_p*100)
    
    plt.plot(riscos_portfolio, retornos_portfolio, label=f'ρ = {correlacao}')

# Customizando o gráfico para remover as linhas superior e direita
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xlabel('Risco (Desvio Padrão) (%)')
plt.ylabel('Retorno(%)')
plt.title('Curvas de Risco e Retorno para Diferentes Correlações')
plt.legend()
plt.grid(True)
plt.show()
