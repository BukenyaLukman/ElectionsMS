from django.urls import path

from . import views

app_name = 'elections'


urlpatterns = [
	path('',views.home, name="home"),
	path('candidates_district_performance/',views.candidates_district_performance, name="performance"),
	path('candidate_profiles/',views.candidate_profiles, name="profiles"),
	path('candidate_results/',views.candidate_results, name="results"),
	path('render_category/<int:id>/',views.render_category, name="render_category"),
	path('map_activity/',views.map_activity, name="map"),
]