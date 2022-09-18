# Given two strings, return the list of Strings that are unique to each string.
# String 1 - “My Dog chased My cat!”
# String 2 - "your dog Chased your cat."
# return - "my", "your"

str1 = "My Dog chased My cat!"
str2 = "your dog Chased your cat."
list1 = str1.split(" ") 
list2 = str2.split(" ") 
occurence = {}
res = set()

for word in list1:
    originalWord = "".join([c if c.isalnum() else '' for c in list(word)])
    word = originalWord.lower()
    if word not in occurence:
        occurence[word] = [False,originalWord]
 
for word in list2:
    originalWord = "".join([c if c.isalnum() else '' for c in list(word)])
    word = originalWord.lower()
    if word in occurence:
        occurence[word][0] = True
    else:
        res.add(originalWord)
        
for word in occurence:
    if not occurence[word][0]:
        res.add(occurence[word][1])
    
print(list(res))

# time = O(3n) => O(n*n)
# space = O(n) => for storing the words in the first string in hashmap
    
    
        


