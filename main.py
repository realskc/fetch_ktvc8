import requests
import os

n = int(input())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

if not os.path.exists('images'):
	os.mkdir('images')

images = []

for i in range(n):
	image_url = input()
	response = requests.get(image_url, headers=headers)
	id = image_url.split('/')[-1].split('.')[0]
	filename_suffix = '.' + image_url.split('.')[-1]
	filename = str(id) + filename_suffix
	images.append('images/' + filename)
	if response.status_code == 200:
		with open('images/' + filename, 'wb') as f:
			f.write(response.content)
		print('Download succeeded: ' + filename)
	else:
		print('Download failed: ' + filename)

print('Enter song name:')
song_name = input()
command = 'wsl convert ' + ' '.join(images) + ' ' + song_name + '.pdf'
os.system(command)