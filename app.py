#! usr/bin/env python3

from flask import *

app = Flask(__name__)
app.config.from_object(__name__)

def main():
	app.run()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
	main()