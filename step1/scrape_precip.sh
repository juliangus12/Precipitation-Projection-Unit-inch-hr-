#!/bin/bash

# Ensure the target directory exists
mkdir -p ./precip_data

# Download only precipitation files from 1951-2018 into the folder
for year in {1951..2018}; do 
	wget -P ./precip_data https://cirrus.ucsd.edu/~pierce/nonsplit_precip/precip/livneh_unsplit_precip.2021-05-02.${year}.nc
	
done 
