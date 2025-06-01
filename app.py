
import streamlit as st
import pandas as pd

st.title("AI Emergency Assistant (Berbasis CSV)")

# Load data dari CSV
data = pd.read_csv("data_kegawatdaruratan.csv")

# Input keluhan
keluhan = st.text_input("Masukkan keluhan utama pasien:")

if keluhan:
    hasil = data[data['keluhan'].str.contains(keluhan, case=False)]

    if not hasil.empty:
        st.subheader("Diagnosis Diferensial:")
        st.write(hasil.iloc[0]['diagnosis'])
        st.subheader("Saran Terapi Awal:")
        st.write(hasil.iloc[0]['terapi'])
    else:
        st.warning("Keluhan tidak ditemukan dalam database.")
