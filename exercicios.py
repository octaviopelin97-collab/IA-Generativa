# calculadora


import streamlit as st


st.title('Calculadora')


numero1 = st.number_input('numero ') 
numero2 = st.number_input('numero ', step=0.1)


if st.button('RESULTADO'):
    soma = numero1 +  numero2
    st.success(soma)


# ----------------------------------------


# calculadora de imc



st.title('Calculo do imc')


peso = st.number_input('PESO')
altura = st.number_input('Altura')


if st.button('Calcular IMC'):
    calculo = round(peso / (altura ** 2), 2)
    st.success(calculo)


    # -------------------------------------------
import streamlit as st

st.title('Cadastro de Usuário')


nome = st.text_input('Nome completo:')
email = st.text_input('e-mail:')
idade = st.number_input('Idade:') 

if st.button('Salvar'):
   st.success('Cadastro realizado com sucesso!') 

 