import streamlit as st 
import pandas as pd 
import mysql.connector

def conectar():
    return mysql.connector.connect(host="localhost", user="root", password="33725105", database="cadastro")

#CREATE 

def criar_usuario(nome, email,senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
    con.commit()
    con.close()
    
    
#READ

def ler_usuarios():
    con = conectar()
    df = pd.read_sql("SELECT * FROM usuarios", con)
    con.close()
    return df 

#UPDATE

def atualizar_usuario(id, nome, email, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s", (nome, email, senha, id))
    con.commit()
    con.close()   
    
   
    
    
def deletar_usuario(id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    con.commit()
    con.close()

   
    
st.set_page_config(page_title="Registros de funcionários", layout="wide")

st.title("Registros de funcionários")

menu = ["Cadastrar", "Listar", "Atualizar", "Deletar"]
escolha = st.sidebar.selectbox("Menu", menu)

if escolha == "Cadastrar":
    st.subheader("Cadastrar")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        criar_usuario(nome, email, senha)
        st.success("cadastrado com sucesso!")
        
        
elif escolha == "Listar":
    st.subheader("Listar")
    df = ler_usuarios()
    st.dataframe(df)
    
elif escolha == "Atualizar":
    st.subheader("Atualizar lista")
    df = ler_usuarios()
    lista_usuarios = df["id"].tolist()
    id = st.selectbox("ID", lista_usuarios)
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    if st.button("Atualizar"):
        atualizar_usuario(id, nome, email, senha)
        st.success("atualizado com sucesso!")
        
elif escolha == "Deletar":
    st.subheader("Deletar")
    df = ler_usuarios()
    lista_usuarios = df["id"].tolist()
    id = st.selectbox("ID", lista_usuarios)
    if st.button("Deletar"):
        deletar_usuario(id)
        st.success(" deletado com sucesso!")
