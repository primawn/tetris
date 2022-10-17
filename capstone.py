import streamlit as st
import pandas as pd
import data
import map

#STREAMLIT
#Create header
st.write("""# Hubungan Prevalensi Diabetes Melitus dengan Prevalensi TB Paru di Pulau Jawa Tahun 2020""")
st.write("Prima Widiani | Tetris Program 2022")

map.show_maps(map.select_data, map.threshold(map.select_data))
st.markdown("<h6 style='text-align: center;'>Persebaran "+map.select_data+" di Pulau Jawa</h6>", unsafe_allow_html=True)

# st.write("""Latar Belakang""")
st.write("Hidup yang menjadi lebih mudah di kemajuan teknologi ini membuat kita seringkali menjadi lalai dalam menjaga gaya hidup dan pola makan. Menurut WHO, gaya hidup yang tidak baik tersebut merupakan salah satu pemicu diabetes melitus (Kemkes, 2018), yang mana sejauh ini penderita diabetes melitus semakin bertambah banyak.")


chart_data = pd.DataFrame(
    data.datajawa,
    columns=["Penderita Tuberkulosis", "Penderita Diabetes"],
    index=data.datajawa['Provinsi']    
)

st.bar_chart(chart_data)
st.markdown("<h6 style='text-align: center;'>Jumlah Penderita Tuberkulosis dan Diabetes di Pulau Jawa</h6>", unsafe_allow_html=True)

st.write("Diabetes melitus merupakan suatu penyakit yang menyebabkan gangguan metabolisme kronis pada tubuh (WHO, 1999). Hal ini menyebabkan tingginya kadar gula darah, terganggunya produksi insulin dalam tubuh, dan seringkali juga memberikan peluang bagi penyakit lain untuk masuk ke tubuh kita, salah satunya adalah TBC. Tuberkulosis (TBC/TB) adalah penyakit mudah menular yang disebabkan oleh infeksi bakteri, yang pada umumnya menyerang paru-paru.")
st.write("Namun, jika mengacu pada diagram batang di atas, dapat dilihat bahwa ternyata data penderita kedua penyakit tersebut adalah tidak berhubungan.")
st.write("Meskipun memiliki jumlah penderita Diabetes tertinggi, namun jumlah penderita Tuberkulosis di Jawa Barat masih lebih sedikit daripada di Jawa Tengah yang merupakan provinsi dengan jumlah penderita Tuberkulosis tertinggi di Pulau Jawa.")

choice_prov = st.sidebar.selectbox(
    'Data Penderita Diabetes Melitus dan TBC berdasarkan Provinsi',
    ('Semua Data', 'DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur'))

if choice_prov == "Semua Data":
         st.sidebar.table(data.datajawa)
if choice_prov == "DKI Jakarta":
         st.sidebar.table(data.jkt_data)
if choice_prov == "Banten":
         st.sidebar.table(data.banten_data)
if choice_prov == "DI Yogyakarta":
         st.sidebar.table(data.diy_data)
if choice_prov == "Jawa Barat":
         st.sidebar.table(data.jabar_data)
if choice_prov == "Jawa Tengah":
         st.sidebar.table(data.jateng_data)
if choice_prov == "Jawa Timur":
         st.sidebar.table(data.jatim_data)
         
st.sidebar.caption("(Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa)")
