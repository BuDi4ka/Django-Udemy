from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


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
def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


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
        response_data = render_to_string('challenges/challenge.html')
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not supported</h1>')    
    
    