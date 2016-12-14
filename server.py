import json
import pafy

from flask import Flask, Response

app = Flask(__name__)

def generate_result(video, stream):
    return {
        "author": video.author,
        "duration": video.duration,
        "length": video.length,
        "keywords": video.keywords,
        "title": video.title,
        "username": video.username,
        "videoid": video.videoid,

        "bitrate": stream.bitrate,
        "extension": stream.extension,
        "filesize": stream.get_filesize(),
        "quality": stream.quality,
        "url": stream.url
    }

@app.route("/audio/<id>")
def get_audio_url(id):
    url = "https://www.youtube.com/watch?v=" + id
    video = pafy.new(url)
    stream = video.getbestaudio()
    return Response(
        json.dumps(generate_result(video, stream)),
        mimetype="application/json", status=200
    )

@app.route("/video/<id>")
def get_video_url(id):
    url = "https://www.youtube.com/watch?v=" + id
    video = pafy.new(url)
    stream = video.getbestvideo()
    return Response(
        json.dumps(generate_result(video, stream)),
        mimetype="application/json", status=200
    )

if __name__ == "__main__":
    app.run()
