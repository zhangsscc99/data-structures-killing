class Empty(Exception):
    ''' Raise this class for exceptions '''
    pass

class ArrayStack:
    ''' Stack implemented with python list append/pop'''
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Empty()
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()
        return self.array.pop(-1)

    def __repr__(self):
            return str(self.array)


def SumSubarray(mylist):
    mod=10**9+7
    n=len(mylist)
    s1=ArrayStack()
    s2=ArrayStack()
    left=[0]*n
    right=[0]*n
    for i in range(n):
        
        while s1 and mylist[s1.top()]>=mylist[i]:
            s1.pop()
        if s1.is_empty():
            left[i]=i+1
        else:

            left[i]=i-s1.top()
        s1.push(i)
    mylist.reverse()
    
    for i in range(n):
        
        while s2 and mylist[s2.top()]>mylist[i]:
            s2.pop()
        if s2.is_empty():
            right[i]=i+1
        else:
            right[i]=i-s2.top()
        s2.push(i)
    right.reverse()
    mylist.reverse()
    


    return sum(a*l*r for a,l,r in zip(left,right,mylist))%mod

print(SumSubarray([3,1,2,4]))
