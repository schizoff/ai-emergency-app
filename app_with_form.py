
import streamlit as st
import pandas as pd

st.title("AI Emergency Assistant (Berbasis CSV + Input Klinis)")

# Load data
data = pd.read_csv("data_kegawatdaruratan_ddx.csv")

# --- Form Input Klinis ---
st.header("📝 Input Data Klinis")

anamnesis = st.text_area("Anamnesis")
pemeriksaan_fisik = st.text_area("Hasil Pemeriksaan Fisik")
penunjang = st.text_area("Hasil Pemeriksaan Penunjang")

st.markdown("---")

# Input keluhan untuk analisis sederhana berbasis teks
st.header("🔍 Analisis Berdasarkan Keluhan Utama")
keluhan = st.text_input("Masukkan keluhan utama pasien (bebas):")

if keluhan:
    hasil = data[data['keluhan'].str.contains(keluhan, case=False)]

    if not hasil.empty:
        st.subheader("🧠 Diagnosis Utama:")
        st.write(hasil.iloc[0]['diagnosis'])

        st.subheader("📌 Diagnosis Banding:")
        for ddx in eval(hasil.iloc[0]['diagnosis_banding']):
            st.write(f"- {ddx}")

        st.subheader("💊 Saran Terapi Awal:")
        st.write(hasil.iloc[0]['terapi'])
    else:
        st.warning("Keluhan tidak ditemukan dalam database.")
