import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps

# Create directory if it doesn't exist
os.makedirs('sample_images/realistic', exist_ok=True)

# Function to create a more realistic tomato leaf with bacterial spot
def create_realistic_tomato_bacterial_spot():
    # Base size
    width, height = 600, 400
    
    # Create a base green leaf with texture
    img = Image.new('RGB', (width, height), (20, 80, 15))
    
    # Create a more realistic leaf texture
    for i in range(width):
        for j in range(height):
            # Add some noise to create texture
            noise = np.random.randint(-10, 10)
            # Calculate distance from center for a leaf-like shape
            dist_x = (i - width/2) / (width/2)
            dist_y = (j - height/2) / (height/2)
            dist = np.sqrt(dist_x**2 + dist_y**2)
            
            # Make a leaf-like shape
            if dist < 0.9 + 0.1 * np.sin(i/20) + 0.1 * np.sin(j/20):
                r = 30 + noise + int(20 * dist)
                g = 120 + noise - int(40 * dist)
                b = 20 + noise
                img.putpixel((i, j), (max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255))))
            else:
                img.putpixel((i, j), (240, 240, 240))  # Background
    
    # Draw leaf veins
    draw = ImageDraw.Draw(img)
    # Main vein
    draw.line([(width/2, 20), (width/2, height-20)], fill=(15, 60, 10), width=5)
    
    # Secondary veins
    for i in range(5):
        y = 50 + i * 70
        # Left side veins
        draw.line([(width/2, y), (100, y-30)], fill=(15, 60, 10), width=3)
        # Right side veins
        draw.line([(width/2, y), (width-100, y-30)], fill=(15, 60, 10), width=3)
    
    # Add bacterial spot symptoms (small circular lesions)
    for _ in range(80):
        x = np.random.randint(100, width-100)
        y = np.random.randint(50, height-50)
        
        if np.random.random() < 0.7:  # 70% chance for a dark spot
            radius = np.random.randint(3, 8)
            color = (np.random.randint(60, 90), np.random.randint(20, 40), np.random.randint(10, 30))
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)
            
            # Add yellow halo around some spots
            if np.random.random() < 0.5:
                halo_radius = radius + np.random.randint(2, 5)
                draw.ellipse(
                    (x-halo_radius, y-halo_radius, x+halo_radius, y+halo_radius), 
                    outline=(180, 180, 30), 
                    width=2
                )
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    # Enhance contrast and color
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.1)
    
    # Add some shadows and highlights
    for _ in range(1000):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        radius = np.random.randint(1, 4)
        if np.random.random() < 0.5:
            # Highlight
            opacity = np.random.randint(10, 30)
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(255, 255, 255, opacity))
        else:
            # Shadow
            opacity = np.random.randint(10, 30)
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=(0, 0, 0, opacity))
    
    # Save the image
    output_path = 'sample_images/realistic/tomato_bacterial_spot.jpg'
    img.save(output_path, quality=95)
    return output_path

# Function to create a more realistic tomato leaf with early blight
def create_realistic_tomato_early_blight():
    # Base size
    width, height = 600, 400
    
    # Create a base green leaf with texture
    img = Image.new('RGB', (width, height), (20, 80, 15))
    
    # Create a more realistic leaf texture
    for i in range(width):
        for j in range(height):
            # Add some noise to create texture
            noise = np.random.randint(-10, 10)
            # Calculate distance from center for a leaf-like shape
            dist_x = (i - width/2) / (width/2)
            dist_y = (j - height/2) / (height/2)
            dist = np.sqrt(dist_x**2 + dist_y**2)
            
            # Make a leaf-like shape
            if dist < 0.9 + 0.1 * np.sin(i/20) + 0.1 * np.sin(j/20):
                r = 30 + noise + int(20 * dist)
                g = 120 + noise - int(40 * dist)
                b = 20 + noise
                img.putpixel((i, j), (max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255))))
            else:
                img.putpixel((i, j), (240, 240, 240))  # Background
    
    # Draw leaf veins
    draw = ImageDraw.Draw(img)
    # Main vein
    draw.line([(width/2, 20), (width/2, height-20)], fill=(15, 60, 10), width=5)
    
    # Secondary veins
    for i in range(5):
        y = 50 + i * 70
        # Left side veins
        draw.line([(width/2, y), (100, y-30)], fill=(15, 60, 10), width=3)
        # Right side veins
        draw.line([(width/2, y), (width-100, y-30)], fill=(15, 60, 10), width=3)
    
    # Add early blight symptoms (concentric rings and yellowing)
    for _ in range(7):
        center_x = np.random.randint(150, width-150)
        center_y = np.random.randint(80, height-80)
        
        # Create yellowing area around the lesion
        max_radius = np.random.randint(30, 60)
        for i in range(width):
            for j in range(height):
                dist = np.sqrt((i - center_x)**2 + (j - center_y)**2)
                if dist < max_radius:
                    # Get current pixel color
                    r, g, b = img.getpixel((i, j))
                    # Add yellowing effect that fades with distance
                    fade_factor = 1 - (dist / max_radius)
                    yellow_r = int(r + (180 - r) * fade_factor * 0.7)
                    yellow_g = int(g + (180 - g) * fade_factor * 0.7)
                    yellow_b = int(b * (1 - fade_factor * 0.7))  # Reduce blue to make it more yellow
                    img.putpixel((i, j), (min(255, yellow_r), min(255, yellow_g), yellow_b))
        
        # Draw concentric rings for target-like appearance
        for radius in range(5, max_radius, 5):
            # Alternate between dark and lighter brown
            if radius % 10 == 0:
                color = (np.random.randint(80, 100), np.random.randint(50, 70), np.random.randint(10, 30))
            else:
                color = (np.random.randint(100, 120), np.random.randint(70, 90), np.random.randint(30, 50))
                
            draw.ellipse(
                (center_x-radius, center_y-radius, center_x+radius, center_y+radius), 
                outline=color,
                width=2
            )
    
    # Apply some blur for realism
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    # Enhance contrast and color
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.1)
    
    # Save the image
    output_path = 'sample_images/realistic/tomato_early_blight.jpg'
    img.save(output_path, quality=95)
    return output_path

# Function to create a more realistic healthy tomato leaf
def create_realistic_healthy_tomato():
    # Base size
    width, height = 600, 400
    
    # Create a base green leaf with texture
    img = Image.new('RGB', (width, height), (20, 80, 15))
    
    # Create a more realistic leaf texture
    for i in range(width):
        for j in range(height):
            # Add some noise to create texture
            noise = np.random.randint(-10, 10)
            # Calculate distance from center for a leaf-like shape
            dist_x = (i - width/2) / (width/2)
            dist_y = (j - height/2) / (height/2)
            dist = np.sqrt(dist_x**2 + dist_y**2)
            
            # Make a leaf-like shape
            if dist < 0.9 + 0.1 * np.sin(i/20) + 0.1 * np.sin(j/20):
                r = 30 + noise + int(10 * dist)
                g = 140 + noise - int(20 * dist)
                b = 30 + noise
                img.putpixel((i, j), (max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255))))
            else:
                img.putpixel((i, j), (240, 240, 240))  # Background
    
    # Draw leaf veins
    draw = ImageDraw.Draw(img)
    # Main vein
    draw.line([(width/2, 20), (width/2, height-20)], fill=(20, 100, 30), width=5)
    
    # Secondary veins
    for i in range(5):
        y = 50 + i * 70
        # Left side veins
        draw.line([(width/2, y), (100, y-30)], fill=(20, 100, 30), width=3)
        # Right side veins
        draw.line([(width/2, y), (width-100, y-30)], fill=(20, 100, 30), width=3)
    
    # Add some random light spots to create natural texture
    for _ in range(200):
        x = np.random.randint(100, width-100)
        y = np.random.randint(50, height-50)
        radius = np.random.randint(1, 3)
        color = (
            np.random.randint(40, 60), 
            np.random.randint(150, 180), 
            np.random.randint(40, 60)
        )
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)
    
    # Apply light blur for realism
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    
    # Enhance color
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.2)
    
    # Add some shine effects
    for _ in range(50):
        x = np.random.randint(100, width-100)
        y = np.random.randint(50, height-50)
        radius = np.random.randint(2, 6)
        # Add highlight with transparency
        for r in range(radius):
            opacity = int(255 * (1 - r/radius))
            color = (255, 255, 255, opacity)
            draw.ellipse((x-r, y-r, x+r, y+r), fill=color)
    
    # Save the image
    output_path = 'sample_images/realistic/tomato_healthy.jpg'
    img.save(output_path, quality=95)
    return output_path

# Function to create a more realistic potato leaf with late blight
def create_realistic_potato_late_blight():
    # Base size
    width, height = 600, 400
    
    # Create a base green leaf with texture - potato leaves are usually a bit darker
    img = Image.new('RGB', (width, height), (15, 70, 10))
    
    # Create a more realistic leaf texture
    for i in range(width):
        for j in range(height):
            # Add some noise to create texture
            noise = np.random.randint(-10, 10)
            # Calculate distance from center for a leaf-like shape
            dist_x = (i - width/2) / (width/2)
            dist_y = (j - height/2) / (height/2)
            dist = np.sqrt(dist_x**2 + dist_y**2)
            
            # Make a leaf-like shape - potato leaflets are more rounded
            if dist < 0.85 + 0.05 * np.sin(i/15) + 0.05 * np.sin(j/15):
                r = 25 + noise + int(15 * dist)
                g = 110 + noise - int(30 * dist)
                b = 15 + noise
                img.putpixel((i, j), (max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255))))
            else:
                img.putpixel((i, j), (240, 240, 240))  # Background
    
    # Draw leaf veins
    draw = ImageDraw.Draw(img)
    # Main vein
    draw.line([(width/2, 20), (width/2, height-20)], fill=(15, 60, 10), width=4)
    
    # Secondary veins
    for i in range(7):
        y = 40 + i * 50
        # Left side veins
        draw.line([(width/2, y), (150, y-10)], fill=(15, 60, 10), width=2)
        # Right side veins
        draw.line([(width/2, y), (width-150, y-10)], fill=(15, 60, 10), width=2)
    
    # Add late blight symptoms (large dark water-soaked patches with fuzzy white edges)
    for _ in range(4):
        center_x = np.random.randint(150, width-150)
        center_y = np.random.randint(80, height-80)
        
        # Create a large irregular dark patch
        max_radius = np.random.randint(40, 80)
        
        # Draw the main dark area
        for angle in range(0, 360, 5):
            # Create irregular edge
            radius_variation = np.random.randint(-15, 15)
            radius = max_radius + radius_variation
            
            x = center_x + int(radius * np.cos(np.radians(angle)))
            y = center_y + int(radius * np.sin(np.radians(angle)))
            
            # Ensure point is within image bounds
            x = max(0, min(width-1, x))
            y = max(0, min(height-1, y))
            
            # Draw a line from center to this point
            draw.line([(center_x, center_y), (x, y)], fill=(30, 20, 10), width=3)
        
        # Fill the area with dark color
        for i in range(width):
            for j in range(height):
                dist = np.sqrt((i - center_x)**2 + (j - center_y)**2)
                if dist < max_radius + np.random.randint(-15, 15):
                    # Dark brown to black color for late blight
                    img.putpixel((i, j), (
                        np.random.randint(20, 40),
                        np.random.randint(15, 30),
                        np.random.randint(5, 15)
                    ))
        
        # Add white fuzzy edge in some areas (characteristic of late blight)
        for angle in range(0, 360, 10):
            if np.random.random() < 0.7:  # 70% chance for white fuzzy growth
                edge_x = center_x + int((max_radius + 5) * np.cos(np.radians(angle)))
                edge_y = center_y + int((max_radius + 5) * np.sin(np.radians(angle)))
                
                # Ensure point is within image bounds
                edge_x = max(0, min(width-1, edge_x))
                edge_y = max(0, min(height-1, edge_y))
                
                # Add white fuzzy spots
                for _ in range(np.random.randint(5, 15)):
                    spot_x = edge_x + np.random.randint(-10, 10)
                    spot_y = edge_y + np.random.randint(-10, 10)
                    
                    # Ensure point is within image bounds
                    spot_x = max(0, min(width-1, spot_x))
                    spot_y = max(0, min(height-1, spot_y))
                    
                    radius = np.random.randint(1, 3)
                    draw.ellipse(
                        (spot_x-radius, spot_y-radius, spot_x+radius, spot_y+radius), 
                        fill=(np.random.randint(200, 255), np.random.randint(200, 255), np.random.randint(200, 255))
                    )
    
    # Apply blur for realism
    img = img.filter(ImageFilter.GaussianBlur(1))
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.3)
    
    # Save the image
    output_path = 'sample_images/realistic/potato_late_blight.jpg'
    img.save(output_path, quality=95)
    return output_path

# Create all realistic sample images
created_files = [
    create_realistic_tomato_bacterial_spot(),
    create_realistic_tomato_early_blight(),
    create_realistic_healthy_tomato(),
    create_realistic_potato_late_blight()
]

print(f"Created realistic sample images: {created_files}")