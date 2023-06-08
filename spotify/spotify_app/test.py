import re
url = 'https://open.spotify.com/playlist/35Ux8wZHG7balGjo2Zc2Uz?si=f0a0702884c14d1a'
uri = re.findall(r"\/playlist\/(\w+)", url)
print(uri[0])