#coding:utf-8

def maximum(n1, n2, n3):
    m = n1
    if n2 > m:
        m = n2
        if n3 > m:
            m = n3
    return m


print(maximum(20, 55, 13))