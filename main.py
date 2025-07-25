from PIL import Image

# open image
img_url = "/home/arnavdeeps/Desktop/wallpaper.png"

# open image
img = Image.open(img_url)

height = img.height
width = img.width
aspect_ratio = height/width

CHAR = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,^`'.-" # reverse this list for brightness inversion

def processImage(image):

    # convert to grayscale
    grayscale = image.convert("L")

    # resize image
    resized = image.resize((256,int(round(256*aspect_ratio))))

    return resized

processed = processImage(img)

def getGrayscaleVal(processedImage):
    brightnessMap = []
    pixels = processedImage.load()
    if len(pixels[0,0]) == 3:
        for x in range(255):
            for y in range(int(round(256*aspect_ratio))-1):
                R,G,B = pixels[x,y]
                brightness = sum([R,G,B])/3
                brightnessMap.append(int(brightness))
    elif len(pixels[0,0]) == 4:
        for x in range(255):
            for y in range(int(round(256*aspect_ratio))-1):
                R,G,B,A = pixels[x,y]
                brightness = sum([R,G,B])/3
                brightnessMap.append(int(brightness))
    else:
        raise("file type incompatible")
    return brightnessMap

def makeAscii(map):
    ascii = ""
    for n in map:
        if (len(ascii) % 256 == 0):
            ascii = ascii + "\n"
        ascii = ascii + CHAR[int(round((n/4)))]
    return ascii


with open("demofile.txt", "a") as f:
  f.write(makeAscii(getGrayscaleVal(processed)))

#open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read()) 

# print(makeAscii(getGrayscaleVal(processed)))

# display image
# processed.show()

