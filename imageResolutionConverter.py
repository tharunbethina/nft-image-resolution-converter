from PIL import Image

# Path to your original 1280x1280 image
input_path = '../../Downloads/Mypic.jpg'
# Path to save the resized image
output_path = '../7resized_25x25.jpg'

# Open image
image = Image.open(input_path)

if image.mode == 'P':
    image = image.convert('RGB')

# Resize image with high-quality resampling
resized_image = image.resize((70, 70), Image.LANCZOS)

# Save resized image
resized_image.save(output_path)

print(f'Resized image saved at {output_path}')
