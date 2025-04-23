import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# Create directory if it doesn't exist
os.makedirs('sample_images', exist_ok=True)

# Function to create a sample tomato leaf with bacterial spot
def create_tomato_bacterial_spot():
    # Create base image (green leaf)
    img = Image.new('RGB', (400, 400), (30, 120, 20))
    
    # Create leaf shape
    draw = ImageDraw.Draw(img)
    # Draw leaf outline
    points = [(200, 50), (300, 150), (350, 250), (200, 350), (50, 250), (100, 150)]
    draw.polygon(points, fill=(40, 140, 30))
    
    # Draw leaf veins
    draw.line([(200, 50), (200, 350)], fill=(30, 110, 20), width=5)
    draw.line([(200, 150), (300, 150)], fill=(30, 110, 20), width=3)
    draw.line([(200, 200), (100, 200)], fill=(30, 110, 20), width=3)
    draw.line([(200, 250), (300, 250)], fill=(30, 110, 20), width=3)
    
    # Add bacterial spot symptoms (small dark spots)
    for _ in range(50):
        x = np.random.randint(100, 300)
        y = np.random.randint(100, 300)
        radius = np.random.randint(2, 8)
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(60, 40, 30))
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    
    # Save the image
    img.save('sample_images/tomato_bacterial_spot.jpg')
    return "sample_images/tomato_bacterial_spot.jpg"

# Function to create a sample tomato leaf with early blight
def create_tomato_early_blight():
    # Create base image (green leaf)
    img = Image.new('RGB', (400, 400), (30, 120, 20))
    
    # Create leaf shape
    draw = ImageDraw.Draw(img)
    # Draw leaf outline
    points = [(200, 50), (300, 150), (350, 250), (200, 350), (50, 250), (100, 150)]
    draw.polygon(points, fill=(40, 140, 30))
    
    # Draw leaf veins
    draw.line([(200, 50), (200, 350)], fill=(30, 110, 20), width=5)
    draw.line([(200, 150), (300, 150)], fill=(30, 110, 20), width=3)
    draw.line([(200, 200), (100, 200)], fill=(30, 110, 20), width=3)
    draw.line([(200, 250), (300, 250)], fill=(30, 110, 20), width=3)
    
    # Add early blight symptoms (concentric rings)
    for _ in range(8):
        center_x = np.random.randint(120, 280)
        center_y = np.random.randint(120, 280)
        
        # Draw concentric circles for target-like appearance
        for radius in range(5, 20, 4):
            color_val = 80 - radius * 2 if radius % 8 == 1 else 120 - radius * 2
            draw.ellipse(
                (center_x-radius, center_y-radius, center_x+radius, center_y+radius), 
                outline=(color_val, color_val//2, 10),
                width=2
            )
            
        # Add some brown coloration around
        for i in range(12):
            angle = i * 30
            x = center_x + int(25 * np.cos(np.radians(angle)))
            y = center_y + int(25 * np.sin(np.radians(angle)))
            radius = np.random.randint(3, 8)
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(80, 60, 10))
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    
    # Save the image
    img.save('sample_images/tomato_early_blight.jpg')
    return "sample_images/tomato_early_blight.jpg"

# Function to create a sample healthy tomato leaf
def create_healthy_tomato():
    # Create base image (green leaf)
    img = Image.new('RGB', (400, 400), (30, 120, 20))
    
    # Create leaf shape
    draw = ImageDraw.Draw(img)
    # Draw leaf outline
    points = [(200, 50), (300, 150), (350, 250), (200, 350), (50, 250), (100, 150)]
    draw.polygon(points, fill=(40, 140, 30))
    
    # Draw leaf veins
    draw.line([(200, 50), (200, 350)], fill=(30, 110, 20), width=5)
    draw.line([(200, 150), (300, 150)], fill=(30, 110, 20), width=3)
    draw.line([(200, 200), (100, 200)], fill=(30, 110, 20), width=3)
    draw.line([(200, 250), (300, 250)], fill=(30, 110, 20), width=3)
    
    # Add some texture with slightly different green colors
    for _ in range(100):
        x = np.random.randint(100, 300)
        y = np.random.randint(100, 300)
        radius = np.random.randint(2, 5)
        green_val = np.random.randint(120, 150)
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(20, green_val, 15))
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.1)
    
    # Save the image
    img.save('sample_images/tomato_healthy.jpg')
    return "sample_images/tomato_healthy.jpg"

# Function to create a sample potato leaf with late blight
def create_potato_late_blight():
    # Create base image (green leaf)
    img = Image.new('RGB', (400, 400), (40, 130, 30))
    
    # Create leaf shape
    draw = ImageDraw.Draw(img)
    # Draw leaf outline - potato leaf shape
    points = [(200, 50), (280, 120), (320, 200), (280, 280), (200, 320), (120, 280), (80, 200), (120, 120)]
    draw.polygon(points, fill=(50, 150, 40))
    
    # Draw leaf veins
    draw.line([(200, 50), (200, 320)], fill=(40, 120, 30), width=4)
    for i in range(3):
        y = 120 + i * 60
        draw.line([(200, y), (320, y)], fill=(40, 120, 30), width=2)
        draw.line([(200, y), (80, y)], fill=(40, 120, 30), width=2)
    
    # Add late blight symptoms (dark brown/black irregular patches)
    for _ in range(5):
        center_x = np.random.randint(120, 280)
        center_y = np.random.randint(120, 280)
        
        # Create an irregular shape for the blight patch
        for i in range(20):
            angle = np.random.randint(0, 360)
            distance = np.random.randint(10, 40)
            x = center_x + int(distance * np.cos(np.radians(angle)))
            y = center_y + int(distance * np.sin(np.radians(angle)))
            radius = np.random.randint(5, 15)
            # Dark brown to black color for late blight
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(30, 20, 10))
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    # Add some white fuzzy appearance (characteristic of late blight)
    for _ in range(30):
        x = np.random.randint(100, 300)
        y = np.random.randint(100, 300)
        radius = np.random.randint(1, 3)
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(200, 200, 200))
    
    # Save the image
    img.save('sample_images/potato_late_blight.jpg')
    return "sample_images/potato_late_blight.jpg"

# Create all sample images
created_files = [
    create_tomato_bacterial_spot(),
    create_tomato_early_blight(),
    create_healthy_tomato(),
    create_potato_late_blight()
]

print(f"Created sample images: {created_files}")