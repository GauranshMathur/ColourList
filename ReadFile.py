def getListInFile(fileName):
	'''
	DOCSTRING : Gets and reads a file in args

	INPUT : name of file to open

	OUTPUT : return list of colours 
	'''
	with open(fileName, mode='r') as cFile:
		listOfColours = cFile.readlines()
		return listOfColours
	cFile.close()