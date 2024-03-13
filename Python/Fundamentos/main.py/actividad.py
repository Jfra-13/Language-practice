from email.mime import image
from PIL import Image
import sys
try:
    img = Image.open("polar.png")
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)
#img.show()
img.save("polar.jpg","jpg")