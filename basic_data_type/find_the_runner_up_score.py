"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])