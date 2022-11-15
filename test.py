# 2.	(2 points) Write Python function to print the count of all numbers from 1 to 100 that are divisible by 3 and 5. 
def fizbuz():
    count = 0
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(i)
            count+=1
        
    print("the count of all numbers from 1 to 100 that are divisible by 3 and 5 is {}".format(count))
    return count

fizbuz()
print("_____________________________")

# 3.	(5 points) Write Python code to print the number of unique words in a text file of your preference. 
from collections import Counter
def unique_words_counter():
    s = open('data.txt', 'r').read()
    s = s.split(" ")
    counter = Counter(s)
    
    uniqe_words = counter.keys()

    print("the number of unique words in the text file is {}".format(len(uniqe_words)))
    print(uniqe_words)
    return uniqe_words;

unique_words_counter()
print("_____________________________")


# 4.	(2 points) Write a function that takes 3 parameters of any data type of your choice. If all the parameters are of type integer, print the sum and return true.
#  Otherwise return false.

def func(a,b,c):
    if type(a) == type(b) == type(c) == int:
        print(a+b+c)
        return True
    else:
        return False

print(func(1,2,3))
print(func(1,'a',3.0))
