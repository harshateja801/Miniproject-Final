import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

class_names = np.array(sorted(['volcano', 'flooding', 'fire', 'wind', 'tsunami']))
def damage_classification(img):
    st.write(img.shape)
    image = np.zeros((1, 1024, 1024, 3), dtype=np.uint8)
    image[0] = img
    model = tf.keras.models.load_model('C:/Users/harsh/OneDrive/Documents/Final/Miniproject/ml-models/model2.h5')
    prediction = model.predict(image).tolist()[0]

    results = {class_names[i]: round(prediction[i] * 100, 2) for i in range(len(class_names))}
   
    for class_name, percentage in results.items():
           st.markdown(f"<h3 style='font-size: 24px;'>{class_name}: {percentage}%</h3>", unsafe_allow_html=True)
# Create a Streamlit web app
st.title('Disaster Classification')

# Create a file uploader to upload the image
uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    m1=image.resize((512,512))
    st.image(m1, caption='Uploaded Image')
  

    # Resize the image to 1024x1024
    resized_image = image.resize((1024, 1024))

    # Convert the image to numpy array
    input_data = np.array(resized_image)

    # Make predictions
    predictions = damage_classification(input_data)

    # Display the predicted class label
  