import ReadFile
import CreateFile

CreateFile.fileCreateIfNotExist()


def getHexOfColour(fileName,name):
	'''
	DOCSTRING : Getting the list of names from the file and
	striping it to get the hexa decimal

	INPUT : Name of file, name of colour

	OUTPUT: Hexadecimal code in the str format
	'''
	if(fileName == 'ColourMainList' or fileName == 'ColourSecondaryList' or fileName == 'ColourTertiaryList'):
		listOfNames = ReadFile.getListInFile(fileName)
	for names in listOfNames:
		if name in names:
			names = names.lstrip(name)
			names = names.lstrip(' : ')
			return names

def hexToRGB(Hex):
	'''
	DOCSTRING : Uses a math function to convert Hexadecimal as str to RGB in a tuple

	INPUT : Hexadecimal as str

	OUTPUT : tuple of RGB as int
	'''
	Hex = Hex.lstrip('#')
	num = len(Hex)
	return tuple(int(Hex[i:i+num//3], 16) for i in range(0, num, num//3))



	
