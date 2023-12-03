"""
タロウくんは一を教えると十を知る、とても優秀なロボットです。
タロウくんに文字列を教えると、その部分文字列を全て単語として学習します。
タロウ君に文字列Sを教えたときに学習する単語の種類数を求めてください。
ただし、Sの部分文字列とは、Sから0文字以上の文字を取り除き、元の順番で連結した文字列を指します。
空文字列は部分文字列には含みません。
"""


import sys

def solve(S):
    a = []
    n = len(S)
    if n == 2:
        return [S]
    else:
        for i in range(n):
            if S[:i]+S[i+1:] not in a:
                a += solve(S[:i]+S[i+1:]) + [S[:i]+S[i+1:]]       
        return a

def main(S):
    n = len(set(S[0]))
    if n == 1:
        print(len(S[0]))
    else:
        a = solve(S[0])
        a.append(S[0])
        a = list(set(a))
        print(len(a)+n)  

if __name__ == '__main__':
    S = []
    for l in sys.stdin:
        S.append(l.rstrip('\r\n'))
    main(S)