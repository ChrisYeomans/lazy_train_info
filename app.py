#! usr/bin/env python3
from flask import *
from flask_bootstrap import Bootstrap
from station_info import StationInfo

app = Flask(__name__)
app.config.from_object(__name__)
st = StationInfo()

def main():

	Bootstrap(app)
	app.run()

@app.route('/')
def index():
	info = st.get_info_lst("Dublin Connolly")
	return render_template('index.html', info=info)

@app.route('/info/<st_name>')
def info(st_name):
	info = st.get_info_lst(st_name)
	return render_template('info.html', info=info)

if __name__ == "__main__":
	main()