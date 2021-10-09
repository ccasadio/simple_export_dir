import os
import sys
import inspect

def simple_export_dir():
	"""
	Creates a folder with the same name as the calling file 
	in the same location and returns the path to that folder
	"""
	frame     = inspect.stack()[1]
	module    = inspect.getmodule(frame[0])
	filename  = module.__file__
	file_path = os.path.realpath(filename)
	path      = os.path.splitext(file_path)[0]

	# Create a new directory if it does not already exist 
	os.makedirs(path, exist_ok=True)
	return path