import sys
from astropy.io import fits
import numpy as np


img1 = sys.argv[1]
img2 = sys.argv[2]

image_list = [img1,img2]


image_concat = []
for image in image_list:
    image_concat.append(fits.getdata(image))

final_image = np.zeros(shape=image_concat[0].shape)
for image in image_concat:
    final_image += image

hdu = fits.PrimaryHDU(final_image)
hdu.writeto('pseudogreen.fits', clobber=True)


