import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                # Extract the least significant bit of each color channel
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Split binary_message into 8-bit chunks
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111111':  # Check for first half of 16-bit delimiter
            next_byte = binary_message[i+8:i+16]
            if next_byte == '11111110':
                break
        char = chr(int(byte, 2))
        message += char

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        sys.exit(1)

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()
