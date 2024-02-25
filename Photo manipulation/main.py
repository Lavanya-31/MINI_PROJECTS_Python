from PIL import Image, ImageFilter

# Open the image file
image_path = r"C:\Users\Lavanya G\Pictures\photo"
image = Image.open(image_path)

# Display the original image
image.show()

# Convert the image to grayscale
grayscale_image = image.convert("L")
grayscale_image.show()

# Rotate the image by 90 degrees
rotated_image = image.rotate(90)
rotated_image.show()

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

# Crop the image
crop_box = (100, 100, 400, 400)  # Define the box (left, upper, right, lower)
cropped_image = image.crop(crop_box)
cropped_image.show()

# Resize the image
new_size = (300, 300)
resized_image = image.resize(new_size)
resized_image.show()

# Save the manipulated image
resized_image.save("resized_example.jpg")
