# generate lps array
# an array that consists of the lengths
# of the longest prefix and suffix ending
# at that index. This array tells us the index 
# to which we need to move, when there is a mismatch

def build_lps(needle):
    # string = "abcaby"
    j = 0
    lps = [0]*len(needle)

    for i in range(1,len(string)):
        # if there is a match
        if needle[i] == needle[j]:
            lps[i] = j+1
            i+=1
            j+=1
        else:
            if j == 0:
                # since the array is already intialised to zero
                # we just move to next index
                i+=1
            else:
                # move j to the index pointed by 
                # lps[j-1] and continue comparisons
                j = lps[j-1]

    print(lps)
    return lps

def hasSubString(needle:str,haystack:str) -> bool:

    lps = build_lps(needle)
    i = j = 0

    while (i < len(haystack))and (j<len(needle)):
        if haystack[i] == needle[j]:
            i+=1
            j+=1
        else:
            if j == 0:
                i+=1
            else:
                j = lps[j-1]
    

    if j == len(needle):
        return True
    
    return False


    