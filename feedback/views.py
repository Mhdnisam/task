from django.shortcuts import render, redirect

# Create your views here.
from feedback.forms import FeedbackModelForm
from feedback.models import Feedback


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackModelForm()
    return render(request, 'feedback.html', {'form': form})


def show_feedback(request):
    form = Feedback.objects.all()
    context = {
        'form': form
    }
    return render(request, 'show.html', context)
