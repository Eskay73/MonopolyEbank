from django.shortcuts import render, redirect
from .models import games

# from django.contrib import messages
# from .forms import gameForm


# def index(request):
#     item_list = games.objects.order_by("-createdAt")
#     if request.method == "POST":
#         form = gameForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo')
#     form = gameForm()
#     return render(request, 'todo/index.html', page)

# def remove(request, item_id):
#     item = games.objects.get(id=item_id)
#     item.delete()
#     messages.info(request, "item removed !!!")
#     return redirect('todo')

def index(request):
    if(games.objects.all().first()):
        hasGame =True
    else:
        hasGame =False

    return render(request, 'index.html',{'hasGame':hasGame})
