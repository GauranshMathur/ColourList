def addToTheColourList(Clist, name, hex):
	'''
	DOCSTRING : opens file to and adds the name and hex in a new line
	INPUT : Name of file, name of colour, hexadecimal code
	OUTPUT : If file name is incorrect print saying enter a valid name
	'''
	if(Clist == 'ColourMainList' or Clist == 'ColourSecondaryList' or Clist == 'ColourTertiaryList'):
		with open(Clist,mode='w') as cFile:
			cFile.write(f"\n{name} : {hex}")
		cFile.close()
	else:
		print("Enter a valid name of file")