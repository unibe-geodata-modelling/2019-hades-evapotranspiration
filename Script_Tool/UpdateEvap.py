

#Import system modules
import arcpy, os
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
if arcpy.CheckExtension('Spatial')== 'Available':
	arcpy.CheckExtension('Spatial')
else:
	print('No spatial analyst license available')
    

#Set environment settings
outWorkspace = arcpy.GetParameterAsText (0)
env.workspace = outWorkspace


#Read parameter values
inProjection = arcpy.GetParameterAsText (1)
inDEM = arcpy.GetParameterAsText (2)
inEvapotransp = arcpy.GetParameterAsText (3)

#Read land cover data
inGlacier = arcpy.GetParameterAsText (4)
inWater = arcpy.GetParameterAsText (5)
inWetlands = arcpy.GetParameterAsText (6)
inRock = arcpy.GetParameterAsText (7)
inForest = arcpy.GetParameterAsText (8)
inBush = arcpy.GetParameterAsText (9)
inGrass = arcpy.GetParameterAsText (10)
inAgricult = arcpy.GetParameterAsText (11)
inBuiltUp = arcpy.GetParameterAsText (12)
inLooseRock = arcpy.GetParameterAsText (13)
inConiferForest = arcpy.GetParameterAsText (14)
inDecidForest = arcpy.GetParameterAsText (15)
inMixedForest = arcpy.GetParameterAsText (16)


#Create folder for results
out_folder_path = outWorkspace
out_name = "Results"

arcpy.CreateFolder_management(out_folder_path, out_name)
Results = str(arcpy.CreateFolder_management(out_folder_path, out_name))

#Project raster files into a specific projection
#Project DEM
arcpy.ProjectRaster_management(inDEM, "DEM.tif", inProjection)
arcpy.ProjectRaster_management(inEvapotransp, "evapotransp.tif", inProjection)

#Project Land cover
arcpy.ProjectRaster_management (inGlacier, "Glacier.tif", inProjection)
arcpy.ProjectRaster_management (inWater, "Water.tif", inProjection)
arcpy.ProjectRaster_management (inWetlands, "Wetland.tif", inProjection)
arcpy.ProjectRaster_management (inRock, "Rock.tif", inProjection)
arcpy.ProjectRaster_management (inForest, "Forest.tif", inProjection)
arcpy.ProjectRaster_management (inBush, "Bush.tif", inProjection)
arcpy.ProjectRaster_management (inGrass, "Grass.tif", inProjection)
arcpy.ProjectRaster_management (inAgricult, "Agriculture.tif", inProjection)
arcpy.ProjectRaster_management (inBuiltUp, "BuiltUp.tif", inProjection)
arcpy.ProjectRaster_management (inLooseRock, "LooseRock.tif", inProjection)
arcpy.ProjectRaster_management (inConiferForest, "ConiferForest.tif", inProjection)
arcpy.ProjectRaster_management (inDecidForest, "DecidForest.tif", inProjection)
arcpy.ProjectRaster_management (inMixedForest, "MixedForest.tif", inProjection)


#Create DEM derivates
#Slope
##Set local variables
outMeasurement = 'DEGREE'
zFactor = 1

##Execute Slope
outSlope = Slope("DEM.tif", outMeasurement, zFactor)

##Save the output
outSlope.save(os.path.join(outWorkspace, "Slope.tif"))

#Aspect
##no other local variables needed
##Execute aspect
outAspect = Aspect("DEM.tif")
outAspect.save(os.path.join(outWorkspace, "Aspect.tif"))


#Reclassify DEM derivates
#Build classes for slope values
myRemapRange_Slope= RemapRange([[0, 2, 1], [2,8,2], [8, 16, 3], [16, 45, 4],[45, 90, 5]])
outReclassRRsl = Reclassify("Slope.tif", "VALUE", myRemapRange_Slope)
outReclassRRsl.save(os.path.join(outWorkspace, "rclassremransl.tif"))

#Build classes for aspect values
myRemapRange_Aspect= RemapRange([[315, 360, 1], [0,45,1], [45, 135, 2], [135, 225, 3], [225, 315, 4], [-1,-1,5]])
outReclassRRas = Reclassify("Aspect.tif", "VALUE", myRemapRange_Aspect)
outReclassRRas.save(os.path.join(outWorkspace, "rclassremranas.tif"))



#Create a combined land cover raster file
##Reclassify individual land covers

myRemapRange_Glacier = RemapRange([[0,0,-9999],[100,100,1]])
outReclassRRgl = Reclassify('Glacier.tif', 'VALUE', myRemapRange_Glacier)
outReclassRRgl.save(os.path.join(outWorkspace, 'reclGlacier.tif'))

myRemapRange_Water= RemapRange([[0,0,-9999],[100,100,2]])
outReclassRRwtr = Reclassify('Water.tif', 'VALUE', myRemapRange_Water)
outReclassRRwtr.save(os.path.join(outWorkspace, 'reclWater.tif'))

myRemapRange_Wetlands= RemapRange([[0,0,-9999],[100,100,2]])
outReclassRRwtl = Reclassify('Wetland.tif', 'VALUE', myRemapRange_Wetlands)
outReclassRRwtl.save(os.path.join(outWorkspace, 'reclWetland.tif'))

myRemapRange_Rock= RemapRange([[0,0,-9999],[100,100,3]])
outReclassRRroc = Reclassify('Rock.tif', 'VALUE', myRemapRange_Rock)
outReclassRRroc.save(os.path.join(outWorkspace, 'reclRock.tif'))

myRemapRange_Forest= RemapRange([[0,0,-9999],[100,100,4]])
outReclassRRfor = Reclassify('Forest.tif', 'VALUE', myRemapRange_Forest)
outReclassRRfor.save(os.path.join(outWorkspace, 'reclForest.tif'))

myRemapRange_Bush= RemapRange([[0,0,-9999],[100,100,5]])
outReclassRRbsh = Reclassify('Bush.tif', 'VALUE', myRemapRange_Bush)
outReclassRRbsh.save(os.path.join(outWorkspace, 'reclBush.tif'))

myRemapRange_Grass= RemapRange([[0,0,-9999],[100,100,6]])
outReclassRRgr = Reclassify('Grass.tif', 'VALUE', myRemapRange_Grass)
outReclassRRgr.save(os.path.join(outWorkspace, 'reclGrass.tif'))

myRemapRange_Agricult= RemapRange([[0,0,-9999],[100,100,7]])
outReclassRRagr = Reclassify('Agriculture.tif', 'VALUE', myRemapRange_Agricult)
outReclassRRagr.save(os.path.join(outWorkspace, 'reclAgricult.tif'))

myRemapRange_BuiltUp= RemapRange([[0,0,-9999],[100,100,8]])
outReclassRRbu = Reclassify('BuiltUp.tif', 'VALUE', myRemapRange_BuiltUp)
outReclassRRbu.save(os.path.join(outWorkspace, 'reclBuiltUp.tif'))

myRemapRange_LooseRock= RemapRange([[0,0,-9999],[100,100,3]])
outReclassRRlr = Reclassify('LooseRock.tif', 'VALUE', myRemapRange_LooseRock)
outReclassRRlr.save(os.path.join(outWorkspace, 'reclLooseRock.tif'))

myRemapRange_ConiferFor= RemapRange([[0,0,-9999],[100,100,4]])
outReclassRRcf = Reclassify('ConiferForest.tif', 'VALUE', myRemapRange_ConiferFor)
outReclassRRcf.save(os.path.join(outWorkspace, 'reclConiferFor.tif'))

myRemapRange_DecidFor= RemapRange([[0,0,-9999],[100,100,4]])
outReclassRRdf = Reclassify('DecidForest.tif', 'VALUE', myRemapRange_DecidFor)
outReclassRRdf.save(os.path.join(outWorkspace, 'reclDecidFor.tif'))

myRemapRange_MixedFor= RemapRange([[0,0,-9999],[100,100,4]])
outReclassRRmf = Reclassify('MixedForest.tif', 'VALUE', myRemapRange_MixedFor)
outReclassRRmf.save(os.path.join(outWorkspace, 'reclMixedFor.tif'))

##Make a list with all the reclassified rasters
recllist = arcpy.ListRasters("recl*", "TIF")

##Process the list
for i in recllist:
	arcpy.gp.ExtractByAttributes_sa(i, '"Value" >0', (os.path.join(outWorkspace, "extr"+i[4:])))
	

##List extracted datasets
Rasters = arcpy.ListRasters("extr*", "TIF")
extrlist = ";".join(Rasters)

#Combine Rasters
arcpy.MosaicToNewRaster_management(extrlist, outWorkspace, "LandCover.tif", "", "16_BIT_SIGNED","", "1","LAST","FIRST")


##Build attribute table for single band raster dataset
###Overwrite the existing attribute table file
arcpy.BuildRasterAttributeTable_management("LandCover.tif", "Overwrite")


#Create a combined characteristics-raster
arcpy.gp.RasterCalculator_sa(""""LandCover.tif" + ("rclassremransl.tif" * 10) + ("rclassremranas.tif" * 100)""", (os.path.join(outWorkspace, "preCharacteristics.tif")))

#Extract errors
arcpy.gp.ExtractByAttributes_sa("preCharacteristics.tif", '"Value" >100', "characteristics.tif")

#Create an attribute table
arcpy.BuildRasterAttributeTable_management("characteristics.tif", "Overwrite")


#Create a Evapotranspiration raster, based on characteristics and the median of the old Evapotranspiration dataset (resolution 25m)
##Prepare Evapotranspiration raster for the analysis, as it has to be integer
###Round and change to integer
inRound = os.path.join(outWorkspace, 'evapotransp.tif')
outInt = Int(inRound ) #only deletes the decimals and changes raster setting to integer
outInt.save("intevap.tif")

arcpy.Resample_management("intevap.tif", "resamplevap25.tif", "25")

##Zonal Statistics
outZonalStats = ZonalStatistics("characteristics.tif", "Value", "resamplevap25.tif", "MEDIAN", "DATA")
outZonalStats.save(os.path.join(Results,"evapmedian25.tif"))

#Prepare rasters for the update
##Resample for comparing (choose the lower resolution, in this case its the evapotranspiration (r=1000)
arcpy.Resample_management(os.path.join(Results,"evapmedian25.tif"), "resevapmedian1000.tif", "1000")


#Compare the two rasters
arcpy.gp.RasterCalculator_sa('"resevapmedian1000.tif" - "intevap.tif"', "difference.tif")

#Build classes for values extending the threshold
#Build classes for slope values
myRemapRange_Diff= RemapRange([[-654, -366, 1], [-365,435,0], [436, 778, 1]]) #threshold is defined as a 44% quantile, since the difference median - old evapotranspiration value range expands for 44%
outReclassRRdiff = Reclassify("difference.tif", "VALUE", myRemapRange_Diff)
outReclassRRdiff.save(os.path.join(Results, 'errors.tif'))


errors = os.path.join(Results, 'errors.tif')

outCon = Con(errors, 'resevapmedian1000.tif', 'intevap.tif','VALUE =1')
outCon.save(os.path.join(Results, 'updateevap.tif'))
