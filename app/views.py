from django.shortcuts import render, redirect
from app.forms import ClienteForm
from app.models import Cliente


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(nome__icontains=search)

    else:
        data['db'] = Cliente.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'form.html', data)


def create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()
    return redirect('home')

