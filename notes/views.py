from django.shortcuts import render,redirect, get_object_or_404
from notes.models import Notes
from notes.forms import NotesForm, NotesItemForm

# Create your views here.
def notes_list(request):
    notes = Notes.objects.all()
    return render(request, "notes/notes_list.html", {
        "notes": notes,
    })

def notes_detail(request, pk):
    notes = get_object_or_404.objects.get(pk=pk)
    
    if request.method == "POST":
        notes_item_form = NotesItemForm(request.POST)
        if notes_item_form.is_valid():
            new_item = notes_item_form.save(commit=False)
            new_item.notes = notes

            last_item = notes.items.order_by('-order')[0]
            new_item.order = last_item.order + 1

            new_item.save()

            return redirect(to='notes_detail', pk=pk)
    else:
        notes_item_form = NotesItemForm()

    return render(request, "notes/notes_detail.html", {
        "item_form": notes_item_form,
        "notes": notes,
    })

def notes_create(request):
    if request.method == "POST":  # form was submitted
        form = NotesForm(request.POST)
        if form.is_valid():
             notes = form.save()
        return redirect(to=notes)
    else:
        form = NotesForm()

        return render(request, "notes/notes_create.html", {"form": form})

   
def notes_edit(request, pk):
       notes = get_object_or_404(Notes, pk=pk)

    if request.method =="POST":
        form = NotesForm(instance=note, data=request.POST)
        if form.is_valid():
             notes = form.save()
       return redirect(to="notes_list")
    else:
       form = NotesForm()

    return render(request, "notes/notes_list.html", {"form": form})

def notes_delete(request, pk):
       note = get_object_or_404(Notes, pk=pk)
    if request.method =="POST":
       notes= form.delete()
    return redirect(to="notes_list")

    else:
       form = NotesForm()

    return render(request, "notes/notes_list.html", {"form": form})
