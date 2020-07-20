# Projecting Data, Spatial Joins, and Table Exports with PyQGIS

### Follow along using the script for this tutorial -- the purpose of the script is to produce a spreadsheet identifying the gas leak closest to each school. Spreadsheets like these have been used by a local climate justice organization, Mothers Out Front, to prioritize their activism and better communicate with utilities. 
I knew the series of geoprocessing operations I needed this script to do at the outset. However, I had no idea how to script them in QGIS. Largely I solved this issue by navigating the documentation in QGIS and searching Stack Overflow. This tutorial will provide an overview of the different commands used to perform these operations.

A future direction for this code is to create a custom toolbox, similar to ones used in ArcMap, so that the input and output file paths and desired Coordinate Reference Systems are not hard-coded into the script, and so that users have a GUI to input their own files.

Note QGIS 3.8 Zanzibar is required to run this tutorial.

## Step 1. Download and Unzip the data
All the data for this lab are available here. 

## Step 2. Inspect the script
You’ll notice here that this script inputs a KML file of gas leaks and a shapefile of Massachusetts schools, and creates multiple new files. Find and identify the file names for each of the files that this script outputs including:
1.	A shapefile of gas leaks 
2.	A shapefile of gas leaks projected to a new Coordinate Reference System
3.	A shapefile of MA Schools projected to a new Coordinate Reference System
4.	A shapefile of schools joined to gas leaks
5.	An excel file with the distances between a school and the closet gas leak

## Step 3. Change file paths
You’ll see here that the file paths for both the input files (the gas leak KML, and the schools shapefiles) are hard-coded into the script. You’ll need to go ahead and change those to the ones used on your computer.

## Step 4.  See where different Coordinate Reference Systems are used in the code
There are multiple times in this script where you’ll see the text “ESPG:####”. This is a standard naming convention for Coordinate Reference Systems. Let’s explore each time where this occurs:
•	The first time is on Line 17. All KML files use a geographic coordinate system, WGS_1984, as their default. Here, we are asking for the output shapefile to be projected to the same coordinate system as the schools data, which is in Massachusetts State Plane.

•	The second time is on line 32, where we’re using ESPG 3857, which is the coordinate system used most commonly by google maps and Open Street Maps. It’s perhaps not the most appropriate for a distance calculation, but it’s what matches what many people are used to seeing on their phones (and, now we have a bit of code to experiment with for changing the output CRS).

## Step 5. Learn about Processing Algorithms in QPyGIS
Let’s stop and take a deeper dive into what’s happening in this code block containing line 32. In the line before (Line 31), you’ll see the command beginning with processing.run( . QGIS contains a vast library of algorithms used for geoprocessing. The code in line 31 calls a specific processing algorithm. Let’s take a minute and see what the different options are for processing in QGIS

•Open QGIS
•Open the python console using the   button in the upper toolbar
•QGIS has an internal script editor, open a new one using the   button
•Enter the following code, taken from the QGIS 3 documentation:

> import processing
> for alg in QgsApplication.processingRegistry().algorithms():
>        print(alg.id(), "->", alg.displayName())

This will output a long list of geoprocessing algorithms that QGIS can run (some of which are native to the application, some of which rely on GDAL and other libraries). Do you see any geoprocessing operations that you recognize? Pick one that you’d like to learn more about, and replace “native:buffer” into the following code:

> processing.algorithmHelp("native:buffer") 

A detailed description of the algorithm and the required inputs should pop up in the command window. Repeat this procedure for “native:joinbynearest”. Inspect lines 47-51 in the code and identify the inputs for this geoprocessing operation.

## Step 6. Learn about writing vector files in QGIS
Inspect the last line of the script (line 66). You’ll see here a command:

> QgsVectorFileWriter.writeAsVectorFormat(

Look familiar? This is a throwback to where we wrote the KML as a shapefile back on Line 21. You’ll notice however that the last parameter here says “CSV” instead of “ESRI Shapefile”. Let’s look through the documentation for this command and see what other formats QGIS can write to.
•	In the toolbar above the command window, click the help   button. 
•	Type in QgsVectorFileWriter.writeAsVectorFormat and look at the documentation page for this command
•	What other file types, besides KMLs, Shapefiles, and CSVs, can this command write to?
## Step 7. Back to the main event – running the code!

Download the complete script from github and open it up in the QGIS editor. Click the run   button. The gas leaks layer and the schools layer should pop up on the map.
Inspect the output code. This script used string editing to create new file paths for the multiple files produced here, and print statements within the code outputted the file paths for the final projected gas leaks and schools layer, as well as the table outputted after the join operation:
> C:/Users/Sarah/Documents/Clark_Fall_2019/Programming_python/Final_project_data/GasLeaks2018Projected.shp
> C:/Users/Sarah/Documents/Clark_Fall_2019/Programming_python/Final_project_data/SchoolsProjected.shp
> C:/Users/Sarah/Documents/Clark_Fall_2019/Programming_python/Final_project_data/SchoolswLeaksTable.CSV

•	Open up the spreadsheet at the file path listed above and locate the “distance” field. This give you the distance to the nearest gas leak in the units of the coordinate reference system chosen above!

## Step 8. Fiddling around on your own

A note that since the file paths are hard-coded into the script, you’ll need to delete these files on your computer and remove them from the map in QGIS before running the code again.

•	Experiment with changing the coordinate reference system for the gas leaks and schools layers. See how this changes the final distance output in the spreadsheet. You can find more ESPG codes at https://epsg.io/3857
•	Experiment with using KML data from previous years. Go to www.heetma.org and navigate to their gas leak maps. Download the Worcester data for previous years, and change the file paths in the code to output spreadsheets for past years.

