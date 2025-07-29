from flask import Flask, render_template, url_for
import os

app = Flask(__name__)


@app.route('/')
def home():
    image_folder = os.path.join('static', 'images')
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(
        ('.png', '.jpg', '.jpeg', '.gif'))]

    captions = [
        "Best moments with you 🥰",
        "Our craziness together 🤪",
        "Always smiling with you 😄",
        "Unforgettable memories 💖",
        "To many more adventures 🚀"
    ]

    images = [{'file': f, 'caption': captions[i % len(
        captions)]} for i, f in enumerate(image_files)]
    return render_template('index.html', images=images)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
