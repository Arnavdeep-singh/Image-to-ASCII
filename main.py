from PIL import Image

# open image
img_url = "/home/arnavdeeps/Desktop/statue.jpg"


# open image
img = Image.open(img_url)
THIRD = 1/5

og_height = img.height
og_width = img.width
aspect_ratio = og_width/og_height
width = 256
height = int(width * aspect_ratio * THIRD) 

CHAR = "$@B%8&WM#oahkbdpqwmZO0QLCJUYXzcvunxjft/\\|()1{}[]?i!lI*^+~;:,-_`'.- " [::-1] # reverse this list for brightness inversion
# CHAR = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
def processImage(image):

    # convert to grayscale
    # grayscale = image.convert("L")

    # resize image
    resized = image.resize((width,height))

    return resized

processed = processImage(img)

def getGrayscaleVal(processedImage):
    brightnessMap = []
    pixels = processedImage.load()
    if len(pixels[0,0]) == 3:
        for y in range(height):
            for x in range(width):
                R,G,B = pixels[x,y]
                brightness = sum([R,G,B])/3
                brightnessMap.append(int(brightness))
    elif len(pixels[0,0]) == 4:
        for y in range(height):
            for x in range(width):
                R,G,B,A = pixels[x,y]
                brightness = sum([R,G,B])/3
                brightnessMap.append(int(brightness))
    else:
        raise("file type incompatible")
    return brightnessMap

def makeAscii(map):
    ascii = ""
    for n in map:
        if ((len(ascii) % (width + 1)) == 0):
            ascii = ascii + "\n"
        ascii = ascii + CHAR[int(round((n/3.87)))]
    return ascii



with open("demofile.txt", "a") as f:
  f.write(makeAscii(getGrayscaleVal(processed)))

#open and read the file after the appending:
# with open("demofile.txt") as f:
#     print(f.read()) 
#
# print(makeAscii(getGrayscaleVal(processed)))

# display image
# processed.show()

