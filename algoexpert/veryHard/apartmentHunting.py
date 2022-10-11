
# build a 2D matrix of size r*b call it map
# loop throught the map and populate it with 
# 0 if the requirement is present in the block
# Infinity if the requirement is not present in the block

# loop through each requirement and find the 
# nearest block in which the requirement is present 
# by looping thorugh the requirement twice
# once from left to right and 
# again from right to left
# and populate the nearest location of the requirement

# [[1, 0, 0, 1, 2], [0, 1, 0, 0, 0], [4, 3, 2, 1, 0]]

# the array should look like this
# after the array is populated, at each block find 
# the max distance that needs to traveled
# return the block with min max distance

def apartmentHunting(blocks, reqs):
    # Write your code here.
    map = []
    minDistance = float("inf")
    blockToLive = 0
    
    for req in reqs:
        satisfy = []
        for block in blocks:
            if block[req]:
                satisfy.append(0)
            else:
                satisfy.append(float("inf"))
        map.append(satisfy)

    # print(map)
    for req in map:
      # loop from left to right
      reqFoundIndex = float("inf")
      for i in range(len(req)):
          if req[i] == 0:
              reqFoundIndex = i
          req[i] = abs(i-reqFoundIndex)
          
      # loop from right to left
      for i in range(len(req)-1,-1,-1):
          if req[i] == 0:
              reqFoundIndex = i
          req[i] = min(req[i],abs(i-reqFoundIndex))

      print(map)   
        
    for block in range(0,len(blocks)):
        currentBlock = []
        for req in map:
              currentBlock.append(req[block])
        print(currentBlock)
        if max(currentBlock) < minDistance:
            minDistance = max(currentBlock)
            blockToLive = block

    return blockToLive

        
    
    
     































    
    
