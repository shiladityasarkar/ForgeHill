import streamlit as st
import hillforge as hf
import time

def stream_data(des):
    for word in des.split(" "):
        yield word + " "
        time.sleep(0.05)

st.title('The HillForge Test 🕵🏻‍♂️')
hf = hf.HillForge()
img = st.file_uploader(label='image', type=['png','jpg', 'jpeg'], label_visibility='hidden')

if img is not None:
    img_, r = hf.detect(img)

# Create three columns
col1, col2, col3 = st.columns([1,1,2])

with col1:
    st.write('Image on which test is done...')
    try:
        st.image(img, width=300)
    except AttributeError:
        st.write('Image incoming :)')

with col2:
    try:
        st.pyplot(img_)
    except NameError:
        st.write('The graph will appear here...')

with col3:
    try:
        if r:
            des = """
                ## With respect to this `HillForge` graph...
                ## The image looks `Forged` ❌
                """
        else:
            des = """
                ## With respect to this `HillForge` graph...
                ## The image looks `Fine` 😃
                """
    except NameError:
        des = """## made by `shiladitya` with ❤️"""

    st.write_stream(stream_data(des))