from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def mathematics(request, a, symbol, b):
    if symbol == 'div':
        c = a / b
        symbol = '/'
    if symbol == '*':
        c = a * b
    if symbol == '+':
        c = a + b
    if symbol == '-':
        c = a - b
    else:
        c = 'wrong'
    return render(request, 'index.html', {'c': c, 'a': a, 'b': b, 'symbol': symbol})
