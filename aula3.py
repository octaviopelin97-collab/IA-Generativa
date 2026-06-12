import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

modelo_previsão = LinearRegression()
modelo_previsão.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])

# 3. Tela simples para o usuário
valor_investido = st.number_input("Digite o investimento:")

# 4. Botão e resultado básico
if st.button("Previsão"):
    resultado = modelo_previsão.predict([[valor_investido]])
    
    st.write("O faturamento previsto é:")
    st.success(resultado[0])