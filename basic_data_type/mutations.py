'''
https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
'''

def mutate_string(string, position, character):
    string_list=list(string)
    string_list[position]=character
    new_string=''.join(string_list)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)