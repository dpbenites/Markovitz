import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm, t, probplot

# Função para obter dados históricos das ações e calcular retornos
def stock_data(ticker, start_date='2019-01-02'):
    data = yf.Ticker(ticker)
    data = data.history(start=start_date, end=None)
    data.index = data.index.strftime('%Y-%m-%d')
    data.reset_index(inplace=True)

    data['Prev-Close'] = data['Close'].shift(1)
    data['Return'] = data['Close'] / data['Prev-Close'] - 1
    data['Log-Return'] = np.log(data['Return'] + 1)

    return data

# Função para plotar histogramas e distribuições
def return_distributions(data, distribution='normal', mode='standard', bins=100, color='blue', edgecolor='black', alpha=0.7):
    std = data['Return'].std()
    std_log = data['Log-Return'].std()
    mean = data['Return'].mean()
    mean_log = data['Log-Return'].mean()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    if distribution == 'normal' and mode == 'standard':
        x_space = np.linspace(data['Return'].min(), data['Return'].max(), 100)
        y_space = norm.pdf(x_space, loc=mean, scale=std)
        axes[0].plot(x_space, y_space, label='normal fit', color='orange')
        data['Return'].hist(bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, density=True, ax=axes[0])
        axes[0].text(0.3, 0.95, f'Mean: {mean:.4f}\nStd: {std:.4f}', color='red', ha='right', va='top', transform=axes[0].transAxes, fontsize=10)
        axes[0].legend()
        axes[0].set_title('Histograma e Ajuste Normal - Retornos Padrão')
        axes[0].set_xlabel('Retornos Padrão')
        axes[0].set_ylabel('Frequência')

        # QQ-plot para normal
        probplot(data['Return'].dropna(), dist='norm', fit=True, plot=axes[1])

    plt.subplots_adjust(wspace=0.4)
    plt.show()

# Carregar dados
googl = stock_data('GOOGL')

# Gerar gráficos de distribuição para retornos padrão
return_distributions(googl, distribution='normal', mode='standard')
