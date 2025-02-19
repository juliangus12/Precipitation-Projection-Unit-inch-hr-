import xarray as xr
import os 
import warnings

def get_max_annual_temp(file_path, lat, lon):
    """
    Returns the annual maximum temperature for the closest location (NetCDF file)

    params:
        file_path (string): Path to the NetCDF file
        lat (float): Latitude of location
        lon (float): Longitude of location 

    returns:
        float: annual maximum temperature
    """

    ds = xr.open_dataset(file_path)
    
    return ds["Tmax"].sel(lat=lat, lon = lon, method= "nearest").max().values

def get_max_annual_precip(file_path, lat, lon):
    """
    Returns the annual maximum precipitation for the closest location (NetCDF file)

    params:
        file_path (string): Path to the NetCDF file
        lat (float): Latitude of location
        lon (float): Longitude of location 

    returns:
        float: annual maximum precipitation 
    """

    ds = xr.open_dataset(file_path)

    return ds["PRCP"].sel(lat= lat, lon = lon, method= "nearest").max().values

def AMS_Norfolk_precip(folder_path, lat, lon, output_path):
    """
    Generates a text file containing the annual maxium precipitation for all NetCDF files in the provided folder path

    params:
        folder_path (string): Path to the folder containing NetCDF files
        lat (float): Latitude of location 
        lon (float): Longitude of location 
        output_path (string): Path to save AMS_Norflok.txt 

    returns:
        None
    """
    results = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".nc"):
            file_path = os.path.join(folder_path, file_name)
            # this is for the last 4 characters of the name (the year)
            year = int(file_name.split(".")[-2])

            max_precip = get_max_annual_precip(file_path, lat, lon)
            results.append((year, max_precip))

    with open(output_path, "w") as f:
        f.write("year\tAMS\n") 
        for year, max_precip in sorted(results):
            f.write(f"{year}\t{max_precip:.5f}\n")

def AMS_Norfolk_temp(folder_path, lat, lon, output_path):
    """
    Generates a text file containing the annual maxium temperature for all NetCDF files in the provided folder path

    params:
        folder_path (string): Path to the folder containing NetCDF files
        lat (float): Latitude of location 
        lon (float): Longitude of location 
        output_path (string): Path to save AMS_Norflok_temp.txt

    returns:
        None
    """
    results = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".nc"):
            file_path = os.path.join(folder_path, file_name)
            # this is for the last 4 characters of the name (the year)
            year = int(file_name.split(".")[-2])

            max_temp = get_max_annual_temp(file_path, lat, lon)
            results.append((year, max_temp))

    with open(output_path, "w") as f:
        f.write("year\tAMS\n") 
        for year, max_temp in sorted(results):
            f.write(f"{year}\t{max_temp:.5f}\n")

# coordinates for Norfolk, VA
latitude = 36.857398
longitude = -76.297371

precip_data = "precip_data"
temp_data = "temp_data"

AMS_Norfolk_precip(precip_data, latitude, longitude, "AMS_Norfolk.txt")
AMS_Norfolk_temp(temp_data, latitude, longitude, "AMS_Norfolk_temp.txt")


        

