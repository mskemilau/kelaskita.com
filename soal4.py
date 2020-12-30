from django.http import HttpResponse
visitor = 0

def counter(request):
    global visitor
    visitor += 1
    return HttpResponse(f'Halaman ini sudah dikunjungi sebanyak {visitor} kali')