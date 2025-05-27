import streamlit as st

st.title("Nastars-Bakery🥨")
st.write("Find your sweet food at this place (*^ω^)")
st.image("dc50297e933a6c84a806232607af4a73.jpg")
st.image("3de28c91a675305ab3f05292ef85682c.jpg")
st.image("")

st.title("Strawberries Cake")
st.header("mengecek nilai genap/ganjil")
angka = st.number_input("pilih angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
