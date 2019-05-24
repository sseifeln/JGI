import sys
import pandas as pd
import numpy as np

def loadmsoaData(dirName='../Loneliness'):
	msoaData = pd.read_excel('%s/msoa_loneliness.xlsx'%(dirName), 'msoa_loneliness', index_col=None)
	msoaDataDict =  pd.read_excel('%s/msoa_loneliness.xlsx'%(dirName), 'Data Dictionary', index_col=None)
	return msoaData, msoaDataDict

def loadFinalData(dirName='../Loneliness'):
	finalData = pd.read_excel('%s/final_data.xlsx'%(dirName), 'Data', index_col=None)
	finalDataDict =  pd.read_excel('%s/final_data.xlsx'%(dirName), 'Data Dictionary', index_col=None)
	return finalData, finalDataDict

def loadDrugsList(dirName='../Loneliness'):
	drugsList = pd.read_csv('%s/drug_list.csv'%(dirName))
	return drugsList

def loadProccessedData(dirName='../Loneliness'):
	processedData = pd.read_csv('%s/processed_data.csv'%(dirName))
	# drop the un-named column
	processedData = processedData.drop(['Unnamed: 0'], axis=1)
	return processedData

def mergedDataStreams(final_data, proc_data):
	pCodeData= final_data.merge( proc_data , on=['PCT','pcstrip','SHA'])
	pCodeData.reset_index(drop=False, inplace=True)
	pCodeData = pCodeData[['PCT','pcstrip','SHA','Postcode']]
	mergedData= final_data.merge( pCodeData , on=['PCT','pcstrip','SHA'])
	return mergedData

