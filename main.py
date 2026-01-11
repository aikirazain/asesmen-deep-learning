import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# --- DATA LOGIKA INDIKATOR ---
data_instrumen = {
    "Beriman & Bertakwa": {
        "Mindful": "Refleksi tenang tentang nilai moral yang dirasakan saat mempelajari topik ini.",
        "Meaningful": "Menghubungkan ajaran agama dengan aksi nyata membantu sesama.",
        "Joyful": "Merayakan kebesaran Tuhan melalui observasi alam yang menyenangkan."
    },
    "Bernalar Kritis": {
        "Mindful": "Menyadari emosi yang muncul saat menghadapi informasi yang membingungkan.",
        "Meaningful": "Menganalisis validitas informasi untuk keputusan penting dalam hidup.",
        "Joyful": "Permainan 'Detektif Informasi' untuk menemukan logika yang unik."
    },
    "Kreatif": {
        "Mindful": "Mengamati proses berpikir saat mencoba menemukan ide orisinal.",
        "Meaningful": "Menciptakan produk inovatif dari bahan bekas untuk solusi rumah tangga.",
        "Joyful": "Eksperimen bebas dengan berbagai media tanpa takut salah."
    },
    # Tambahkan dimensi lainnya di sini...
}

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="DL Assessment Builder", layout="wide")
st.title("🛠️ Deep Learning Assessment Builder")
st.subheader("Mindful, Meaningful, & Joyful berbasis Profil Lulusan")

# --- SIDEBAR INPUT ---
st.sidebar.header("Konfigurasi Instrumen")
nama_guru = st.sidebar.text_input("Nama Guru")
mapel = st.sidebar.text_input("Mata Pelajaran")

dimensi_terpilih = st.sidebar.multiselect(
    "Pilih Dimensi Profil Lulusan:",
    list(data_instrumen.keys())
)

pilar_fokus = st.sidebar.radio("Fokus Pilar Deep Learning:", ["Mindful", "Meaningful", "Joyful"])

# --- PROSES GENERATE ---
if st.sidebar.button("Generate Instrumen"):
    st.write(f"### Draf Instrumen untuk: {mapel}")
    
    hasil_akhir = []
    for dim in dimensi_terpilih:
        narasi = data_instrumen[dim][pilar_fokus]
        hasil_akhir.append({"Dimensi": dim, "Pilar": pilar_fokus, "Instrumen": narasi})
    
    df = pd.DataFrame(hasil_akhir)
    st.table(df)

    # --- VISUALISASI GRAFIK RADAR ---
    st.write("### Analisis Keseimbangan Dimensi")
    fig = px.line_polar(df, r=[10]*len(df), theta='Dimensi', line_close=True)
    st.plotly_chart(fig)

    # --- FITUR DOWNLOAD PDF (Sederhana) ---
    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Instrumen RPP: {mapel}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Guru: {nama_guru}", ln=True, align='L')
        for index, row in df.iterrows():
            pdf.multi_cell(0, 10, txt=f"{row['Dimensi']} ({row['Pilar']}): {row['Instrumen']}")
        return pdf.output(dest='S').encode('latin-1')

    st.download_button(
        label="📥 Download as PDF",
        data=generate_pdf(),
        file_name="Instrumen_RPP_DeepLearning.pdf",
        mime="application/pdf"
    )