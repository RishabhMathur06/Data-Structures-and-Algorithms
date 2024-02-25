
def isKPalRec(str1, str2, m, n):

	if not m: return n

	if not n: return m

	if str1[m-1] == str2[n-1]:
		return isKPalRec(str1, str2, m-1, n-1)

	res = 1 + min(isKPalRec(str1, str2, m-1, n), 
				isKPalRec(str1, str2, m, n-1))
	
	return res

def isKPal(string, k):
	revStr = string[::-1]
	l = len(string)
	
	x = isKPalRec(string, revStr, l, l)
	print(x)
	
	return (x <= k * 2)


# Driver program
string = "acdcb"
k = 2

print("Yes" if isKPal(string, k) else "No")
