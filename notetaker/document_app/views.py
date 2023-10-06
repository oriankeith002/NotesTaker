from django.shortcuts import render,redirect

# Create your views here.

from .models import Document

def editor(request):
    docid = int(request.GET.get('docid',0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid',0))
        title = request.POST.get('title')
        content = request.POST.get('content','')

        # editing a stored document
        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()

            return redirect('/?docid=%i'%docid)
        else:
            # creating a new document
            document = Document.objects.create(title=title,content=content)
            return redirect('/?docid=%i' % document.id)

    if docid > 0: #here we know its not the default
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid':docid,
        'documents':documents,
        'document':document
    }

    return render(request, 'document_app/editor.html', context=context)


def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('/?docid=0')