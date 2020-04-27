import os

from path import Path
from PIL import Image

WIDTH = 1000


def resize_image(im):
	w,h = im.size
	print(im.size)
	coef = w/WIDTH
	print(coef)
	print((WIDTH,round(h/coef)))
	return im.resize((WIDTH,round(h/coef)))

path = Path(os.getcwd()) / "images"

files = path.files()
to_resize = []
for file in files:
	name, ext = file.splitext()
	if not name.endswith("_s"):
		if name + "_s" + ext not in files:
			to_resize.append(file)

for file in to_resize:
	im = Image.open(file)
	if im.size[0] > 1100:
		print(f"Processing {file.name} ({im.size[0]}x{im.size[1]})")
		new_im = resize_image(im)
		name,ext = file.splitext()
		new_im.save(name + "_s" + ext)
	else:
		print(f"Skipping {file.name} (({im.size[0]}x{im.size[1]})")
		name,ext = file.splitext()
		file.copy(name + "_s" + ext)








