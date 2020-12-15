import requests

url = "https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&key={KEY}&part=snippet&maxResults=10"
response = requests.get(url)
data = response.json()
for video in data['items'][0:6]:
    print(video['snippet']['title'])
