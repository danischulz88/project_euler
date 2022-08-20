from math import floor

n=1000
s3=0
for i in range(1, floor((n-1)/3)+1):
    s3=s3+3*i

s5=0
for i in range(1, floor((n-1)/5)+1):
    s5=s5+5*i

s15=0
for i in range (1, floor((n-1)/15)+1):
    s15=s15+15*i

soma=s3+s5-s15
print("soma = {}".format(soma))