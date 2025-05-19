from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 


monthly_challenges = {
    'january': 'Eat more meat entire month!',
    'february': 'Walk at least 20 min a day!',
    'march': 'Learn Django!',
    'april': 'Eat more meat entire month!',
    'may': 'Walk at least 20 min a day!',
    'june': 'Learn Django!',
    'july': 'Eat more meat entire month!',
    'august': 'Walk at least 20 min a day!',
    'september': 'Learn Django!',
    'october': 'Eat more meat entire month!',
    'november': 'Walk at least 20 min a day!',
    'december': 'Learn Django!'
}
# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect('/challenges/' + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')    
    
    