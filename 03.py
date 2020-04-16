from random import randint

A = ['Дима', 'Отис', 'Вася'] #kto
B = ['Машей', 'Наташей', 'Аней']#c kem
C = ['магазин', 'ресторан', 'аквапарк']#kyda

a = A[randint(0,len(A) - 1)]
b = B[randint(0,len(B) - 1)]
c = C[randint(0,len(C) - 1)]

pred = [
	lambda : '%s с %s пойдут в %s?' % (a, b, c),
	lambda : 'В %s пойдут %s с %s' % (c, a, b),
	lambda : '%s с %s ходили в %s?' % (a, b, c),
]

print (pred[randint(0,len(pred) - 1)]())

x = ['Da', 'Net']
print(x[randint(0,1)])