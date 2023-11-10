from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        download_path = 'path_to_save_video'  # Specify your download path
        video.download(download_path)
        return "Download complete!"
    except Exception as e:
        return "An error occurred: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
