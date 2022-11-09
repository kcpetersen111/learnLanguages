import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image

start_time = time.time()

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
name = "Snogaloren"
batch_size = 3

images = model.text_to_image(name, batch_size)

for i in range(len(images)):
    Image.fromarray(images[i]).save("%s%s.png" % (name, i+1))

print("It took : %s seconds to run"% (time.time() - start_time))
