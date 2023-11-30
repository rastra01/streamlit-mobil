import pickle 
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi harga mobil bekas')

year = st.number_input('Inpur Tahun Mobil')
mileage = st.number_input('Inpur Km Mobil')
tax = st.number_input('Input Pajk Mobil')
mpg = st.number_input('input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')


predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year,mileage,tax,mpg,engineSize]]
    )
    st.write('Estimasi harga mobil bekas Ponds :', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) :' , predict*19000)