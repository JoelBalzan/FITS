import sys
from astropy.io import fits

### IMPORT AND OPEN IMAGE ###
img = sys.argv[1] #image to remove extra dimensions from
hdulist = fits.open(img)
hdu = hdulist[0]

### REMOVE EXTRA DIMENSIONS ###
print(hdu.data.shape)
hdu.data = hdu.data[:,:]
print(hdu.data.shape)

### REMOVE HEADER DATA ###
#hdu.header.remove('CRPIX3')
#hdu.header.remove('CDELT3')
#hdu.header.remove('CRVAL3')
#hdu.header.remove('CTYPE3')
#hdu.header.remove('CRPIX4')
#hdu.header.remove('CDELT4')
#hdu.header.remove('CRVAL4')
#hdu.header.remove('CTYPE4')
hdu.header.remove('PC03_01')
hdu.header.remove('PC04_01')
hdu.header.remove('PC03_02')
hdu.header.remove('PC04_02')
hdu.header.remove('PC03_03')
hdu.header.remove('PC04_03')
hdu.header.remove('PC03_04')
hdu.header.remove('PC04_04')
hdu.header.remove('LONPOLE')
hdu.header.remove('LATPOLE')
hdu.header.remove('PC01_01')
hdu.header.remove('PC02_01')
hdu.header.remove('PC01_02')
hdu.header.remove('PC02_02')
hdu.header.remove('PC01_03')
hdu.header.remove('PC02_03')
hdu.header.remove('PC01_04')
hdu.header.remove('PC02_04')
hdu.header.remove('PV2_1'  )
hdu.header.remove('PV2_2'  )
hdu.header.remove('DATE'   )
hdu.header.remove('TIMESYS')
hdu.header.remove('ORIGIN' )
hdu.header.remove('BMAJ'   )
hdu.header.remove('BMIN'   )
hdu.header.remove('BPA'    )
hdu.header.remove('BTYPE'  )
hdu.header.remove('TELESCOP')
hdu.header.remove('PROJECT')
hdu.header.remove('SBID'   )
hdu.header.remove('DATE-OBS')
hdu.header.remove('DURATION')
hdu.header.remove('DATAMIN')
hdu.header.remove('DATAMAX')
hdu.header.remove('HISTORY')

### SAVE IMAGE ###
hdu.writeto('ASKAP_888MHZ.fits')
