'''
    Name: Rishabh Mathur
    Date: 12 JAN, 2024
'''
class RevFirKEleQue:
    def reverseKQ(self, q, k, n):
        x = 0
        y = k-1

        while(x != y):
            q[x], q[y] = q[y], q[x]
            x += 1
            y -= 1

        return q

if __name__ == "__main__":

    q = [1,2,3,4,5]
    k = 3
    n = len(q)

    ob = RevFirKEleQue()
    print(ob.reverseKQ(q, k, n))
