'''
https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
'''

def split_and_join(line):
    # write your code here
    # line_list=line.split(' ')
    # a='-'.join(line_list)
    # return a

    return line.replace(' ','-')

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)