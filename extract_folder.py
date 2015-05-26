# -*- coding:utf-8 -*-
__version__ = 1.0
__author__ = 'Mohamed Safwan'
'''Extract folder name from source directory path'''

def extract(source_dir):
	i=-1
	c=0
	end=len(source_dir)
	if(source_dir[-1]=="\\"):
		c=1
		i=-2
		end=-1
	while(source_dir[i]!='\\'):
		i=i-1;
	start=i+1
	
	return source_dir[start:end]
	

