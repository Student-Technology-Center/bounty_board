from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from .forms import *
from .models import *

# Create your views here.

def index(request):
    '''
    Currently returns underconstruction page
    '''

    return render(request, 'bounty_board_index.html')

def bountySubmit(request):
    '''
    View function for evaluating a workshop
    '''

    if request.method == 'POST':
        # if this is a POST request we need to process the form data
        #form = EvaluateWorkshopForm(request.POST)
        form = BountyBoardForm(request.POST)

        # check weather it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request, 'bounty_board_index.html')

    else:
        form = EvaluationForm()

    return render(request, 'bounty_board_add.html', {'form': form})
