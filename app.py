import streamlit as st
import matplotlib.pyplot as plt
import os

ARQUIVO = "alunos.txt"

def salvar_aluno(nome, serie, n1, n2, n3):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{nome},{serie},{n1},{n2},{n3}\n")

def ler_alunos():
    alunos = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(",")
                if len(dados) == 5:
                    nome, serie, n1, n2, n3 = dados
                    alunos.append({
                        "nome": nome,
                        "serie": serie,
                        "notas": [float(n1), float(n2), float(n3)]
                    })
    return alunos

st.title("Sistema de Notas dos Alunos")

menu = st.sidebar.radio("Menu", ["Cadastrar Aluno", "Relatórios"])

if menu == "Cadastrar Aluno":
    st.header("Cadastrar novo aluno")

    nome = st.text_input("Nome do aluno:")
    serie = st.selectbox("Série:", ["1D", "2D", "3D"])
    n1 = st.number_input("Nota 1:", 0.0, 10.0, step=0.1)
    n2 = st.number_input("Nota 2:", 0.0, 10.0, step=0.1)
    n3 = st.number_input("Nota 3:", 0.0, 10.0, step=0.1)

    if st.button("Salvar"):
        if nome.strip() == "":
            st.warning("Digite o nome do aluno.")
        else:
            salvar_aluno(nome, serie, n1, n2, n3)
            st.success(f"Aluno {nome} cadastrado com sucesso!")

elif menu == "Relatórios":
    st.header("Relatórios e Análises")

    alunos = ler_alunos()

    if not alunos:
        st.info("Nenhum aluno cadastrado ainda.")
    else:
        # Média geral por série
        st.subheader("Média geral por série")

        medias_por_serie = 
        for a in alunos:
            media = sum(a["notas"]) / 3
            if a["serie"] not in medias_por_serie:
                medias_por_serie[a["serie"]] = 
            medias_por_serie[a["serie"]].append(media)

        for serie, medias in medias_por_serie.items():
            media_geral = sum(medias) / len(medias)
            st.write(f" Série {serie}: média geral = {media_geral:.2f}")

        serie_sel = st.selectbox("Selecione uma série para visualizar:", list(medias_por_serie.keys()))

        medias = [sum(a["notas"]) / 3 for a in alunos if a["serie"] == serie_sel]
        nomes = [a["nome"] for a in alunos if a["serie"] == serie_sel]

        fig, ax = plt.subplots()
        ax.bar(nomes, medias)
        ax.set_title(f"Médias Finais - Série {serie_sel}")
        ax.set_xlabel("Alunos")
        ax.set_ylabel("Média Final")
        plt.xticks(rotation=45)
        st.pyplot(fig)