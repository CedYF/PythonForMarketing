#!/usr/bin/python


from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from your own developer

DEVELOPER_KEY = 'INSERTYOURKEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  developerKey=DEVELOPER_KEY)

# Replace the Q value with any query you'd like

search_response = youtube.search().list(
  q="JakePaul",
  part='id,snippet',
  maxResults=50
).execute()

videos = []
titles = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.

for search_result in search_response.get('items', []):
  #print(search_result)
  if search_result['id']['kind'] == 'youtube#video':
    videos.append('%s' % (search_result['snippet']['thumbnails']['high']['url']))
    titles.append('%s' % (search_result['snippet']['title']))


print(videos)
print(titles)
