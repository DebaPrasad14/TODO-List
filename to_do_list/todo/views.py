from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
        else:
            pass
        all_items = List.objects.all
        messages.success(request, ('Item has been successfully added to the list.'))
        return render(request, 'home.html', {'todo_items': all_items})
    else: 
        all_items = List.objects.all
        return render(request, 'home.html', {'todo_items': all_items})


def about(request):
    my_name = "Deba M"
    company = "AMDOCS"
    context = {'name': my_name, 'company': company}
    return render(request, 'about.html', context)


def delete(request, item_id):
    item = List.objects.get(pk=item_id)
    item.delete()
    messages.success(request, ('Item has been deleted from the list!'))
    return redirect('home')


def cross_off(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    messages.success(request, ('Item has been marked as completed!'))
    return redirect('home')


def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    messages.success(request, ('Item has been marked as not completed!'))
    return redirect('home')


def edit(request, item_id):
    if request.method == 'POST':
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited successfully!'))
            return redirect('home')
    else: 
        item = List.objects.get(pk=item_id)
        return render(request, 'edit.html', {'item': item})
