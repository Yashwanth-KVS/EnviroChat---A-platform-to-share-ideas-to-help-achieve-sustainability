from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Member


# Create your views here.

def home(request):
    search_list(request)
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def search_list(request):
    return render(request, 'search.html')


def search_name(request):
    query = request.GET.get('search', '')
    objs = Member.objects.filter(username__startswith=query)
    payload = []
    for obj in objs:
        payload.append({
            'id': obj.id,
            'name': obj.username
        })
    return JsonResponse({
        'status': True,
        'payload': payload
    })


def search_detail(request, id):
    mem = get_object_or_404(Member, id=id)
    print(mem)
    return render(request, "search-details.html", {"member": mem})
