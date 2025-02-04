table_str = list()

rf = 3 #rounding factor

def f(x):
    return 2 + 2*x - x**2 #define function here f: R -> R

#a, b from integral
a = 0 
b = 3
n = 20
dx = (b - a)/n

def calculate_trapezium_area(x, f):
    
    return dx * f(x + dx/2)

def calculate_integral(f):
    total = 0
    for i in range(n):
        x = a + i*dx
        trapezium_area = calculate_trapezium_area(x, f)
        total += trapezium_area
        data = {'n': i, 'x': x,'x + dx/2':x + dx/2, 'f(x + dx/2)': f(x + dx/2), 'dx*f(x + dx/2)': dx*f(x + dx/2)}
        table_str.append(data)
    return total

print('_'*105)

print(f'|{'n':20}|{'x':20}|{'x + dx/2':20}|{'f(x + dx/2)':20}|{'dx*f(x + dx/2)':20}|')

print('-'*105)

result = calculate_integral(f)

for r in table_str:

    print(f'|{r['n']:<20,.{rf}f}|{r['x']:<20,.{rf}f}|{r['x + dx/2']:<20,.{rf}f}|{r['f(x + dx/2)']:<20,.{rf}f}|{r['dx*f(x + dx/2)']:<20,.{rf}f}|')


print('-'*105)


print(f'Σ = {result:.{rf}f}' )