def fileCreateIfNotExist():
	'''
	DOCSTRING : Checks if the files exist and if are empty or not.
	INPUT : 
	OUTPUT : 
	'''
		with open('ColourMainList',mode='w+') as cFile:
			cFile.seek(0) 
			first_char = cFile.read(1)  
			if not first_char:
				addValToMainList()
		cFile.close()

		with open('ColourSecondaryList',mode='w+') as cFile:
			cFile.seek(0) 
			first_char = cFile.read(1)  
			if not first_char:
				addValToSecondaryList()
		cFile.close()

		with open('ColourTertiaryList',mode='w+') as cFile:
			cFile.seek(0) 
			first_char = cFile.read(1)  
			if not first_char:
				addValToTertiaryList()
		cFile.close()

         
def addValToMainList():
	'''
	DOCSTRING : Writes values to the file
	INPUT : 
	OUTPUT : 
	'''
	with open('ColourMainList',mode='w') as cFile:
		cFile.write("Red : #ff0000\nOrange : #ffa500\nYellow : #ffff00\n"
		"Green : #008000\nBlue : #0000ff\nIndigo : #4b0082\nViolet : #ee82ee")
	cFile.close()

def addValToSecondaryList():
	'''
	DOCSTRING : Writes values to the file
	INPUT : 
	OUTPUT : 
	'''
	with open('ColourSecondaryList',mode='w') as cFile:
		cFile.write("Purple : #800080\nMagenta : #ff00ff\nCyan : #00ffff\n"
		"White : #ffffff\nBlack : #000000\nGrey : #808080\nPink : #ffc0cb")
	cFile.close()

def addValToTertiaryList():
	'''
	DOCSTRING : Writes values to the file
	INPUT : 
	OUTPUT : 
	'''
	with open('ColourTertiaryList',mode='w') as cFile:
		cFile.write("Amber : #ffbf00\nVermilion : #e34234\nTeal : #008080\n"
		"Chartreuse : #7fff00\nScarlet : #ff2400\nAubergine : #614051\nTurquoise : #40e0d0")
	cFile.close()