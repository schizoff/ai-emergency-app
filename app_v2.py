
import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Emergency Assistant")

# Load data
try:
    data = pd.read_csv("data_kasus_gawat.csv")
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    st.stop()

# --- Form Input Klinis ---
st.header("📝 Input Data Klinis")

anamnesis = st.text_area("Anamnesis")
pemeriksaan_fisik = st.text_area("Hasil Pemeriksaan Fisik")
penunjang = st.text_area("Hasil Pemeriksaan Penunjang")

submit = st.button("Analisis Diagnosis")

if submit:
    if not (anamnesis.strip() and pemeriksaan_fisik.strip() and penunjang.strip()):
        st.warning("Harap lengkapi semua bagian input.")
    else:
        input_text = f"{anamnesis} {pemeriksaan_fisik} {penunjang}"

        # Gabungkan kolom data untuk similarity check
        data['gabungan'] = data['anamnesis'] + " " + data['pemeriksaan_fisik'] + " " + data['penunjang']

        # Vectorize dan hitung similarity
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(data['gabungan'].tolist() + [input_text])
        similarity = cosine_similarity(vectors[-1], vectors[:-1])

        # Ambil hasil terbaik
        idx = similarity[0].argmax()
        hasil = data.iloc[idx]

        st.subheader("🧠 Diagnosis Utama:")
        st.write(hasil['diagnosis'])

        try:
            ddx_list = ast.literal_eval(hasil['diagnosis_banding'])
            st.subheader("📌 Diagnosis Banding:")
            for ddx in ddx_list:
                st.write(f"- {ddx}")
        except:
            st.warning("Diagnosis banding tidak dapat ditampilkan.")

        st.subheader("💊 Saran Terapi Awal:")
        st.write(hasil['terapi'])
