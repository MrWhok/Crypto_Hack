from PIL import ImageChops,Image

im1 = Image.open("lemur.png")
im2 = Image.open("flag.png")

im3 = ImageChops.add(ImageChops.subtract(im1, im2), ImageChops.subtract(im2, im1))
im3.show()

