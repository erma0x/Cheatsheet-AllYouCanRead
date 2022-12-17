import random as rnd
alpha = '1234556768790asdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
ps=''
for i in range(30):
	ps+=rnd.choice(alpha)
print(ps)
