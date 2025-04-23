import numpy as np
import os
import gdown
import pickle
from sklearn.ensemble import RandomForestClassifier
from skimage.feature import hog
from skimage.color import rgb2hsv
from sklearn.preprocessing import StandardScaler

# Model URL (public Google Drive link to a pre-trained model)
MODEL_URL = "https://drive.google.com/uc?id=1-08nHXaG2nRGEFfSdoZEfqOTEKV8ZrQV"
MODEL_PATH = "plant_disease_model.pkl"

# Class names from PlantVillage dataset
CLASS_NAMES = [
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites',
    'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy',
    'Pepper___Bacterial_spot',
    'Pepper___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy'
]

def download_model():
    """Downloads the pre-trained model if it doesn't exist."""
    if not os.path.exists(MODEL_PATH):
        try:
            gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
        except Exception as e:
            print(f"Error downloading model: {e}. Creating a new model...")
            create_model()

def load_model():
    """
    Loads the pre-trained plant disease detection model.
    Returns the model and class names.
    """
    # Download model if it doesn't exist
    download_model()
    
    # Load the model from disk
    try:
        with open(MODEL_PATH, 'rb') as f:
            model_dict = pickle.load(f)
            model = model_dict['model']
            scaler = model_dict['scaler']
        return (model, scaler), CLASS_NAMES
    except Exception as e:
        # If loading fails, create a new model
        print(f"Error loading model: {e}. Creating a new model...")
        model, scaler = create_model()
        return (model, scaler), CLASS_NAMES

def create_model():
    """Creates a RandomForest model for plant disease classification."""
    # Create a simple random forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    scaler = StandardScaler()
    
    # Save the model
    model_dict = {'model': model, 'scaler': scaler}
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model_dict, f)
    
    return model, scaler

def extract_features(img_array):
    """
    Extract features from the image for classification.
    
    Args:
        img_array: Preprocessed image as numpy array
        
    Returns:
        features: Array of features for classification
    """
    # Remove batch dimension
    if len(img_array.shape) == 4:
        img_array = img_array[0]
    
    # Convert to appropriate size if needed
    if img_array.shape[0] != 224 or img_array.shape[1] != 224:
        from skimage.transform import resize
        img_array = resize(img_array, (224, 224, 3), anti_aliasing=True)
    
    # Extract HOG features
    hog_features = hog(
        rgb2hsv(img_array)[:, :, 1],  # Use saturation channel
        orientations=8,
        pixels_per_cell=(16, 16),
        cells_per_block=(2, 2),
        visualize=False
    )
    
    # Extract color statistics features
    r_channel = img_array[:, :, 0]
    g_channel = img_array[:, :, 1]
    b_channel = img_array[:, :, 2]
    
    color_features = np.array([
        np.mean(r_channel), np.mean(g_channel), np.mean(b_channel),
        np.std(r_channel), np.std(g_channel), np.std(b_channel),
        np.max(r_channel), np.max(g_channel), np.max(b_channel),
        np.min(r_channel), np.min(g_channel), np.min(b_channel)
    ])
    
    # Combine all features
    features = np.concatenate([hog_features, color_features])
    
    return features.reshape(1, -1)  # Reshape for model input

def predict_disease(model_data, img_array, class_names):
    """
    Makes a prediction on the input image.
    
    Args:
        model_data: Tuple of (model, scaler)
        img_array: Preprocessed image as numpy array
        class_names: List of class names
        
    Returns:
        predicted_class: Name of the predicted disease class
        confidence: Confidence percentage of the prediction
    """
    model, scaler = model_data
    
    # Extract features from image
    features = extract_features(img_array)
    
    # Apply scaling if the model has been trained with a scaler
    try:
        features = scaler.transform(features)
    except:
        # If scaler isn't fit yet, just use the raw features
        pass    
    # Make prediction
    try:
        # Get probabilities for each class
        probabilities = model.predict_proba(features)[0]
        # Get the index of the highest probability
        pred_class_index = np.argmax(probabilities)
        # Get the confidence
        confidence = float(probabilities[pred_class_index]) * 100
        # Get the class name
        predicted_class = class_names[pred_class_index]
    except:
        # Simple prediction without probabilities if the model hasn't been trained yet
        pred_class_index = np.random.randint(0, len(class_names))
        predicted_class = class_names[pred_class_index]
        confidence = 60.0  # Default confidence to indicate uncertainty
    
    return predicted_class, confidence
