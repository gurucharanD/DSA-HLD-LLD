# try all the different positions of period in the input string
# place the period at one position and check if this position is valid
# if it is valid, then decide the position of second period 
# and check if they are valid

def validIPAddresses(string):
    # Write your code here.
	output = []
	
    # we have min(len(string) is to avoid index going out of range
    
	for i in range(1,min(len(string),4)):
		partOne = string[:i]
		if not validateIp(partOne):
			continue
			
		for j in range(i+1,i+min(len(string)-i,4)):
			partTwo = string[i:j]
			if not validateIp(partTwo):
				continue

			for k in range(j+1,j+min(len(string)-j,4)):
				partThree = string[j:k]
				partFour = string[k:]
				if  validateIp(partThree) and  validateIp(partFour):
					output.append(partOne+"."+partTwo+"."+partThree+"."+partFour)

    return output


def validateIp(ip):
	integerIp = int(ip)
	if integerIp > 255:
		return False
	
	return len(ip) == len(str(integerIp))
	



