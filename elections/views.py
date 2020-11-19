from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
	presidents = Politicians.objects.filter(electoral_positions__name__contains="President")
	categories = ElectoralPositions.objects.all()
	context = {'presidents':presidents,'categories':categories}
	return render(request, 'elections/home.html', context)

def candidates_district_performance(request):
	categories = ElectoralPositions.objects.all()
	context = {'categories':categories}
	return render(request, 'elections/candidate_district_performance.html', context)


def candidate_profiles(request):
	categories = ElectoralPositions.objects.all()
	context = {'categories':categories}
	return render(request, 'elections/candidate_profiles.html', context)

def candidate_results(request):
	categories = ElectoralPositions.objects.all()
	context = {'categories':categories}
	return render(request, 'elections/candidate_results.html', context)

def map_activity(request):
	categories = ElectoralPositions.objects.all()
	context = {'categories':categories}
	return render(request, 'elections/map_activity.html', context)

def render_category(request,id):
	results = Politicians.objects.get(id=id)
	context = {'results':results}
	return render(request, 'elections/results.html',context)
	#return JsonResponse('category obtained', safe=False)