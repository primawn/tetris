import streamlit as st
import pandas as pd
import data
import map

#STREAMLIT
#Create header
st.markdown("<h1 style='text-align: center'>Hubungan Prevalensi Diabetes Melitus dengan Prevalensi TB Paru di Pulau Jawa Tahun 2020</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center'>Prima Widiani | Tetris Program 2022</h5>", unsafe_allow_html=True)
st.markdown("----")

# st.write("""Latar Belakang""")
st.write("Diabetes melitus merupakan penyakit yang menyebabkan gangguan metabolisme kronis pada tubuh (WHO, 1999). Hal ini menyebabkan tingginya kadar gula darah, terganggunya produksi insulin dalam tubuh, dan seringkali juga memberikan peluang bagi penyakit lain untuk masuk ke tubuh kita, salah satunya adalah TBC. Tuberkulosis (TBC/TB) adalah penyakit mudah menular yang disebabkan oleh infeksi bakteri, yang pada umumnya menyerang paru-paru.")
st.write("Hidup yang menjadi lebih mudah di kemajuan teknologi ini membuat kita seringkali menjadi lalai dalam menjaga gaya hidup dan pola makan. Menurut WHO, gaya hidup yang tidak baik tersebut merupakan salah satu pemicu diabetes melitus (Kemkes, 2018), yang mana sejauh ini penderita diabetes melitus semakin bertambah banyak.")
st.write("Oleh karena itu, muncullah pertanyaan: jika prevalensi diabetes melitus di provinsi-provinsi Pulau Jawa pada 2020 dibandingkan satu sama lain dan dihubungkan dengan prevalensi TB paru, apakah angka yang didapat akan linear? Jika prevalensi DM di suatu daerah merupakan angka terbesar dibandingkan provinsi lain, apakah prevalensi TB di daerah tersebut juga mencapai angka tertinggi?")

st.markdown("<h5 style='text-align: left;'>Persebaran "+map.select_data+" di Pulau Jawa</h5>", unsafe_allow_html=True)
map.show_maps(map.select_data, map.threshold(map.select_data))



choice_prov = st.selectbox(
    '<h5>Prevalensi Diabetes Melitus dan TBC berdasarkan Provinsi</h5>',
    ('Semua Data', 'DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'))

if choice_prov == "Semua Data":
         st.table(data.datajawa)
if choice_prov == "DKI Jakarta":
         st.table(data.jkt_data)
if choice_prov == "Banten":
         st.table(data.banten_data)
if choice_prov == "DI Yogyakarta":
         st.table(data.diy_data)
if choice_prov == "Jawa Barat":
         st.table(data.jabar_data)
if choice_prov == "Jawa Tengah":
         st.table(data.jateng_data)
if choice_prov == "Jawa Timur":
         st.table(data.jatim_data)
         
st.caption("(Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa)")

st.write("Seperti yang ditunjukkan pada tabel data prevalensi TB dan DM di masing-masing Kabupaten/Kota per Provinsi diatas, di Kota Sidoarjo, Provinsi Jawa Timur, terdapat 73559 orang penderita DM pada tahun 2020. Prevalensi DM yang jika dibandingkan dengan Kabupaten/Kota lain, contohnya Kota Mojokerto, merupakan angka yang lebih sedikit karena pada tahun 2020 Mojokerto mencapai prevalensi DM di angka 89200.")
st.write("Jika melihat pada data prevalensi TB dan DM di tiap kabupaten/kota pada masing-masing Provinsi, dapat disimpulkan bahwa dari data yang terlihat menunjukkan bahwa tingginya prevalensi DM di suatu kabupaten/kota tidak selalu diiringi dengan tingginya prevalensi TB. Beberapa daerah yang menjadi daerah dengan angka prevalensi DM tertinggi belum tentu menjadi daerah yang mempunyai angka prevalensi TB yang tinggi juga.")
       
chart_data = pd.DataFrame(
    data.datajawa,
    columns=["Penderita Tuberkulosis", "Penderita Diabetes"],
    index=data.datajawa['Provinsi']    
)

st.bar_chart(chart_data)
st.markdown("<h6 style='text-align: center;'>Jumlah Penderita Tuberkulosis dan Diabetes di Pulau Jawa</h6>", unsafe_allow_html=True)

st.write("Terlebih lagi, jika mengacu pada diagram batang di atas, dapat dilihat bahwa ternyata data penderita kedua penyakit tersebut adalah tidak berhubungan. Tingginya angka penderita Diabetes tidak linear dengan angka penderita TB. Meskipun jumlah penderita diabetes mencapai angka tertinggi diantara provinsi lain di Pulau Jawa, namun jumlah penderita TB di Jawa Barat masih lebih sedikit daripada di Jawa Tengah yang merupakan provinsi dengan jumlah penderita Tuberkulosis tertinggi di Pulau Jawa.")

st.caption("Sumber:")
st.caption("Imkasari, Pradanis Yanuarinda. “Pengaruh Imunitas Terhadap Penderita Diabetes Melitus.” Fakultas Keperawatan Universitas Airlangga, http://ners.unair.ac.id/site/index.php/news-fkp-unair/30-lihat/1026-pengaruh-imunitas-terhadap-penderita-diabetes-melitus.")
st.caption("“Penyakit Diabetes Melitus.” Direktorat P2PTM, Kementerian Kesehatan Republik Indonesia, http://p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus.")

