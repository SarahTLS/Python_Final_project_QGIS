# The purpose of this script, created by Sarah Lerman-Sinkoff, is to find the publicly reported gas leak closest to each massachuetts school, using QGIS
# the script performs the following operations

# 1. Converts gas leak data from a KML to a shapefile
# 2. Changes the projection of the gas leak data and schools data
# 3. Finds the gas leak closest to each school, using a spatial join
# 3. Adds each layer to the map
# 4. Exports an excel file with the data


# Import the modules we will useAdvancedEffects

from qgis.core import QgsVectorFileWriter, QgsVectorLayer

# Create a CRS object for the KML Data to use

QgsCoordinateReferenceSystem("EPSG:26986")

# Convert the downloaded KML gas leak data to a shapefile

from qgis.core import QgsVectorFileWriter, QgsVectorLayer  #import QPyGIS modules

dest_crs = QgsCoordinateReferenceSystem(26986) # create a variable with a coordinate reference system
vlayer = QgsVectorLayer(r"C:/Users/Sarah/Documents/Clark_Fall_2019/Programming_python/Final_project_data/GasLeaks2018.kml", "line", "ogr") # input KML file to be written as a shapfile
writer = QgsVectorFileWriter.writeAsVectorFormat(vlayer, r"C:/Users/Sarah/Documents/Clark_Fall_2019/Programming_python/Final_project_data/GasLeaks2018_shapefile.shp", "utf-8", dest_crs, "ESRI Shapefile") # output file to be written as shapefile

# project the gas leak data to massachusetts state plane

GasFilePath =  'C:/Users/Sarah/Documents/Clark_Fall_2019/Programming_python/Final_project_data/GasLeaks2018_shapefile.shp'
GasFilePath_split = GasFilePath.split('/G')
ProjectedGasFilePath = GasFilePath_split[0] + '/GasLeaks2018Projected.shp' # Using string editing to create a new filepath for the projected file
print (ProjectedGasFilePath) # check that string editing code worked

import processing # import the processing algorithm
processing.run("native:assignprojection", {'INPUT': GasFilePath,
'CRS':'epsg:3857','OUTPUT':ProjectedGasFilePath}) 

# project the schools data to massachusetts state plane

SchoolsFilePath = 'C:/Users/Sarah/Documents/Clark_Fall_2019/Programming_python/Final_project_data/AllSchools/SCHOOLS_PT.shp'
SchoolsFilePath_split = SchoolsFilePath.split('/A')
ProjectedSchoolsFilePath = SchoolsFilePath_split[0] + '/SchoolsProjected.shp' # Using string editing to create a new filepath for the projected file
print (ProjectedSchoolsFilePath) # check that string editing code worked
processing.run("native:assignprojection", {'INPUT': SchoolsFilePath,'CRS':'epsg:3857','OUTPUT':ProjectedSchoolsFilePath}) 

# Spatial join to figure out the gas leak closest to each school

ProjSchools_split = ProjectedSchoolsFilePath.split('/Sch')
ProjSchools_wLeaks = ProjSchools_split[0]+ '/SchoolswLeaks.shp' # make an output file path for the joined layer

processing.run("native:joinbynearest",
{'INPUT':ProjectedSchoolsFilePath,
'INPUT_2':ProjectedGasFilePath,
'FIELDS_TO_COPY':'Name',
'OUTPUT':ProjSchools_wLeaks})

# add the gas leak and schools point data to the map
gasleaklayer = QgsVectorLayer(ProjectedGasFilePath, "Gas_Leaks_2018_Projected", "ogr")  
QgsProject.instance().addMapLayer(gasleaklayer)

schoolslayer= QgsVectorLayer(ProjSchools_wLeaks, "MA_Schools_Projected_wLeaks", "ogr")
QgsProject.instance().addMapLayer(schoolslayer)

# Export table with the data

ProjSchools_wLeaks_split = ProjSchools_wLeaks.split('/Sch')
ProjSchools_wLeaks_CSV = ProjSchools_wLeaks_split[0] + '/SchoolswLeaksTable.CSV' # make an output file path for the joined layer
print(ProjSchools_wLeaks_CSV)

QgsVectorFileWriter.writeAsVectorFormat(schoolslayer, ProjSchools_wLeaks_CSV, "utf-8", dest_crs, "CSV", layerOptions = ['GEOMETRY=AS_XYZ'])

