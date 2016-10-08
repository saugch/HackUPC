from flask import Flask, redirect, url_for, request
from datetime import date, datetime
from calculations import ask_me, generate_dates_list

app = Flask(__name__, template_folder= 'static')

@app.route('/')
def index():
    return redirect(url_for('static', filename= 'index.html'))

@app.route('/result', methods=['POST'])
def calculate_result():
    
    from_city = request.form['from_city'].encode('ascii','ignore')
    to_city = [request.form['to_city'].encode('ascii','ignore')]
    depart_date = datetime.strptime(request.form['depart_date'].encode('ascii','ignore'), "%Y-%m-%d").date()
    return_date = datetime.strptime(request.form['return_date'].encode('ascii','ignore').encode('ascii','ignore'), "%Y-%m-%d").date()
    num_days = int(request.form['num_days'].encode('ascii','ignore'))
    travellers_num = int(request.form['travellers_num'].encode('ascii','ignore'))
    budget = int(request.form['budget'].encode('ascii','ignore'))

    inoutdates = generate_dates_list(depart_date, return_date, num_days)

    #chosen_currency = request.form['chosen_currency']
    d = ask_me(from_city, to_city, inoutdates, budget, num_days)

    print from_city, to_city, inoutdates, budget, num_days, inoutdates
    print 'res', d

    #print type(from_city), type(to_city), type(depart_date), type(return_date), type(num_days), type(travellers_num), type(budget)
    #from_city = from_city.encode('ascii','ignore')
    #print from_city, type(from_city)
    
    return render_template2('result.html', destinacio= to_city )
    #return redirect(url_for('static', filename='result.html', res='HOLA!!'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")