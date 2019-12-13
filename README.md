# Update of the evapotranspiration dataset (HADES)

## Aim
Current evapotranspiration raster dataset from HADES exhibits too high or low values for a certain land cover. Therefore, there is a need for identifying inaccuracies in the evapotranspiration dataset.The aim of the scripted ArcGIS-Tool is:
If needed
 - to create an evapotranspiration raster, based on land cover, aspect, slope, and the original evapotranspiration values
 - to update the original evapotranspiration raster dataset


## Usage
The provided script is only suitable for the usage with ArcGIS. 
The projection can be individually chosen by the user in the tool-window.

If other input data is used, the following must be considered:
 - check the components of your land cover dataset. If necessary, adapt 
      - input parameter of tool (26-38)
      - projection part (54-66)
      - reclassifying part (104-154)
      
 - adapt the threshold the following way: 
      - take the value ranges of the old (o) and the new (n) evapotranspiration dataset
      - calculate the percentage: (n/o) * 100
      - take the value range of difference.tif (d) and substract the percentage share of extreme values: t(u) = d(max) - (d * (n/o)), t(l) = d(min) - (d * (n/o))
      - t(l) is your lower, t(u) is your upper threshold
      - insert the new thresholds in original line 210

## Package
The following data is supplied in this package:

### Data
- DEM
- evapotranspiration (HADES)
- individual land covers (CORINE)
    - Glacier
    - Water
    - Wetland
    - Rock
    - Loose Rock
    - Forest
    - Coniferous Forest
    - Deciduous Forest
    - Mixed Forest
    - Bush
    - Grass
    - Agriculture
    - Built Up Area

### Doc
- Scientific Report
- Maps
- Statistics
- Meta-Data

### Script_Tool
- Python Script
- ArcGIS-Toolbox




# Acknowledgement
This project was carried out within the framework of the “Geodataanalysis and Modelling” seminar at the University of Bern. Special thanks goes to our supervisors Dr. Andreas Zischg, Dr. Pascal Horton, and Jan Schwanbeck.
