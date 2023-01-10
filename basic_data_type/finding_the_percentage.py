'''
https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=internal-search&h_r=next-challenge&h_v=zen
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total_scores=sum(student_marks[query_name])
    count=len(student_marks[query_name])
    
    avg_score=format(total_scores/count, '0.2f')
    print(avg_score)