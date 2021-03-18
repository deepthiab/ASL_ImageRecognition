import streamlit as st
from tensorflow import keras
from PIL import Image, ImageFilter
from utils import image_prep
import numpy as np
import string
import os

dirname = os.path.dirname(__file__)
modelpath = os.path.join(dirname, 'models')


st.title("American Sign Language Alphabet")

st.subheader('Image Recognition')

# @st.cache
model = keras.models.load_model(modelpath)


st.write('CNN model')

label_dic = {i:string.ascii_uppercase[i] for i in range(26)}
label_dic.pop(9)
label_dic.pop(25)

uploaded_file = st.file_uploader("Choose an image..." , type = 'jpg')

if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    # st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Converting to a gray scale 28x28 pixel image.... ")
    prepped_img = image_prep.imageprepare(uploaded_image)
    st.write("Classifying...")
    prediction = np.argmax(model.predict(prepped_img))
    alphabet = label_dic[prediction]
    st.write(f'The sign was  {alphabet}')

    



