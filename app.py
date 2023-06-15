from flask import Flask, request, render_template
import get_data
import w
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/show_records")
def show_records():
    python_datas = get_data.get_data()
    return render_template('show_records.html',html_datas = python_datas)

@app.route("/select_records", methods=['GET', 'POST'])
def select_records():
    if request.method == 'POST':
        # 偷看一下 request.form 
        print(request.form)
        python_records = w.web_select_py(request.form)
        return render_template("show_records.html", html_datas = python_records)
        #python_datas = get_data.get_data()
        #return render_template('show_records.html',html_datas = python_datas)
    else:
        return render_template("select_records.html")

if __name__ == "__main__":
    app.run(debug=True)