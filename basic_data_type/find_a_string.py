'''
https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

def count_substring(string, sub_string):
    count=0
    
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)