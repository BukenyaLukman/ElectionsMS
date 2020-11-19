from django.contrib import admin

from .models import *

class ElectionResultAdmin(admin.ModelAdmin):
	list_display = ('pollingStation','date_uploaded','district','is_verified')
	search_fields = ('pollingStation',)
	actions = ('set_results_verfied',)
	fields = ('pollingStation',
		'district',
		'Constituency',
		'electoral_position',
		('CandidateName',),
		('totalVoters','InvalidVotes'),
		('votesObtained',),
		('resultsForm',))

	list_filter = ('pollingStation','Constituency','district','date_uploaded')
	list_per_page = 50

	def set_results_verfied(self,request,queryset):
		count = queryset.update(is_verified=True)
		self.message_user(request, 'Results from {} Verified'.format(count))
	set_results_verfied.short_description = 'Results Verified'

class ConstituencyAdmin(admin.ModelAdmin):
	list_display = ('name','district','pollingStations','maleVoters','femaleVoters',)


class CountryAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'polling_stations',
		'female_voters',
		'male_voters',
		'popn'
		)

class PartiesAdmin(admin.ModelAdmin):
	list_display = ('name','acronym','logo')
	list_filter = ('name',)
	search_fields = ('name',)

class RegionAdmin(admin.ModelAdmin):
	list_display = ('name','polling_stations','female_voters','male_voters',)
	list_filter = ('name','polling_stations',)
	search_fields = ('name',)

class PollingStationAdmin(admin.ModelAdmin):
	list_display = ('name','constituency','district','numberOfVoters')
	list_filter = ('name','constituency','district',)
	search_fields = ('name',)
class PoliticiansAdmin(admin.ModelAdmin):
	list_display = ('category','first_name','last_name','constituency','education')

class PoliticiansAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','constituency','electoral_positions','education','party')
	list_filter = ('electoral_positions',)
	search_fields = ('last_name',)
		

admin.site.register(Constituency,ConstituencyAdmin)
admin.site.register(ConstituencyCategory)
admin.site.register(Country)
admin.site.register(Parties,PartiesAdmin)
admin.site.register(ElectoralPositions)
admin.site.register(Politicians,PoliticiansAdmin)
admin.site.register(Regions)
admin.site.register(PoliticianCategory)
admin.site.register(ElectionResult,ElectionResultAdmin)
admin.site.register(District)
admin.site.register(PollingStation,PollingStationAdmin)

admin.site.site_header = "NBSUGVOTES2021"
admin.site.site_title = "UGVOTES2021"
admin.site.index_title = "NBSUGVOTES2021"
