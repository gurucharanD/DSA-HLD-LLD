# 65. Valid Number
# examples: "005047e+6","5.047e+6""

# order for a valid number:
# can start with a plus or minus sign
# should be followed by a digit 
# if exponent occurs in between the string it should have a 
# + or - sign infront of it
# if there is an exponent sign in the string
# it should be followed by one more digits
# after the + or - sign
# dot can occur in the string only before the exponent
# any symbols other than the digits , + or - , e or E , .
# are considered as invalid symbols


class Solution:
    def isNumber(self, s: str) -> bool:
        
        seen_digit = seen_exponent = seen_dot = False
        
        for idx,val in enumerate(s):
            
            if val.isdigit():
                seen_digit = True
            elif val in ["+","-"]:
                if idx > 0 and ( s[idx-1] != 'e' or s[idx-1] != 'E'):
                    return False
            elif val in ["e","E"]:
                if seen_exponent or not seen_digit:
                    return False
                
                seen_exponent = True
                seen_digit = False
            elif val == ".":
                if seen_dot or seen_exponent:
                    return False
                
                seen_dot = True
            else:
                return False
            
        return seen_digit
                
            
            