from TikTokApi import TikTokApi

api = TikTokApi()

for video in api.trending.videos(get_all = True):
    video_bytes = video.bytes()
    break

with open('test.mp4', 'wb') as out:
    out.write(video_bytes)