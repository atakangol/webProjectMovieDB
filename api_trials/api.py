import requests


api_key = "6d61b3e2ab08b90b76aba55d68fd4fac"
#dont know how to put secrets exactly

'''
req = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=en-US".format(api_key))

#print(req.json())

response = req.json()
print(response)

print("all the genres in the database:\n")
for i in response["genres"]:
    print(i["name"])

'''


req = requests.get("https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US,null".format(movie_id = 605,api_key = api_key))

req = req.json()

path = (req["poster_path"])
'''
for i in req:
    print(i)
'''
path_to_image = "https://image.tmdb.org/t/p/original{path}".format(path = path)





html = """
<!DOCTYPE html>
<html lang="en">

<head>
</head>
<p> hello world! </p>
<img src="{source}" alt="matrix">
<body>
</body>

</html>
""".format(source = path_to_image)

f= open("try.html","w")

f.write(html)
f.close


