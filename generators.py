# Generators are giving iterable objects. Instead of returning values it yields the value and gives iterable objects

def generator(num):

    for i in range(1,num+1):
        yield i

fun_obj = generator(5)

print(fun_obj)

for i in fun_obj:
    print(i)