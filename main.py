# --- SIDEBAR INPUT ---
st.sidebar.header("Konfigurasi Instrumen")
nama_guru = st.sidebar.text_input("Nama Guru")
mapel = st.sidebar.text_input("Mata Pelajaran")
# FITUR BARU: Input Nama Siswa
nama_siswa = st.sidebar.text_input("Nama Siswa/Subjek yang Dinilai", placeholder="Contoh: Budi Santoso")

dimensi_terpilih = st.sidebar.multiselect(
    "Pilih Dimensi Profil Lulusan:",
    list(data_instrumen.keys())
)

pilar_fokus = st.sidebar.radio("Fokus Pilar Deep Learning:", ["Mindful", "Meaningful", "Joyful"])

# --- PROSES GENERATE ---
if st.sidebar.button("Generate Instrumen & Rubrik"):
    if not nama_siswa:
        st.error("Silakan masukkan Nama Siswa terlebih dahulu!")
    else:
        st.write(f"### Draf Asesmen Deep Learning")
        st.write(f"**Subjek yang Dinilai:** {nama_siswa}")
        
        hasil_akhir = []
        for dim in dimensi_terpilih:
            with st.expander(f"Dimensi: {dim} ({pilar_fokus})", expanded=True):
                # Menambahkan nama siswa ke dalam narasi secara otomatis
                narasi_dasar = data_instrumen[dim][pilar_fokus]
                narasi_personal = f"Untuk siswa bernama **{nama_siswa}**: {narasi_dasar}"
                
                st.info(narasi_personal)
                
                # Data untuk tabel & PDF
                hasil_akhir.append({
                    "Siswa": nama_siswa,
                    "Dimensi": dim, 
                    "Pilar": pilar_fokus, 
                    "Instrumen": narasi_personal
                })

        # --- UPDATE PDF GENERATOR ---
        # Pastikan fungsi PDF Anda mencantumkan nama siswa di header atau tabel
