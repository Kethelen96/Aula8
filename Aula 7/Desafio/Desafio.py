import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
  

df = pd.read_csv("Vendas1.csv")

plt.bar("Vendedor","Vendas")
plt.xlabel('Vendedor')
plt.ylabel('Quantidade vendida')
plt.title('Quantidade vendida por vendedor')
plt.show()


