class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mylist = list(s)
        mylist2 = list(t)

        mylist.sort()
        mylist2.sort()

        s2 = ''.join(mylist)
        t2 = ''.join(mylist2)

        if mylist == mylist2:
            return True
        else:
            return False
        