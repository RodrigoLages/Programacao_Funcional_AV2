from PIL import Image

input_image = Image.open("q3_input_image.jpg")

output_image = Image.new("RGB", input_image.size)
output_image.putdata([tuple(int(p * .5) for p in pixel) for pixel in input_image.getdata()])
output_image.save("q3_output_image.jpg")

print("Brilho da imagem alterado")
