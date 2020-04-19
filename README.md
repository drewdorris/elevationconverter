# elevationconverter

This is a Python script which was going to be used for collecting USGS elevation IMG sources, converting to a Minecraft 0-256 scale, and storing in a yaml. I stopped working on this after finding out about terra121, though this could still be used for compiling more accurate 1:1 or 1:10 data which the terra121 data sources lack.

### How to use:

1. Install GDAL

2. Download and decompile IMG files from these sources:

Compact direct links:
* 1m: https://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/1m/IMG/
* 1/9 arc second (~3m): http://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/19/IMG/
* 1/3 arc second (~10m): http://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/13/IMG/
* 1 arc second (~30m): http://prd-tnm.s3.amazonaws.com/index.html?prefix=StagedProducts/Elevation/1/IMG/

Map directory for finding specific locations:
* 1m: https://catalog.data.gov/dataset?collection_package_id=988723e5-b093-4520-9ea3-cbfea7769bae
* 1/9 arc second (~3m): https://catalog.data.gov/dataset?collection_package_id=14fa2d80-b6e6-4cda-a7f3-95d740b716e1
* I couldn't find 1/3
* 1 arc second (~30m): https://catalog.data.gov/dataset?collection_package_id=4c7396d3-21c7-4cc2-8c34-e42c4cc50ec3

Also there's Alaska data that's 5 meters but I haven't tested that

3. Make a new folder, drag everything (including yml) in it, run the script

4. Drag and drop IMG files into the folder

5. Do this until you have every single location known on the planet ever compiled
