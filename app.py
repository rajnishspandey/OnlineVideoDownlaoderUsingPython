from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

PATH = os.getcwd()

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video.download(PATH)
        return "Download complete!"
    except Exception as e:
        return "An error occurred: " + str(e)

# Route for the form page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and download the video
@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']  # Get video URL from the form
    result = download_video(video_url)  # Call the download function
    return result

if __name__ == '__main__':
    app.run(debug=True)
