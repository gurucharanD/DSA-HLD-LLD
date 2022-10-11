def moveElementToEnd(array, toMove):
	
	print(array)
    # Write your code here.
	pointer1 = 0
	pointer2 = len(array)-1
	
	while(pointer1<pointer2):
		if(array[pointer2]==toMove):
			pointer2-=1
		
		elif(array[pointer1]==toMove):
			temp = array[pointer1]
			array[pointer1]=array[pointer2]
			array[pointer2]=temp
			
			pointer1+=1
			pointer2-=1
		else:
			pointer1+=1
		
    return array
