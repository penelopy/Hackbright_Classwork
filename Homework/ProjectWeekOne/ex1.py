"""Create 26 directories in the current directory, one for each letter of the alphabet:
    ./a/
Loop through all the files in the original_files directory, and organize each of those files into the directory that their name starts with."""

import os, sys


dir_list = ["a", "b", "c"]

for item in dir_list: 
	path = "/Users/penelopehill/Desktop/Main Files - PCH/HB classwork/ProjectWeekOne/files/item/"

	os.mkdir(path[, mode])

#make directory
os.mkdir(path[, mode])	

#Recursively moves a file or dir
shutil.move(src, dst)

