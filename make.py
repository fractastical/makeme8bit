from PIL import Image

def convert_to_8bit(image_path, output_path):
    # Open the input image
    original_image = Image.open(image_path)

    # Convert the image to P mode which is 8-bit color palette
    eight_bit_image = original_image.convert('P', palette=Image.ADAPTIVE, colors=256)

    # Save the 8-bit image
    eight_bit_image.save(output_path)

    print(f"Image saved to {output_path}")

def pixelate_image(image_path, output_path, pixel_size):
    # Open the input image
    original_image = Image.open(image_path)
    
    # Calculate the size of the reduced image
    original_width, original_height = original_image.size
    reduced_width = original_width // pixel_size
    reduced_height = original_height // pixel_size
    
    # Resize the image to the reduced size
    reduced_image = original_image.resize((reduced_width, reduced_height), Image.NEAREST)
    
    # Resize the image back to the original size
    pixelated_image = reduced_image.resize((original_width, original_height), Image.NEAREST)
    
    # Convert the pixelated image to 8-bit color palette
    eight_bit_image = pixelated_image.convert('P', palette=Image.ADAPTIVE, colors=256)
    
    # Save the 8-bit pixelated image
    eight_bit_image.save(output_path)
    
    print(f"Pixelated image saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    input_image_path = "PNG/Acid Bomb.png"  # Replace with your input image path
    output_image_path = "output_image.png"  # Replace with your desired output image path
    pixel_size = 10  # Adjust the pixel size to increase or decrease the pixelation effect
    pixelate_image(input_image_path, output_image_path, pixel_size)


    # convert_to_8bit(input_image_path, output_image_path)
