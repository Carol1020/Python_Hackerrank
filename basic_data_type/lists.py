'''
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
'''

if __name__ == '__main__':
    N = int(input())
    lst=[]
    
    for i in range(0,N):
        input_str=input()
        a=input_str.split()
        if a[0]=='insert':
            lst.insert(int(a[1]), int(a[2]))
        elif a[0]=='print':
            print(lst)
        elif a[0]=='remove':
            lst.remove(int(a[1]))
        elif a[0]=='append':
            lst.append(int(a[1]))
        elif a[0]=='sort':
            lst.sort()
        elif a[0]=='pop':
            lst.pop()
        elif a[0]=='reverse':
            lst.reverse()
