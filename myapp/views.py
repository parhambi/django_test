from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.timezone import activate
from django.utils import timezone
from .models import Question,Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import F
from django.urls import reverse
from django.views import generic
from bitcoin import get_crypto_price
# Create your views here.
class HomeView(generic.ListView):
    template_name = "myapp/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "myapp/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "myapp/results.html"

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"myapp/detail.html",{"question":question,
                                                   "error_message":"you did not select a choice"},)
    else:
        selected_choice.votes = F("votes") +1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("myapp:results",args=(question_id,)))
    
def btc(request,crypto_asset):
    price = get_crypto_price(crypto_asset)
    return render(request,"myapp/bitcoin.html",{"price":price})