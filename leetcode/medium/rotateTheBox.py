# for each row invoke the helper function
# loop form the end of the row
# if you find an empty space, insert into Q
# if you find an obstacle empty the Q
# if you find a stone, replace the last empty spot with stone 

class Solution(object):

    
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        def rotateRow(row):
            queue = []
            for index in range(len(row)-1,-1,-1):
                if row[index] == ".":
                    row[index] = "."
                    queue.append(index)
                elif row[index] == "*":
                    queue = []
                    row[index] = "*"
                else:
                    if len(queue) != 0:
                        emptySpot = queue.pop(0)
                        row[emptySpot] = "#"
                        row[index] = "."
                        queue.append(index)
                    else:
                        row[index] = "#"
                        
            return row
        
        return zip(*[rotateRow(row) for row in box][::-1])


    

            
        