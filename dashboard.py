
import streamlit as st

st.set_page_config(
    page_title="Aplikasi Streamlit",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Aplikasi Streamlit Pertama")
st.write("Selamat datang di aplikasi Streamlit lokal!")

nama = st.text_input("Masukkan nama Anda")

if st.button("Sapa Saya"):
    if nama:
        st.success(f"Halo, {nama}! Streamlit berhasil berjalan.")
    else:
        st.warning("Silakan masukkan nama terlebih dahulu.")
