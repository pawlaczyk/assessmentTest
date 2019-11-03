from django.shortcuts import redirect
from django.shortcuts import render
from .forms import DocumentForm

def add_document(request):
    if request.method == "POST":
        form = DocumentForm(
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            document = form.save()
            return redirect("add_document_done")
    else:
        form = DocumentForm()
    return render(request, "documents/change_document.html", {'form': form})
