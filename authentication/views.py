from django.http import HttpResponse


# Create your views here.
def test(request):
    print('heloo')
    var_q = request.GET.get('q')

    return HttpResponse('<h1> HELLO {}</h1>'.format(var_q,))


def test2(request):
    print('foo 2 was called')
    return HttpResponse('<h1> HELLO 2 </h1>')
