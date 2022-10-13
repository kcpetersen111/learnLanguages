import time
import keras_cv
from tensorflow import keras 
import matplotlib.pyplot as plt
from PIL import Image

# fle = open("moby.txt")
# st = fle.read()
# fle.close()
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
name = "Snogaloren"

images = model.text_to_image(name, batch_size=3)

for i in range(len(images)):
    Image.fromarray(images[i]).save("%s%s.png" % (name, i+1))
# def plot_images(images):
#     plt.figure(figsize=(20, 20))
#     for i in range(len(images)):
#         ax = plt.subplot(1, len(images), i+1)
#         plt.imshow(images[i])
#         plt.axis("off")


# plot_images(images)
