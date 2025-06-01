
import streamlit as st
import pandas as pd
import ast

st.title("AI Emergency Assistant (Berbasis CSV + Input Klinis)")

# Load data
try:
    data = pd.read_csv("data_kegawatdaruratan_ddx.csv")
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    st.stop()

# --- Form Input Klinis ---
st.header("📝 Input Data Klinis")

anamnesis = st.text_area("Anamnesis")
pemeriksaan_fisik = st.text_area("Hasil Pemeriksaan Fisik")
penunjang = st.text_area("Hasil Pemeriksaan Penunjang")

st.markdown("---")

# Input keluhan untuk analisis sederhana berbasis teks


if keluhan:
    hasil = data[data['keluhan'].str.contains(keluhan, case=False, na=False)]

    if not hasil.empty:
        st.subheader("🧠 Diagnosis Utama:")
        st.write(hasil.iloc[0]['diagnosis'])

        # Diagnosis banding aman
        try:
            ddx_list = ast.literal_eval(hasil.iloc[0]['diagnosis_banding'])
            st.subheader("📌 Diagnosis Banding:")
            for ddx in ddx_list:
                st.write(f"- {ddx}")
        except Exception as e:
            st.warning("Diagnosis banding tidak dapat ditampilkan.")

        st.subheader("💊 Saran Terapi Awal:")
        st.write(hasil.iloc[0]['terapi'])
    else:
        st.warning("Keluhan tidak ditemukan dalam database.")
