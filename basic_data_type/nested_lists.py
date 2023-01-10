'''
https://www.hackerrank.com/challenges/nested-list/problem?h_r=internal-search
'''
if __name__ == '__main__':
    
    stuscores=[]
    scores=[]
    names=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stuscores.append([name, score])
        scores.append(score)
    
    sortedscores=sorted(set(scores))
    
    for n, s in stuscores:
        if s==sortedscores[1]:
            names.append(n)
        
    sorted_names=sorted(names)
    for name in sorted_names:
        print(name)