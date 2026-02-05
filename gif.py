import imageio
from PIL import Image

filenames = ['file.1.jpg', 'file.2.jpg']
images = []

for f in filenames:
    img = Image.open(f).convert("RGB")
    img = img.resize((500, 500))   # 👈 force same size
    images.append(img)

imageio.mimsave('file.gif', images, duration=0.5)

print("GIF created successfully 🎉")

