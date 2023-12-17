from PIL import Image
from random import randint

file_name = "danger_zone.png"
with Image.open(file_name) as img:
     pixels = img.load()

x, y = img.size

red_color = 0
not_red = 0
i = 0
j = 0
for _ in range(100):
    for _ in range(100):
        i = randint(0, x - 1)
        j = randint(0, y - 1)
        pixel_color = pixels[i, j]
        if pixel_color == (255, 0, 0, 255):
            red_color += 1
        else:
            not_red += 1

print(x, y)
print("Red Aria using Monte Carlo method: ", float(red_color/(not_red + red_color)*100), "%")
print("Number of red pixels: ", red_color)
print("Number of not red pixels: ", not_red)
print("X, Y:", int(red_color/(not_red + red_color)*x), "X", int(red_color/(not_red + red_color)*y))
print("Aria: ", float(red_color/(not_red + red_color)*42),"square miles")

red_color = 0
not_red = 0

for n in range(x):
    for m in range(y):
        pixel_color = pixels[n, m]
        if pixel_color == (255, 0, 0, 255):
            red_color += 1
        else:
            not_red += 1