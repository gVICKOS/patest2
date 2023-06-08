import streamlit as st 
#import math
import pickle
st.write('hello world') 
file_pi2= open('piii.pkl','rb')
obj= pickle.load(file_pi2)
st.write(obj)
