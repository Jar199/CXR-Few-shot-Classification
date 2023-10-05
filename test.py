import streamlit as st
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="M3 demo", page_icon=":green_apple:")
st.header('What diseases can be predicted from chest X-ray images?')

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    col1.write("X-ray Image :camera:")
    col1.image(image)

    col2.write("Result :wrench:")
    col2.success('pneumothorax', icon="✅")
    col2.success('pneumonia', icon="✅")
    
col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image :gear:", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("test.jpg")
