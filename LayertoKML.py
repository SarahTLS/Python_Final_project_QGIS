#converting the kml to shapefile

from qgis.core import QgsVectorFileWriter, QgsVectorLayer

data_source = r"C:/Users/Sarah/Desktop/MOF_Data_QGIS/Gas_Leaks_2018"
layer = QgsVectorLayer(data_source, "GasLeakas2018", "ogr")
output_layer = r"C:/Sarah/Desktop/MOF_Data_QGIS/KML"
QgsVectorFileWriter.writeAsVectorFormat(layer, output_layer, "utf-8", layer.crs(), "KML")

print ("Layer to KML Conversion Complete")
print (output_layer + " is now a .kml")
