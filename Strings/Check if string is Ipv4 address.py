'''
    Date: 15 Feb, 2024
    Name: Rishabh Mathur
'''

class Solution:
    def valid_part(self, part):
        n = len(part)

        # Check if string part has not more than 3 elements as,
        # given range of ipv4's one unit is betwen (0-255)
        if n>3:
            return False
        
        #checking for leading 0's.
        if n > 1 and part[0] == '0' and part != '0':
            return False
        
        # Check if all the elements in 3 length part are digits
        for i in range(n):
            if not part[i].isdigit():
                return False

        # Converting the string part into it's number
        # so as to check if it lies between 0 to 255
        num = int(part)

        # Check if it's between 0-255 and return False otherwise.
        return 0 <= num <=255

    def checkIP(self, ip_str):
        count = 0

        # Check if there are 3 dots present in the string.
        for i in range(len(ip_str)):
            if  ip_str[i] == '.':
                # Increase the count by 1 whenever a dot is encountered.
                count += 1

        # If 3 dots are not there then,
        # return FALSE as it's not a valid IPv4 address.
        if count != 3:
            return False
        
        # Split the string wrt to dots(.) to divide it into 4 different numbers
        parts = ip_str.split('.')

        # Perform checking operations to validate the 
        # digits in the address.
        for part in parts:
            if not self.valid_part(part):
                return False
            
        return True

if __name__  == "__main__":

    ip_str = "128.0.0.1"
    ob = Solution()

    print("Valid Ipv4 Address" if ob.checkIP(ip_str) else "Not Valid")