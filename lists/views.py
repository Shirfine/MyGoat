from django.shortcuts import render, redirect
from lists.models import List
from lists.forms import ItemForm, ExistingListItemForm


# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    # return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            # form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})

    # list_ = List.objects.get(id=list_id)
    # error = None
    #
    # if request.method == 'POST':
    #     try:
    #         item = Item(text=request.POST['text'], list=list_)
    #         item.full_clean()
    #         item.save()
    #         return redirect(list_)
    #     except ValidationError:
    #         error = "You can't have an empty list item"
    # form = ItemForm()
    # return render(request, 'list.html', {
    #     'list': list_, 'form': form, 'error': error
    # })


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        # Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})

        # list_ = List.objects.create()
        # item = Item(text=request.POST['text'], list=list_)
        # try:
        #     item.full_clean()
        #     item.save()
        # except ValidationError:
        #     list_.delete()
        #     error = "You can't have an empty list item"
        #     return render(request, 'home.html', {'error': error})
        # return redirect('view_list', list_.id)

# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['text'], list=list_)
#     return redirect('/lists/%d/' % (list_.id,))
