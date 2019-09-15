from django.http import HttpResponseRedirect
from django.shortcuts import render
from polls.models import Paste
from polls.forms import pasteForm
from django.template import RequestContext

# def index(request):
#       #  latest_question_list = Paste.objects.order_by('-pub_date')[:5]
#   #  context = {'latest_question_list': latest_question_list}
#     return render(request , 'index.html' )

def index(request):
    result={}
    if request.method=='GET' and "id" in request.GET:
        id=request.GET.get("id")
        id=int(id)
        print(id)
        if id:
            result=Paste.objects.get(id=id)
            print(result)

            context = RequestContext(request)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = pasteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            form = pasteForm()
            return HttpResponseRedirect('/polls/')
   
    form = pasteForm()
    return render(request, 'index.html', {'form': form ,"result":result} )
