from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/search", methods=["POST", "GET"])
def searchr():
	results = []
	f = 0
	if request.method == "POST":
		query1 = request.form["query"]
		data = pd.read_excel('db.xlsx')
		if query1 in list(data['TERM']):
			r = data[data['TERM'] == query1]
			for i in range(len(r)):
				l = str(r['DESC'].iloc[i])
				k = str(r['LINK'].iloc[i])
				results.append([l,k])
				f = 1
		else:
			results = []
		return render_template("search.html", result=results, query=query1,fl=f)



if __name__ == '__main__':
	app.run(debug=True)