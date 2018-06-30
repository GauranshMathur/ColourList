def addToTheColourList(Clist, name, hex):
	'''
	'''
	if(Clist == 'ColourMainList' or Clist == 'ColourSecondaryList' or Clist == 'ColourTertiaryList'):
		with open(Clist,mode='w') as cFile:
			cFile.write(f"\n{name} : {hex}")
		cFile.close()
	else:
		print("Enter a valid name of file")