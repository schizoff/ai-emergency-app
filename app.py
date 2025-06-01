
import streamlit as st

st.title("AI Emergency Assistant")

# Input dari user
keluhan = st.selectbox("Keluhan Utama", [
    "Nyeri dada", "Sesak napas", "Penurunan kesadaran", "Demam tinggi",
    "Nyeri perut kanan bawah", "Muntah darah", "Trauma kepala",
    "Pingsan", "Kejang", "Nyeri punggung hebat"
])

# Rule-based logic
def rule_based_diagnosis(keluhan):
    data = {
        "Nyeri dada": ("ACS, PE, pneumotoraks", "Aspirin, O2, monitor, EKG"),
        "Sesak napas": ("Asma, PPOK, edema paru", "O2, nebulisasi, steroid"),
        "Penurunan kesadaran": ("Hipoglikemia, stroke, sepsis", "Dextrose IV, CT, antibiotik"),
        "Demam tinggi": ("Sepsis, dengue, malaria", "Cairan IV, antipiretik, antibiotik"),
        "Nyeri perut kanan bawah": ("Apendisitis, kolesistitis, ISK", "Cairan IV, analgesik, USG"),
        "Muntah darah": ("Varises esofagus, tukak lambung", "Cairan IV, somatostatin, endoskopi"),
        "Trauma kepala": ("Cedera otak, perdarahan intraserebral", "CT kepala, observasi"),
        "Pingsan": ("Vasovagal, hipoglikemia, aritmia", "Observasi, cairan IV, EKG"),
        "Kejang": ("Epilepsi, hiponatremia, infeksi CNS", "Diazepam IV, cek elektrolit, LP"),
        "Nyeri punggung hebat": ("Diseksi aorta, kolik nefrolitik", "Pain control, CT angio, kontrol tekanan darah")
    }
    return data.get(keluhan, ("Tidak diketahui", "Observasi"))

if keluhan:
    diagnosis, terapi = rule_based_diagnosis(keluhan)
    st.subheader("Diagnosis Diferensial:")
    st.write(diagnosis)
    st.subheader("Saran Terapi Awal:")
    st.write(terapi)
