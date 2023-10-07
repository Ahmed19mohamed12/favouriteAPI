from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route("/api", methods=['GET'])
def home():
    d = {}
    d['Query'] = str(request.args['Query'])
    yt = YouTube("https://www.youtube.com/watch?v="+str(request.args['Query']))
    yt.set_api_key("/api")
    # Get the video title and author
    title = yt.title
    author = yt.author
    audio = yt.streams.filter(only_audio=True).first().url
    publish_date = yt.publish_date
    duration = yt.length
    thumbnail_url = yt.thumbnail_url
    d['title'] = title
    d['author'] = author
    d['audio'] = audio
    d['upload_date'] = publish_date
    d['duration'] = duration
    d['thumbnail_url'] = thumbnail_url
    # Download the highest resolution audio stream available
    # yt.streams.get_audio_only().download(output_path='.', filename=f'{title} by {author}.mp3')
    
    return jsonify(d)
