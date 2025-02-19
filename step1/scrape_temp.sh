#!/bin/bash

# Ensure the target directory exists 
mkdir -p ./temp_data

# Download only temperature files from 1951-2018 into the folder 
for year in {1951..2018}; do
	wget -P ./temp_data https://cirrus.ucsd.edu/~pierce/nonsplit_precip/temp_and_wind/livneh_lusu_2020_temp_and_wind.2021-05-02.${year}.nc

done
