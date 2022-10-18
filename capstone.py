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
st.write("Hidup yang menjadi lebih mudah di kemajuan teknologi ini membuat kita seringkali menjadi lalai dalam menjaga gaya hidup dan pola makan. Menurut WHO, gaya hidup yang tidak baik tersebut merupakan salah satu pemicu diabetes melitus (Kemkes, 2018), yang mana sejauh ini penderita diabetes melitus semakin bertambah banyak.")
st.write("Diabetes melitus merupakan penyakit yang menyebabkan gangguan metabolisme kronis pada tubuh (WHO, 1999). Hal ini menyebabkan tingginya kadar gula darah, terganggunya produksi insulin dalam tubuh, dan seringkali juga memberikan peluang bagi penyakit lain untuk masuk ke tubuh kita, salah satunya adalah TBC. Tuberkulosis (TBC/TB) adalah penyakit mudah menular yang disebabkan oleh infeksi bakteri, yang pada umumnya menyerang paru-paru. Tidak menutup kemungkinan bahwa penderita DM juga dapat terserang TB karena mudahnya penyakit tersebut untuk menular dan rendahnya imunitas pada pasien DM.")
st.write("Oleh karena itu, muncullah pertanyaan: jika prevalensi diabetes melitus di provinsi-provinsi Pulau Jawa pada 2020 dibandingkan satu sama lain dan dihubungkan dengan prevalensi TB paru, apakah angka yang didapat akan linear? Jika prevalensi DM di suatu daerah merupakan angka terbesar dibandingkan provinsi lain, apakah prevalensi TB di daerah tersebut juga mencapai angka tertinggi?")

st.markdown("<h4 style='text-align: left;'>Persebaran "+map.select_data+" di Pulau Jawa</h4>", unsafe_allow_html=True)
st.caption("(Opsi untuk memilih prevalensi TB/DM dapat dipilih di sidebar)")
map.show_maps(map.select_data, map.threshold(map.select_data))


st.markdown("<h4 style='text-align: left;'>Hubungan Prevalensi DM dan TB di Pulau Jawa Tahun 2020</h4>", unsafe_allow_html=True)

choice_prov = st.selectbox(
    'Data Penderita Diabetes Melitus dan TBC',
    ('Per Provinsi', 'DKI Jakarta','Banten','DI Yogyakarta','Jawa Barat','Jawa Tengah','Jawa Timur','Semua Data'))

if choice_prov == "Per Provinsi":
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
if choice_prov == "Semua Data":
         st.table(data.jawa_data)
         
st.caption("(Data dihimpun dari website resmi Pemerintah Provinsi di pulau Jawa)")

st.write("Seperti yang ditunjukkan pada tabel data prevalensi TB dan DM diatas, Provinsi Jawa Barat mempunyai prevalensi DM tertinggi diantara Provinsi lain di Pulau Jawa dengan jumlah 1078857, sedangkan prevalensi TB tertinggi pada tahun 2020 di Pulau Jawa dimiliki oleh Provinsi Jawa Tengah dengan jumlah 154062. Dari semua Kabupaten/Kota di Pulau Jawa pada tahun 2020, Provinsi Jawa Barat memiliki Kabupaten dan Kota yang memegang jumlah tertinggi baik pada prevalensi DM maupun TB. Kabupaten Bekasi mempunyai prevalensi DM tertinggi dengan jumlah 242169, sementara prevalensi TB tertinggi dimiliki oleh Kota Bogor dengan jumlah 10248.")
st.write("Dari data yang ditunjukkan tabel diatas, dapat diketahui bahwa:" 
         " pertama, di Provinsi DKI Jakarta, Jakarta Selatan memiliki prevalensi DM tertinggi sebesar 63762, sedangkan prevalensi TB tertingginya dimiliki oleh Jakarta Timur."
         " Kedua, pada Provinsi Banten, Kabupaten Tangerang memiliki prevalensi tertinggi pada DM dan TB, berturut-turut sebesar 65661 dan 6089."
         " Ketiga, prevalensi DM tertinggi di Daerah Istimewa Yogyakarta pada tahun 2020 dipegang oleh Kabupaten Kulonprogo dengan jumlah 41193, sementara itu prevalensi TB tertinggi sebesar 632 dimiliki oleh Kabupaten Gunung Kidul."
         " Keempat, di Jawa Tengah, Kabupaten Pemalang memiliki prevalensi DM tertinggi sebesar 77843 (dengan prevalensi TB sebesar 4547) dan Kabupaten Banyumas memiliki prevalensi TB tertinggi sebesar 10189 (dengan prevalensi DM 23858)."
         " Terakhir, pada Provinsi Jawa Timur, prevalensi DM tertinggi sebesar 94624 dan prevalensi TB tertinggi sebesar 4151. Kedua prevalensi tertinggi di Provinsi ini dimiliki oleh Kota Surabaya.")
st.write("Jika melihat pada data prevalensi TB dan DM di tiap Kabupaten/Kota pada masing-masing Provinsi, tingginya prevalensi DM di suatu Kabupaten/Kota tidak selalu diiringi dengan tingginya prevalensi TB. Memang ada beberapa Kabupaten/Kota di sebagian Provinsi yang memiliki prevalensi DM dan TB tertinggi di wilayahnya, namun sebagian besar dari Kabupaten/Kota dari enam Provinsi di Pulau Jawa tidak selalu memiliki prevalensi yang tinggi pada TB dan DM. Beberapa daerah yang menjadi daerah dengan angka prevalensi DM tertinggi belum tentu menjadi daerah yang mempunyai angka prevalensi TB yang tertinggi juga.")
       
chart_data = pd.DataFrame(
    data.datajawa,
    columns=["Penderita Tuberkulosis", "Penderita Diabetes"],
    index=data.datajawa['Provinsi']    
)

st.bar_chart(chart_data)
st.markdown("<h6 style='text-align: center;'>Jumlah Penderita Tuberkulosis dan Diabetes di Pulau Jawa</h6>", unsafe_allow_html=True)

st.write("Terlebih lagi, jika mengacu pada diagram batang di atas, dapat disimpulkan bahwa ternyata data penderita kedua penyakit tersebut tidak berhubungan. Tingginya angka penderita DM tidak linear dengan angka penderita TB. Meskipun jumlah penderita dm mencapai angka tertinggi diantara Provinsi lain di Pulau Jawa, namun jumlah penderita TB di Provinsi Jawa Barat masih lebih sedikit jika dibandingkan dengan Provinsi Jawa Tengah yang merupakan Provinsi dengan jumlah penderita TB tertinggi di Pulau Jawa.")

st.markdown("<h4 style='text-align: left;'>Langkah yang bisa diambil</h4>", unsafe_allow_html=True)
st.write("Meskipun pada tahun 2020 prevalensi DM dan prevalensi TB di Pulau Jawa tidak berhubungan, tetapi alangkah baiknya jika masing-masing individu tidak terlena dengan kemudahan yang ditawarkan oleh kemajuan teknologi saat ini. Penting sekali untuk mengatur dan mengadaptasi pola hidup atau gaya hidup yang sehat, baik untuk penderita DM, penderita TB, penderita keduanya, maupun untuk yang sehat. Tidak hanya membuat tubuh jadi terasa lebih segar dan berat badan lebih terkontrol, mengadopsi gaya hidup sehat juga dapat meningkatkan imunitas tubuh sehingga tidak mudah terserang penyakit. Beberapa gaya hidup sehat yang dapat diterapkan menurut pakar kesehatan adalah seperti mengonsumsi air putih yang cukup untuk melindungi fungsi ginjal dan menghindari dehidrasi, rutin beraktivitas fisik atau berolahraga, menghindari makanan berlemak jahat dan mulai mengonsumsi sayur dan buah-buahan, menerapkan pola makan dengan gizi seimbang, menghindari kafein (di kopi, teh, dan soda), rutin meminum obat (bagi penderita DM maupun TB) sesuai dengan yang dianjurkan dokter, dan rutin melakukan pengecekan kadar gula darah secara berkala.")

link = '[LinkedIn](https://www.linkedin.com/in/primawidiani/)'
button = st.markdown(link, unsafe_allow_html=True)
if st.sidebar.button('LinkedIn'): webbrowser.open_new_tab.(button)
    
st.caption("Sumber:")
st.caption("Bisnis.com. “Saran Pakar Gizi Buat Penderita Diabetes.” Edited by Yayuk Widiyarti, Tempo, TEMPO.CO, 11 Dec. 2019, https://gaya.tempo.co/read/1282451/saran-pakar-gizi-buat-penderita-diabetes.")
st.caption("Imkasari, Pradanis Yanuarinda. “Pengaruh Imunitas Terhadap Penderita Diabetes Melitus.” Fakultas Keperawatan Universitas Airlangga, http://ners.unair.ac.id/site/index.php/news-fkp-unair/30-lihat/1026-pengaruh-imunitas-terhadap-penderita-diabetes-melitus.")
st.caption("“Penyakit Diabetes Melitus.” Direktorat P2PTM, Kementerian Kesehatan Republik Indonesia, http://p2ptm.kemkes.go.id/informasi-p2ptm/penyakit-diabetes-melitus.")
st.caption("“Profil Kesehatan.” Dinas Kesehatan Provinsi DKI Jakarta, https://dinkes.jakarta.go.id/berita/profil/profil-kesehatan.")
st.caption("“Profil Kesehatan.” Dinas Kesehatan Provinsi Jawa Barat, https://diskes.jabarprov.go.id/informasipublik/profil.")
st.caption("“Profil Kesehatan Banten Tahun 2020.” Dinas Kesehatan Provinsi Banten, https://dinkes.bantenprov.go.id/read/profil-kesehatan-provinsi-bant/198/Profil-Kesehatan-Provinsi-Banten-Tahun-2020.html.")
st.caption("“Profil Kesehatan DI Yogyakarta Tahun 2020.” Dinas Kesehatan Daerah Istimewa Yogyakarta,https://dinkes.jogjaprov.go.id/download/download/113")
st.caption("“Profil Kesehatan Provinsi Jawa Tengah 2020.” Badan Pusat Statistik Provinsi Jawa Tengah, https://jateng.bps.go.id/publication/2021/05/28/e645f5998de851c45f0c68c5/profil-kesehatan-provinsi-jawa-tengah-2020.html.")
st.caption("“Profil Kesehatan Provinsi Jawa Timur 2020.” Dinas Kesehatan Provinsi Jawa Timur, https://dinkes.jatimprov.go.id/index.php?r=site/file_list&id_file=10&id_berita=8.")
