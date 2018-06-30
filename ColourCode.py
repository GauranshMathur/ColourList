def getCSSCodeForColourHex(Hex):
	'''
	DOCSTRING : returns the css code for background with Hex val
	INPUT : hex value
	OUTPUT : CSS code
	'''
	return ".mybgcolor {background-color:%s;}" %(Hex)

def getHTMLCodeForColourHex(Hex):
	'''
	DOCSTRING : returns the HTML code for background with Hex val
	INPUT : hex value
	OUTPUT : HTML code
	'''
	return "<div style=\"background-color:%s\">Div content here</div>" %(Hex)
