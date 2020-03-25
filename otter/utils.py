######################################
##### Utilities for Otter-Grader #####
######################################

import os
import sys
import pathlib
import pandas as pd


def block_print():
	"""
	Disables printing to stdout.
	"""
	sys.stdout = open(os.devnull, 'w')


def enable_print():
	"""
	Enables printing to stdout.
	"""
	try:
		sys.stdout.close()
	except:
		pass
	sys.stdout = sys.__stdout__


def list_files(path):
	"""Returns a list of all non-hidden files in a directory
	
	Args:
		path (str): Path to a directory
	
	Returns:
		list: List of filenames (str) in the given directory

	"""
	return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and file[0] != "."]


def merge_csv(dataframes):
	"""Merges dataframes returned by Docker containers
	
	Args:
		dataframes (list): List of Pandas dataframes (all should have same headers)
	
	Returns:
		pandas.core.frame.DataFrame: A merged dataframe resulting from 'stacking' all input df's

	"""
	final_dataframe = pd.concat(dataframes, axis=0, join='inner').sort_index()
	return final_dataframe
