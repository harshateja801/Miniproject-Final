import streamlit as st
import base64
st.set_page_config(
    page_title="Natural Catastrophe Response App",
   
)


def set_background(image_file):
 
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

set_background("C:/Users/harsh/Downloads/Soteria-main (1)/Soteria-main/ml-models/frontend/img(full).jpeg")
st.markdown(
    """
    <style>
    body {
        color: white;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(f'<h1 style="color:white;font-size:100px;">{"Natural Catastrophe Response"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:gold;font-size:24px;">{"Meteorology for natural events isn’t an exact science. Despite advances in technology, no one can tell with complete accuracy when a volcano will erupt, or how powerful a hurricane will be on landfall.However, observation and data are powerful tools, so prediction is getting better and faster."}</h1>', unsafe_allow_html=True)

st.sidebar.success("Select a page above.")
