import requests
search = str(input('Enter movie name to search '))
url = 'http://www.omdbapi.com/?apikey=adfa54be&s='+search
r = requests.get(url).json()

try:
	for x in range(len(r['Search'])):
		title = r['Search'][x]['Title']
		print('title: ' + title)
		imdb = r['Search'][x]['imdbID']
		print('imdbid: ' + imdb)
		print('Year: '+ r['Search'][x]['Year'])
		print('Image: '+ r['Search'][x]['Poster'])
		print('Type: ' + r['Search'][x]['Type'])
		print('More Info: ' + 'http://www.imdb.com/title/'+imdb+'/')
		print()
		print()
		
except Exception as e:
	print(str(e))





