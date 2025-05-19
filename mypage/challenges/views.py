from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


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
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported')    
    
    