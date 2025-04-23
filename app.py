import streamlit as st
import numpy as np
from PIL import Image
import io
from model import load_model, predict_disease
from utils import preprocess_image
from disease_info import get_disease_info

st.set_page_config(
    page_title="Vegetable Disease Detection",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Vegetable Disease Detection")
st.markdown("Upload an image of a vegetable plant leaf to detect if it has a disease.")

if 'prediction_made' not in st.session_state:
    st.session_state.prediction_made = False
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None
if 'confidence' not in st.session_state:
    st.session_state.confidence = None
if 'image' not in st.session_state:
    st.session_state.image = None

# Load model
with st.spinner("Loading model..."):
    try:
        model_data, class_names = load_model()
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("Using a fallback model - accuracy may be reduced.")
        # Create a simple fallback to allow the app to function
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.preprocessing import StandardScaler
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        scaler = StandardScaler()
        model_data = (model, scaler)
        # We'll use the class names defined in model.py

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.info(
        "This application uses a deep learning model to detect diseases in vegetable plants. "
        "Upload a clear image of a plant leaf for the best results."
    )
    
    st.header("Supported Plants")
    st.write("The current model can detect diseases in the following plants:")
    for plant in sorted(set([name.split('___')[0] for name in class_names])):
        st.write(f"- {plant.replace('_', ' ').title()}")
    
    st.header("How to Use")
    st.write("1. Upload an image of a vegetable plant leaf")
    st.write("2. Wait for the model to process the image")
    st.write("3. View the detection results and information about the disease")
    
    st.header("Tips for Best Results")
    st.write("- Use well-lit, clear images")
    st.write("- Focus on the affected part of the plant")
    st.write("- Ensure the image shows the leaf symptoms clearly")

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Upload Plant Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            # Read and display the image
            image_bytes = uploaded_file.getvalue()
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.session_state.image = image
            
            # Process button
            if st.button("Detect Disease"):
                with st.spinner("Processing image..."):
                    # Preprocess image for model
                    processed_img = preprocess_image(image)
                    
                    # Make prediction
                    predicted_class, confidence = predict_disease(model_data, processed_img, class_names)
                    
                    # Update session state
                    st.session_state.prediction_made = True
                    st.session_state.prediction_result = predicted_class
                    st.session_state.confidence = confidence
                    
                    # Force rerun to show results
                    st.rerun()
                    
        except Exception as e:
            st.error(f"Error processing image: {e}")
    else:
        st.info("Please upload an image to begin.")

# Display results in second column if prediction was made
with col2:
    if st.session_state.prediction_made and st.session_state.prediction_result:
        st.subheader("Detection Results")
        
        predicted_class = st.session_state.prediction_result
        confidence = st.session_state.confidence
        
        # Display prediction with confidence
        if "healthy" in predicted_class.lower():
            st.success(f"**Prediction:** {predicted_class.replace('_', ' ').title()}")
        else:
            st.warning(f"**Prediction:** {predicted_class.replace('_', ' ').title()}")
        
        # Create a progress bar for confidence
        st.write(f"**Confidence:** {confidence:.2f}%")
        st.progress(confidence/100)
        
        # Display information about the disease
        st.subheader("Disease Information")
        disease_info = get_disease_info(predicted_class)
        
        if disease_info:
            st.write(f"**Description:** {disease_info['description']}")
            
            with st.expander("See Treatment Methods"):
                for i, treatment in enumerate(disease_info['treatment'], 1):
                    st.write(f"{i}. {treatment}")
            
            with st.expander("See Prevention Tips"):
                for i, prevention in enumerate(disease_info['prevention'], 1):
                    st.write(f"{i}. {prevention}")
        else:
            st.info("No additional information available for this condition.")
# Footer
st.markdown("---")
st.markdown("Developed for educational purposes. This tool is meant to assist in identifying plant diseases but should not replace professional diagnosis.")
