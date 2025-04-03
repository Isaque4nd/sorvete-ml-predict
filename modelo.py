import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Simulando dados de temperatura e vendas de sorvete
data = {
    "Temperatura": np.random.randint(20, 40, 50),
    "Vendas": np.random.randint(100, 500, 50)
}
df = pd.DataFrame(data)

# Dividindo os dados em treino e teste
X = df[["Temperatura"]]
y = df["Vendas"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliação do modelo
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Exibir métricas
print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")

# Gráfico de dispersão
plt.scatter(X_test, y_test, color='blue', label='Real')
plt.scatter(X_test, y_pred, color='red', label='Previsto')
plt.xlabel("Temperatura")
plt.ylabel("Vendas de Sorvete")
plt.legend()
plt.title("Previsão de Vendas de Sorvete vs Temperatura")
plt.show()
