from PIL import Image

def getImage(filename):
    try:
        image = Image.open(filename, 'r')
        print("    Image loaded successfully!")
        return image
    except:
        print("    Error: Image not found.")
        return None

def convertImage(image_jpg, output_name):
    pix_val = list(image_jpg.convert("RGB").getdata())
    r_index = 0
    g_index = 1
    b_index = 2
    opacity_index = 3 # Probably unneccesary since jpeg doesn't have transparency.

    pix_count = 0

    output = open(f"{output_name}.txt", "w+")

    for pixel in pix_val:
        # print(f"({pixel[r_index]}, {pixel[g_index]}, {pixel[b_index]})")
        if pixel[r_index] < 20 and pixel[g_index] < 20 and pixel[b_index] < 20:
            output.write("1 ")
        else:
            output.write("  ")

        if (pix_count + 1) % 128 == 0:
            output.write(f"\n")

        pix_count += 1


def main():
    print("-_-_-_-_- Welcome to the Image Converter! -_-_-_-_-\n")
    print("    What is the name of the image file?")
    #file_name = input("    > ")
    file_name = "small.jpg"
    print("    What is the name of the output file?")
    #output_name = input("    > ")
    output_name = "output"

    image = getImage(file_name)
    if image == None:
        print("    Error: Image not found.")
        return
    else:
        print("    Image loaded successfully!")
        binary_image = convertImage(image, output_name)
        print("    Image converted successfully!")
    

if __name__ == "__main__":
    main()