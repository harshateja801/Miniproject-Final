import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

class_names = np.array(sorted(['Disaster Happened', 'No Disaster Happened']))

def damage_classification(img):

    image = np.zeros((1, 1024, 1024, 3), dtype=np.uint8)
    image[0] = img
    model = tf.keras.models.load_model('C:/Users/harsh/OneDrive/Documents/Final/Miniproject/ml-models/model1.h5')
    prediction = model.predict(image).tolist()[0]
    
    results = {class_names[i]: round(prediction[i] * 100, 2) for i in range(len(class_names))}
   
    for class_name, percentage in results.items():
           st.markdown(f"<h3 style='font-size: 24px;'>{class_name}: {percentage}%</h3>", unsafe_allow_html=True)
# Create a Streamlit web app
st.title('Damage Classification')

# Create a file uploader to upload the image
uploaded_file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)

    # Resize the image to 1024x1024
    resized_image = image.resize((1024, 1024))
  
    resized_image1 = image.resize((512, 512))
    image_width = int(image.size[0] * 0.25)  # Decrease the image width to 50%
    image_height = int(image.size[1] * 0.25)  # Decrease the image height to 50%
    image = image.resize((image_width, image_height))  # Decrease the image size
    st.image(image, caption="Uploaded Image",)

    # Convert the image to numpy array
    input_data = np.array(resized_image)

    # Make predictions
    predictions = damage_classification(input_data)
  

    # Display the predicted class label
    
