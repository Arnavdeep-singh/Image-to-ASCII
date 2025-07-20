from PIL import Image

# open image
img = Image.open("/home/arnavdeeps/Desktop/Figure_1.png")

# convert to grayscale
grayscale = img.convert("L")

CHAR = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,"^`' # reverse this list for brightness inversion


# display image
grayscale.show()
