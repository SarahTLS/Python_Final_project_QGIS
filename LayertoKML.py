#Creating a layer from a KML

# Importing the appropriate packages
from qgis.core import QgsVectorFileWriter, QgsVectorLayer

# defining the inputs for the Write as Vector Format 
data_source = r"C:/Users/Sarah/Desktop/MOF_Data_QGIS/Gas_Leaks_2018" #file path for gas leaks shapefile
layer = QgsVectorLayer(data_source, "GasLeakas2018", "ogr")  # first parameter for write vector file
dest_crs = QgsCoordinateReferenceSystem(4326) # defining the Coordinate reference system for the destination file
output_layer = r"C:/Users/Sarah/Desktop/MOF_Data_QGIS/Gas_Leaks_2018/KML_Data/GasLeaks2018.kml" # defining the output file
QgsVectorFileWriter.writeAsVectorFormat(layer, output_layer, "utf-8", dest_crs, "KML") # writing the new vector file
print ("Layer to KML Conversion Complete")  # print that the thing worked
print (output_layer + " is now a .kml") # print where the file is located


