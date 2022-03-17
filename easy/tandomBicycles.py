from tokenize import group
from turtle import speed


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	
    # Write your code here.
	totalSpeed = 0;
	redShirtSpeeds.sort();

	if fastest == True:
		blueShirtSpeeds.sort(reverse = True);
	else:
		blueShirtSpeeds.sort();

	
	for i in range(len(redShirtSpeeds)):
		totalSpeed+= max(redShirtSpeeds[i],blueShirtSpeeds[i]);


	
    return totalSpeed;



# if you want to find the maximum possible total speed
# you need to pair the slowest rider in one group with fastest rider in another group
# which when taken a maximum returns the fastest rider

# to find the slowest possible total speed
# pair slowese with the slowest and fastest with the fastest
# when taken a max of the two, one player among the two with max speed gets rejected
# and results in decreasing the speed