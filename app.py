#! usr/bin/env python3
from flask import *
from flask_bootstrap import Bootstrap
from station_info import StationInfo

app = Flask(__name__)
app.config.from_object(__name__)
st = StationInfo()
info_cols = ["Origin", "Destination", "Origintime", "Destinationtime", "Status", "Lastlocation", "Duein", "Late", "Exparrival", "Expdepart", "Scharrival", "Schdepart"]

def main():
	Bootstrap(app)
	app.run()

@app.route('/')
def index():
	st_lst = st.get_station_lst()
	return render_template('index.html', st_lst=st_lst)

@app.route('/info/<st_name>')
def info(st_name):
	info = st.get_info_lst(st_name)
	return render_template('info.html', info=info, cols=info_cols, st_name=st_name)

if __name__ == "__main__":
	main()