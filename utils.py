import numpy as np
from PIL import Image, ImageEnhance

def preprocess_image(image, target_size=(224, 224)):
    """
    Preprocesses the input image for the model.
    
    Args:
        image: PIL Image object
        target_size: The target size for resizing
        
    Returns:
        A numpy array ready for model prediction
    """
    # Apply some enhancement for better results
    image = enhance_image(image)
    
    # Resize the image
    if image.size != target_size:
        image = image.resize(target_size)
    
    # Convert to array and normalize
    img_array = np.array(image)
    
    # Handle grayscale images by converting to RGB
    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,) * 3, axis=-1)
    
    # Handle RGBA images by removing alpha channel
    if img_array.shape[2] == 4:
        img_array = img_array[:, :, :3]
    
    # Normalize pixel values to [0, 1]
    img_array = img_array.astype(np.float32) / 255.0
    
    # Expand dimensions to create batch
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def get_leaf_area_percentage(image):
    """
    Calculates the percentage of the image that contains green leaf area.
    This can be used as a quality check for the uploaded image.
    
    Args:
        image: PIL Image object
        
    Returns:
        The percentage of green pixels in the image
    """
    # Convert to RGB if not already
    image = image.convert('RGB')
    
    # Convert to numpy array
    img_array = np.array(image)
    
    # Define green range (can be adjusted as needed)
    lower_green = np.array([20, 40, 20])
    upper_green = np.array([100, 255, 100])
    
    # Create mask of green pixels
    green_mask = np.all((img_array >= lower_green) & (img_array <= upper_green), axis=2)
    
    # Calculate percentage
    green_percentage = (np.sum(green_mask) / green_mask.size) * 100
    
    return green_percentage

def enhance_image(image):
    """
    Enhances the image to improve prediction quality.
    
    Args:
        image: PIL Image object
        
    Returns:
        Enhanced PIL Image object
    """
    # Convert to RGB if not already
    image = image.convert('RGB')
    
    # Adjust brightness and contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.2)
    
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.1)
    
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.5)
    
    return image
