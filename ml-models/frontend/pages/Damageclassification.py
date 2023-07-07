import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

class_names = np.array(sorted(['disaster happened', 'no disaster happened']))

def damage_classification(img):
    st.write(img.shape)
    image = np.zeros((1, 1024, 1024, 3), dtype=np.uint8)
    image[0] = img
    model = tf.keras.models.load_model('C:/Users/harsh/Downloads/Soteria-main (1)/Soteria-main/ml-models/model1.h5')
    prediction = model.predict(image).tolist()[0]
    st.write(prediction)
    return {class_names[i]: prediction[i] for i in range(len(class_names))}

# Create a Streamlit web app
st.title('Damage Classification')

# Create a file uploader to upload the image
uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Resize the image to 1024x1024
    resized_image = image.resize((1024, 1024))

    # Convert the image to numpy array
    input_data = np.array(resized_image)

    # Make predictions
    predictions = damage_classification(input_data)

    # Display the predicted class label
    st.write('Predictions:', predictions)