from PIL import Image
import os

def convert_to_8bit(image_path, output_path):
    # Open the input image
    original_image = Image.open(image_path)

    # Convert the image to P mode which is 8-bit color palette
    eight_bit_image = original_image.convert('P', palette=Image.ADAPTIVE, colors=256)

    # Save the 8-bit image
    eight_bit_image.save(output_path)

    print(f"Image saved to {output_path}")

# def pixelate_image(image_path, output_path, pixel_size):
#     # Open the input image
#     original_image = Image.open(image_path)
    
#     # Calculate the size of the reduced image
#     original_width, original_height = original_image.size
#     reduced_width = original_width // pixel_size
#     reduced_height = original_height // pixel_size
    
#     # Resize the image to the reduced size
#     reduced_image = original_image.resize((reduced_width, reduced_height), Image.NEAREST)
    
#     # Resize the image back to the original size
#     pixelated_image = reduced_image.resize((original_width, original_height), Image.NEAREST)
    
#     # Convert the pixelated image to 8-bit color palette
#     eight_bit_image = pixelated_image.convert('P', palette=Image.ADAPTIVE, colors=256)
    
#     # Save the 8-bit pixelated image
#     eight_bit_image.save(output_path)
    
#     print(f"Pixelated image saved to {output_path}")


def pixelate_image(image_path, output_path, pixel_size):
    # Open the input image
    original_image = Image.open(image_path).convert("RGBA")
    
    # Calculate the size of the reduced image
    original_width, original_height = original_image.size
    reduced_width = original_width // pixel_size
    reduced_height = original_height // pixel_size
    
    # Resize the image to the reduced size
    reduced_image = original_image.resize((reduced_width, reduced_height), Image.NEAREST)
    
    # Resize the image back to the original size
    pixelated_image = reduced_image.resize((original_width, original_height), Image.NEAREST)
    
    # Convert the pixelated image to 8-bit color palette
    eight_bit_image = pixelated_image.convert('P', palette=Image.ADAPTIVE, colors=256).convert("RGBA")
    
    # Convert black pixels to gold and make the background transparent
    datas = eight_bit_image.getdata()
    new_data = []
    for item in datas:
        # Change all black (also shades of black) pixels to gold
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            new_data.append((255, 215, 0, 255))  # Gold color
        else:
            new_data.append(item)
    eight_bit_image.putdata(new_data)
    
    # Make the background transparent by setting all white pixels to transparent
    eight_bit_image = eight_bit_image.convert("RGBA")
    datas = eight_bit_image.getdata()
    new_data = []
    for item in datas:
        # Change all white pixels to transparent
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    eight_bit_image.putdata(new_data)
    
    # Save the 8-bit pixelated image with transparency
    eight_bit_image.save(output_path, "PNG")

def process_folder(input_folder, pixel_size):
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Construct the full file path
            input_path = os.path.join(input_folder, filename)
            
            # Construct the output file path with "_8bit" suffix
            file_name, file_extension = os.path.splitext(filename)
            output_filename = f"{file_name}_8bit8{file_extension}"
            output_path = os.path.join(input_folder, output_filename)
            
            # Pixelate and convert the image
            pixelate_image(input_path, output_path, pixel_size)
            
            print(f"Processed {filename} and saved as {output_filename}")


if __name__ == "__main__":
    # Example usage
    input_image_path = "PNG/Acid Bomb.png"  # Replace with your input image path
    output_image_path = "output_image.png"  # Replace with your desired output image path
    pixel_size = 8  # Adjust the pixel size to increase or decrease the pixelation effect

    input_folder = "PNG"  # Replace with your input folder path
    process_folder(input_folder, pixel_size)

    # pixelate_image(input_image_path, output_image_path, pixel_size)


    # convert_to_8bit(input_image_path, output_image_path)
