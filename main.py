from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, template_folder= 'static')

@app.route('/')
def index():
    return redirect(url_for('static', filename= 'index.html'))

@app.route('/result', methods=['POST'])
def calculate_result():
    
    from_city = request.form['from_city']
    to_city = request.form['to_city']
    depart_date = request.form['depart_date']
    return_date = request.form['return_date']
    num_days = request.form['num_days']
    travellers_num = request.form['travellers_num']
    budget = request.form['budget']
    #chosen_currency = request.form['chosen_currency']

    print type(from_city), type(to_city), type(depart_date), type(return_date), type(num_days), type(travellers_num), type(budget)
    from_city = from_city.encode('ascii','ignore')
    print from_city, type(from_city)
    
    return 'from_city', from_city
    #return render_template('result.html', res=x)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")