def caesarCipherEncryptor(string, key):
	ceaserCipher = ''
	
	if key > 26:
		key = key%26
	
	for character in string:
		assciOfChar = ord(character);
		assciOfChar += key
		
		if assciOfChar >= 123:
			assciOfChar = ( assciOfChar % 123 ) + 97
			
		print(assciOfChar)
		ceaserCipher = ceaserCipher + chr(assciOfChar)
		
		
	return ceaserCipher