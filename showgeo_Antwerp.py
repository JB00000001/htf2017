from numpy import *
from matplotlib.pyplot import *
from matplotlib.image import *
#import matplotlib.pylab as plot
import osgeo.gdal as gdal
from osgeo.gdalconst import *
def read_geotiff(filename, band_id=1):
   # Open the file
   dataset = gdal.Open( filename, GA_ReadOnly )
   if dataset is None:
      print 'Error: GDAL cannot open the file correct.'
      return None
   #fi
   # Fetch a band
   if (band_id < 1 | band_id > dataset.RasterCount):
      print 'Error: The specified band number is out of the range.'
      return None
   # fi
   band = dataset.GetRasterBand(band_id)
   # Get the Raster Data
   data = band.ReadAsArray(0, 0, dataset.RasterXSize, dataset.RasterYSize)
   # Close the file
   dataset = None  # the file will be closed when the dataset object is destructed
   return data
# end_def
#---------------------------------------------------------------
if __name__ == "__main__":
   resample_int = 4           # parameter for resampling the data because they are too large
   filename = './data/L5198024_02420100906_B10.TIF'  # band 1 for TM and ETM+
   data_blue = read_geotiff(filename)
   data_blue = data_blue[::resample_int, ::resample_int]
   filename = './data/L5198024_02420100906_B20.TIF'  # band 2
   data_green = read_geotiff(filename)
   data_green = data_green[::resample_int, ::resample_int]
   filename = './data/L5198024_02420100906_B30.TIF'  # band 3
   data_red = read_geotiff(filename)
   data_red = data_red[::resample_int, ::resample_int]
   (N, M) = data_blue.shape
   data_rgb = zeros((N, M, 3), 'u1')
   data_rgb[:, :, 0] = data_red.astype('u1')
   data_rgb[:, :, 1] = data_green.astype('u1')
   data_rgb[:, :, 2] = data_blue.astype('u1')
   imshow(data_rgb,)
   show()      # Does nothing for non-interactive backends
   savefig('test_landsat_truecolor.png', dpi=100)