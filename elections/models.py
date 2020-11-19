from django.db import models
from django.urls import reverse

class ConstituencyCategory(models.Model):
	name = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Constituency Category"

class District(models.Model):
	district = models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.district


class Constituency(models.Model):
	category = models.ForeignKey(ConstituencyCategory,null=True,blank=True,on_delete=models.SET_NULL)
	name = models.CharField(max_length=200,null=True)
	district = models.ForeignKey(District,null=True,blank=True,on_delete=models.SET_NULL)
	pollingStations = models.IntegerField(null=True)
	femaleVoters = models.IntegerField(null=True)
	maleVoters = models.IntegerField(null=True)
	population = models.IntegerField(null=True)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Constituency"


class Country(models.Model):
	name = models.CharField(max_length=50,null=True)
	polling_stations = models.IntegerField(null=True)
	female_voters = models.IntegerField(null=True)
	male_voters = models.IntegerField(null=True)
	create_date = models.DateTimeField(auto_now_add=True,null=True)
	popn = models.IntegerField(null=True)
	country_update_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Country"


class ElectoralPositions(models.Model):
	name = models.CharField(max_length=100,null=True)
	create_date = models.DateTimeField(auto_now_add=True,null=True)
	update_date = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Electoral Position"


class Parties(models.Model):
	name = models.CharField(max_length=300,null=True,blank=True)
	acronym = models.CharField(max_length=100,null=True)
	logo = models.ImageField(null=True,blank=True)
	def __str__(self):
		return str(self.name)

	class Meta:
		verbose_name_plural = "Parties"



class PoliticianCategory(models.Model):
	categoryName = models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.categoryName

	class Meta:
		verbose_name_plural = "Politician Category"

class PollingStation(models.Model):
	name = models.CharField(max_length=200,null=True)
	constituency = models.ForeignKey(Constituency,null=True,blank=True,on_delete=models.SET_NULL)
	district = models.ForeignKey(District,null=True,blank=True,on_delete=models.SET_NULL)
	numberOfVoters = models.IntegerField()

	def __str__(self):
		return str(self.name)



class Regions(models.Model):
	name = models.CharField(max_length=100,null=True)
	polling_stations = models.IntegerField(null=True)
	female_voters = models.IntegerField(null=True)
	male_voters = models.IntegerField(null=True)
	

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "Regions"


class Politicians(models.Model):  
	category = models.ForeignKey(PoliticianCategory,null=True,blank=True,on_delete=models.SET_NULL)
	region = models.ForeignKey(Regions,null=True,blank=True,on_delete=models.SET_NULL)
	education = models.CharField(max_length=255,null=True)
	institution = models.CharField(max_length=255,null=True)
	party = models.ForeignKey(Parties,null=True,blank=True,on_delete=models.SET_NULL)
	country = models.ForeignKey(Country,null=True,blank=True,on_delete=models.SET_NULL)
	constituency = models.ForeignKey(Constituency,null=True,blank=True,on_delete=models.SET_NULL)
	electoral_positions = models.ForeignKey(ElectoralPositions,null=True,blank=True,on_delete=models.SET_NULL)

	STATUS = (
			('INCUMBENT','INCUMBENT'),
			('FIRST TIME CONTESTANT','FIRST TIME CONTESTANT'),
			('CONTESTED BEFORE','CONTESTED BEFORE')
		)
	MARITAL_STATUS = (
		('MARRIED','MARRIED'),
		('SINGLE','SINGLE'),
		('DIVORCED','DIVORCED'),
	)
	politician_status = models.CharField(max_length=100,null=True,choices=STATUS)
	first_name = models.CharField(max_length=100,null=True)
	last_name = models.CharField(max_length=100,null=True)
	other_name = models.CharField(max_length=100,null=True,blank=True)
	image = models.ImageField(null=True,blank=True)
	DOB = models.DateTimeField(null=True)
	marital_status = models.CharField(max_length=300,null=True,choices=MARITAL_STATUS)
	children = models.CharField(max_length=300,null=True,blank=True)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
		
	

	

	def __str__(self):
		return self.first_name + " " + self.last_name
	class Meta:
		verbose_name_plural = "Politician"




## Votes
class ElectionResult(models.Model):
	pollingStation = models.ForeignKey(PollingStation,null=True,blank=True,on_delete=models.SET_NULL)
	district = models.ForeignKey(District,null=True,blank=True,on_delete=models.SET_NULL)
	Constituency = models.ForeignKey(Constituency,null=True,blank=True,on_delete=models.SET_NULL)
	electoral_position = models.ForeignKey(ElectoralPositions,null=True,blank=True,on_delete=models.SET_NULL)
	CandidateName = models.ForeignKey(Politicians,null=True,blank=True,on_delete=models.SET_NULL)
	totalVoters = models.IntegerField(null=True)
	InvalidVotes = models.IntegerField(null=True)
	votesObtained = models.IntegerField(null=True)
	resultsForm = models.ImageField(null=True)
	date_uploaded = models.DateTimeField(auto_now_add=True,null=True)
	is_verified = models.BooleanField(default=False)


	def __str__(self):
		return str(self.pollingStation)

	def get_absolute_url(self):
		return reverse('elections:results')

	class Meta:
		verbose_name_plural = "Election Results"


