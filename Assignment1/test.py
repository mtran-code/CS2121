import sys
from io import StringIO
from Company import *
from Listing import *


def CheckOutput(expected,presented):
	if expected == presented:
		print("The output is the same as expected!")
		return 1
	else:
		print("^^^^^ This is not the expected output! ^^^^^")
		return 0 

def tests():
	totalScore=0

	# IOError exceptions
	try:
		a = Listing('Country.txt', 'companies.txt')
		totalScore+=5
		print('^^^^^Should see this printed.^^^^^')
	except: 
		print ("The exception does not handle.")

	try:
		a = Listing('countries.txt', 'Company.txt')
		totalScore+=5
		print('^^^^^Should see this printed.^^^^^')
	except: 
		print ("The exception does not handle.")


	a = Listing('countries.txt', 'companies.txt')
	# PART 2
	try:
		a.addCompany('Wolfram Research', 'Data/Technology', 777, 1987)
	except ValueError:
		totalScore+=5
		print('^^^^^Should see this printed.^^^^^')

	a.addCountry('Wolfram Research', 'United States')
	a.addCompany('Wolfram Research', 'Data/Technology', 777, 1987)

	tmpOutput="3 Round Stones, Inc. in Data/Technology sector based in United States\nCitySourced in Governance sector based in United States\nForrester Research in Research & Consulting sector based in United States\nLawdragon in Business & Legal Services sector based in United States\nPave in Finance & Investment sector based in United States\nSpotCrime in Governance sector based in United States\nGun & Bae in Lifestyle/Consumer sector based in Korea\njin hak in Education sector based in Korea\nMEDIAWILL in Housing/Real Estate sector based in Korea\nplantmobile in Data/Technology sector based in Korea\nSuperApps in Data/Technology sector based in Korea\nytndmb in Advertising sector based in Korea\nAbison Burke in Research & Consulting sector based in Mexico\nAspiria in Finance & Investment sector based in Mexico\nCentro Mexicano para la Filantropía (CEMEFI) in Business Services sector based in Mexico\nEl Narval Mundial in Research & Consulting sector based in Mexico\nINNKU in Data/Technology sector based in Mexico\nMoody\'s Analytics in Finance & Investment sector based in Mexico\nSkyAlert in Telecommunication sector based in Mexico\nWolfram Research in Data/Technology sector based in United States\n"
	totalScore+=CheckOutput(tmpOutput, str(a))*10

	totalScore+=CheckOutput('United States', a.countries['Wolfram Research'])*10

	try:
		a.addCompany('Wolfram Research', 'Data/Technology', 777, 1987)
	except ValueError:
		totalScore+=10
		print('^^^^^Should see this printed.^^^^^')

	# PART 3
	a.removeCompany('Wolfram Research')
	tmpOutput="3 Round Stones, Inc. in Data/Technology sector based in United States\nCitySourced in Governance sector based in United States\nForrester Research in Research & Consulting sector based in United States\nLawdragon in Business & Legal Services sector based in United States\nPave in Finance & Investment sector based in United States\nSpotCrime in Governance sector based in United States\nGun & Bae in Lifestyle/Consumer sector based in Korea\njin hak in Education sector based in Korea\nMEDIAWILL in Housing/Real Estate sector based in Korea\nplantmobile in Data/Technology sector based in Korea\nSuperApps in Data/Technology sector based in Korea\nytndmb in Advertising sector based in Korea\nAbison Burke in Research & Consulting sector based in Mexico\nAspiria in Finance & Investment sector based in Mexico\nCentro Mexicano para la Filantropía (CEMEFI) in Business Services sector based in Mexico\nEl Narval Mundial in Research & Consulting sector based in Mexico\nINNKU in Data/Technology sector based in Mexico\nMoody\'s Analytics in Finance & Investment sector based in Mexico\nSkyAlert in Telecommunication sector based in Mexico\n"
	totalScore+=CheckOutput(tmpOutput, str(a))*10

	try:
		a.removeCompany('Wolfram Research')
	except ValueError as ve:
		print(ve)
		totalScore+=5
		print('^^^^^Company not in list. Nothing was removed.^^^^^')
		print('^^^^^Messages should be the same(ish).^^^^^')
		print('If it says \'list.remove(x): x not in list\', something is wrong')

	# PART 4
	tmpOutput='SkyAlert in Telecommunication sector based in Mexico'
	totalScore+=CheckOutput(tmpOutput, str(a.companyDetails('SkyAlert')))*5

	tmpOutput='Wolfram Research is not in the listing.'
	totalScore+=CheckOutput(tmpOutput, str(a.companyDetails('Wolfram Research')))*5

	# PART 5
	tmpOutput="Gun & Bae in Lifestyle/Consumer sector based in Korea\njin hak in Education sector based in Korea\nMEDIAWILL in Housing/Real Estate sector based in Korea\nplantmobile in Data/Technology sector based in Korea\nSuperApps in Data/Technology sector based in Korea\nytndmb in Advertising sector based in Korea\n"
	s = StringIO()
	sys.stdout = s
	a.filterByCountry('Korea')
	s.getvalue()
	totalScore+=CheckOutput(tmpOutput,s.getvalue()) *10
	sys.stdout = sys.__stdout__

	tmpOutput="Abison Burke in Research & Consulting sector based in Mexico\nAspiria in Finance & Investment sector based in Mexico\nCentro Mexicano para la Filantropía (CEMEFI) in Business Services sector based in Mexico\nEl Narval Mundial in Research & Consulting sector based in Mexico\nINNKU in Data/Technology sector based in Mexico\nMoody\'s Analytics in Finance & Investment sector based in Mexico\nSkyAlert in Telecommunication sector based in Mexico\n"	
	s = StringIO()
	sys.stdout = s
	a.filterByCountry('Mexico')
	s.getvalue()
	totalScore+=CheckOutput(tmpOutput,s.getvalue()) *5
	sys.stdout = sys.__stdout__


	if a.filterByCountry('asd') is None:
		totalScore+=5

	# PART 6
	a.saveListing('output.txt')
	iFile = open('output.txt','r')
	tmpOutput = '3 Round Stones, Inc.|Data/Technology|United States|17|2010\nCitySourced|Governance|United States|37|2007\nForrester Research|Research & Consulting|United States|3643|1983\nLawdragon|Business & Legal Services|United States|29|2005\nPave|Finance & Investment|United States|8|2012\nSpotCrime|Governance|United States|44|2007\nGun & Bae|Lifestyle/Consumer|Korea|7|2015\njin hak|Education|Korea|139|1965\nMEDIAWILL|Housing/Real Estate|Korea|6|2015\nplantmobile|Data/Technology|Korea|5|2015\nSuperApps|Data/Technology|Korea|9|2014\nytndmb|Advertising|Korea|188|2000\nAbison Burke|Research & Consulting|Mexico|153|2002\nAspiria|Finance & Investment|Mexico|6|2013\nCentro Mexicano para la Filantropía (CEMEFI)|Business Services|Mexico|33|1988\nEl Narval Mundial|Research & Consulting|Mexico|7|2007\nINNKU|Data/Technology|Mexico|37|2008\nMoody\'s Analytics|Finance & Investment|Mexico|2294|1904\nSkyAlert|Telecommunication|Mexico|42|2011\n'
	iFileContents = iFile.read()
	totalScore+=CheckOutput(tmpOutput,iFileContents) *5

	# PART 7
	tmpOutput="Moody\'s Analytics is the largest company in Mexico.\nIt has grown to a size of 2294 employees in 115 years.\n"
	totalScore+=CheckOutput(tmpOutput,str(a.largestCompany('Mexico'))) *5
	return totalScore

def main():
	#try: 
	return tests()
	#except:
	#	return 0


print ("Your mark is",main())
