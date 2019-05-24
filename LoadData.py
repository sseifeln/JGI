import sys
import pandas as pd

def loadmsoaData(dirName=''):
	msoaData = pd.read_excel('%s/msoa_loneliness.xlsx'%(dirName), 'msoa_loneliness', index_col=None)
	msoaDataDict =  pd.read_excel('%s/msoa_loneliness.xlsx'%(dirName), 'Data Dictionary', index_col=None)
	return msoaData, msoaDataDict

def loadFinalData(dirName=''):
	finalData = pd.read_excel('%s/final_data.xlsx'%(dirName), 'Data', index_col=None)
	finalDataDict =  pd.read_excel('%s/final_data.xlsx'%(dirName), 'Data Dictionary', index_col=None)
	return finalData, finalDataDict

def loadDrugsList(dirName=''):
	drugsList = pd.read_csv('%s/drug_list.csv'%(dirName))
	return drugsList

def loadProccessedData(dirName=''):
	processedData = pd.read_csv('%s/processed_data.csv'%(dirName))
	# drop the un-named column
	processedData = processedData.drop(['Unnamed: 0'], axis=1)
	return processedData

def mergeDataSources(proc_data, codes):
	mergedData= proc_data.merge( codes , on=['PCT','pcstrip','SHA'])
	return mergedData