import requests

response = requests.get("https://www.gutenberg.org/files/2701/old/moby10b.txt")
print(response.text.count("e"))