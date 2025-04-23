import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# Create directory if it doesn't exist
os.makedirs('sample_images/realistic', exist_ok=True)

def create_leaf_base(width=400, height=300, color_base=(40, 140, 30)):
    """Create a basic leaf image with a lighter green base color."""
    img = Image.new('RGB', (width, height), (240, 240, 240))  # White background
    draw = ImageDraw.Draw(img)
    
    # Draw a leaf shape
    leaf_points = [
        (width//2, 20),                   # Top point
        (width-50, height//3),            # Right top curve
        (width-30, height//2),            # Right middle
        (width-50, 2*height//3),          # Right bottom curve
        (width//2, height-20),            # Bottom point
        (50, 2*height//3),                # Left bottom curve
        (30, height//2),                  # Left middle
        (50, height//3)                   # Left top curve
    ]
    
    # Fill with base green color
    draw.polygon(leaf_points, fill=color_base)
    
    # Draw main vein
    draw.line([(width//2, 20), (width//2, height-20)], fill=(30, 110, 20), width=3)
    
    # Draw side veins
    for i in range(1, 6):
        y = 20 + i * (height-40) // 6
        # Right veins
        draw.line([(width//2, y), (width-70, y+10)], fill=(30, 110, 20), width=2)
        # Left veins
        draw.line([(width//2, y), (70, y+10)], fill=(30, 110, 20), width=2)
    
    return img

# Function to create a tomato leaf with bacterial spot
def create_tomato_bacterial_spot():
    img = create_leaf_base(color_base=(45, 145, 35))
    draw = ImageDraw.Draw(img)
    
    # Add bacterial spot symptoms (small dark spots)
    for _ in range(50):
        x = np.random.randint(70, 330)
        y = np.random.randint(50, 250)
        radius = np.random.randint(2, 7)
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(80, 50, 30))
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    
    # Save the image
    output_path = 'sample_images/realistic/tomato_bacterial_spot.jpg'
    img.save(output_path)
    return output_path

# Function to create a tomato leaf with early blight
def create_tomato_early_blight():
    img = create_leaf_base(color_base=(45, 145, 35))
    draw = ImageDraw.Draw(img)
    
    # Add early blight symptoms (concentric rings)
    for _ in range(6):
        center_x = np.random.randint(80, 320)
        center_y = np.random.randint(60, 240)
        
        # Create yellowing around
        for radius in range(20, 35, 2):
            draw.ellipse(
                (center_x-radius, center_y-radius, center_x+radius, center_y+radius), 
                outline=(150, 150, 30),
                width=1
            )
        
        # Draw concentric rings
        for radius in range(5, 20, 4):
            draw.ellipse(
                (center_x-radius, center_y-radius, center_x+radius, center_y+radius), 
                outline=(100, 70, 20),
                width=2
            )
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    
    # Save the image
    output_path = 'sample_images/realistic/tomato_early_blight.jpg'
    img.save(output_path)
    return output_path

# Function to create a healthy tomato leaf
def create_healthy_tomato():
    img = create_leaf_base(color_base=(50, 160, 40))
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    
    # Enhance brightness and contrast slightly
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.1)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.1)
    
    # Save the image
    output_path = 'sample_images/realistic/tomato_healthy.jpg'
    img.save(output_path)
    return output_path

# Function to create a potato leaf with late blight
def create_potato_late_blight():
    img = create_leaf_base(color_base=(40, 130, 30))
    draw = ImageDraw.Draw(img)
    
    # Add late blight symptoms (dark irregular patches with white edges)
    for _ in range(3):
        center_x = np.random.randint(80, 320)
        center_y = np.random.randint(60, 240)
        
        # Create a dark patch
        points = []
        for angle in range(0, 360, 30):
            radius = np.random.randint(20, 40)
            x = center_x + int(radius * np.cos(np.radians(angle)))
            y = center_y + int(radius * np.sin(np.radians(angle)))
            points.append((x, y))
        
        # Draw the dark patch
        draw.polygon(points, fill=(30, 20, 10))
        
        # Add white fuzzy edges
        for _ in range(15):
            edge_x = center_x + np.random.randint(-30, 30)
            edge_y = center_y + np.random.randint(-30, 30)
            radius = np.random.randint(1, 3)
            draw.ellipse(
                (edge_x-radius, edge_y-radius, edge_x+radius, edge_y+radius), 
                fill=(220, 220, 220)
            )
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    
    # Save the image
    output_path = 'sample_images/realistic/potato_late_blight.jpg'
    img.save(output_path)
    return output_path

# Create all realistic sample images
created_files = [
    create_tomato_bacterial_spot(),
    create_tomato_early_blight(),
    create_healthy_tomato(),
    create_potato_late_blight()
]

print(f"Created realistic sample images: {created_files}")