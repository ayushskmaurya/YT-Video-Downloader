from flask import Flask, jsonify, render_template, request
from pytube import YouTube
# pip install pytube3
import threading

app = Flask(__name__)
data = {}


@app.route('/download_status')
def download_status():
    return jsonify(status=data['download'].is_alive())


def download_video():
    data['stream'].download()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.form.get('search'):
        try:
            link = request.form['link'].strip()
            data['yt'] = YouTube(link)
            data['title'] = data['yt'].title
            resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']
            data['res'] = []
            for resolution in resolutions:
                stream = data['yt'].streams.filter(mime_type="video/mp4", res=resolution, progressive=True)
                if len(stream) != 0:
                    data['res'].append(resolution)
            if len(data['res']) == 0:
                raise Exception()
            return render_template('download.html', title=data['title'], res=data['res'])
        except:
            return render_template('error.html')

    if request.form.get('download'):
        res = request.form['res']
        stream = data['yt'].streams.filter(mime_type="video/mp4", res=res, progressive=True)
        data['stream'] = stream[0]
        data['download'] = threading.Thread(target=download_video)
        data['download'].start()
        file_size = round(data['stream'].filesize / (1024*1024), 2)
        return render_template('downloading.html', title=data['title'], filesize=file_size)

    return render_template('index.html')


app.run()
