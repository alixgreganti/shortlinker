import csv
from datetime import datetime

from flask import Flask, request, jsonify, render_template, redirect
from slugify import slugify

from config import configs
from scraper import TripAdvisor
from upload import DataUploader
from datasets import DataSets

import random
import string

app = Flask(__name__)

def generate_code(length=8):
    characters = string.ascii_letters + string.digits  # includes both uppercase and lowercase letters
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

@app.route('/')
def home():
    return "Hello!"

@app.route('/<path:shortcode>')
def redirect_to_url(shortcode):
    # 1. search DB for shortcode, and return url.
    # url = search_db_for_url(shortcode)
    # if url is not None:
    #     return redirect(url)
    # else:
    #     return "Invalid shortcode", 404
    return "WIP"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880, debug=True)
