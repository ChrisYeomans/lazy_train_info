#! usr/bin/env python3
from flask import *
from flask_bootstrap import Bootstrap
from station_info import StationInfo

app = Flask(__name__)
app.config.from_object(__name__)

def main():
	Bootstrap(app)
	app.run()

@app.route('/')
def index():
	st = StationInfo("Dublin Connolly")
	info = st.info_lst
	return render_template('index.html', info=info)


if __name__ == "__main__":
	main()