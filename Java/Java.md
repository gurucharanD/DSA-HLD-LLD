Lang is the default package that is imported in java
System class is present in Lang class

if we want to use anything from class without creating an object, we need to use static
the name of class file will be same as Class name
if the class is public, then the name of the class should be same as the file name

Read Data from standard Input:
use scanner class present in util package

import java.util.*
Scanner sc = new Scanner(System.in);
use methods on scanner object

sc.nextInt
sc.nextFloat
sc.nextDouble
sc.nextLine
____________________________
Primitive Data Types: means core part type of a compiler
    Integral: (They take Integer literal)
        byte - 1byte - -128 to 127
        short - 2bytes - 
        int - 4bytes - 
    Floating point: 
        long - 8bytes - 
        float - 4bytes - single precision
        double - 8bytes - double precision
    char - 2bytes
    boolean - true/false

For every data type in Java there is a built in class available called Wrapper classes
Primitive data types are not classes, we have wrapper classes that contain information about range, size etc of the data type.
Example : Integer, Float, Character, Boolean, Byte
Example : Integer.MIN_VALUE, Integer.MAX_VALUE, Integer.BYTES etc
____________________________
when a varibale is created, the memory will be allocated during the run time.

Literals are constant values that are used in a programm. Literals also have their data types
5 and 7 are Integer Literals. 
153.75 any value with Decimal is a Double literal.
2.5F becomes a Float literal 
"A" is a Character literal
"Java" is a String literal

Integer literals can be represented in Decimal, Binary, Octal, Hexadecimal values
One bit (most significant bit) is reserved to represent a positive or negative number
0 means positive
1 means negative
negative numbers are represented in 2's compliment

For float the decimal is not stored in the memory, the deciaml point will be floated
either towards left or right by multiplying the number with 10
example: 163.52 = 16352*(10^-2) =  1635E-2 is saved in memory

Characters are stored as numeric code called as ASCII codes.
There are codes for all spoken languages called as UNICODE.
A = 65 Z = 90
a = 97 z = 122
Java takes 2 bytes to represent unicode in the memory
____________________________
Java is a hybrid language it is both compiled and interpreted
Java code is compiled to class file
and then the compile class file is interpreted by JVM

____________________________

JVM architecture:

    Class loader will load the class file into the main memory.
    and it also brings the classes that are needed into the memory
____________________________







