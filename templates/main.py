from flask import Flask, redirect, url_for, request, render_template


from datetime import date, datetime
from calculations import ask_me, generate_dates_list
from calculations import disp_coin

app = Flask(__name__, template_folder= 'static')


@app.route('/')
def index():
    return redirect(url_for('static', filename= 'index.html'))

@app.route('/result', methods=['POST'])
def calculate_result():
    
    from_city = request.form['from_city'].encode('ascii','ignore')
    to_city = [request.form['to_city'].encode('ascii','ignore')]
    to_country = [request.form['to_country'].encode('ascii','ignore')]
    depart_date = datetime.strptime(request.form['depart_date'].encode('ascii','ignore'), "%Y-%m-%d").date()
    return_date = datetime.strptime(request.form['return_date'].encode('ascii','ignore').encode('ascii','ignore'), "%Y-%m-%d").date()
    num_days = int(request.form['num_days'].encode('ascii','ignore'))
    travellers_num = int(request.form['travellers_num'].encode('ascii','ignore'))
    budget = int(request.form['budget'].encode('ascii','ignore'))

    chosen_currency = request.form.get('Currency')
    coin = disp_coin(chosen_currency)

    inoutdates = generate_dates_list(depart_date, return_date, num_days)

    
    
    d = ask_me(from_city, to_city, to_country, inoutdates, budget, num_days, travellers_num, coin )
    print d
    #d =  {'gmm': (0, 2), 'o2': [u'VALE-sky', '2016-10-10', [(u'Vincci Lys', 656.66), (u'Sorolla Centro', 568.66), (u'Pio Xii Apartments Valencia', 485.65999999999997)]], 'o1': [u'VALE-sky', '2016-10-09', [(u'Vincci Lys', 709.99), (u'Sorolla Centro', 652.99), (u'Hotel Dimar', 642.99)]], 'o0': [u'VALE-sky', '2016-10-08', [(u'Sh Valencia Palace', 906.0899999999999), (u'Tryp Valencia Ocenic Hotel', 871.0899999999999), (u'Sercotel Sorolla Palace', 835.0899999999999)]]}

    #print from_city, to_city, inoutdates, budget, num_days, inoutdates
    #print 'res'#, d

    #print type(from_city), type(to_city), type(depart_date), type(return_date), type(num_days), type(travellers_num), type(budget)
    #from_city = from_city.encode('ascii','ignore')
    #print from_city, type(from_city)

    ciutat0 = d['o0'][0]
    dates0 = d['o0'][1]
    hotel00 = d['o0'][2][0][0]
    hotel01 = d['o0'][2][1][0]
    hotel02 = d['o0'][2][2][0]
    preu_min0 = round(d['o0'][2][0][1],2)

    if len(d)>2:
        ciutat1 = d['o1'][0]
        dates1 = d['o1'][1]
        hotel10 = d['o1'][2][0][0]
        hotel11 = d['o1'][2][1][0]
        hotel12 = d['o1'][2][2][0]
        preu_min1 =  round(d['o1'][2][0][1],2)

        if len(d)>3:
            ciutat2 = d['o2'][0]
            dates2 = d['o2'][1]
            hotel20 = d['o2'][2][0][0]
            hotel21 = d['o2'][2][1][0]
            hotel22 = d['o2'][2][2][0]
            preu_min2 =  round(d['o2'][2][0][1],2)
        else:
            ciutat2 = 'Blank'
            dates2 = 'Blank'
            hotel20 = 'Blank'
            hotel21 = 'Blank'
            hotel22 = 'Blank'
            preu_min2 =  'Blank'
    

    else:
        ciutat1, ciutat2 = 'Blank','Blank'
        dates1, dates2 = 'Blank','Blank'
        hotel10, hotel20 = 'Blank','Blank'
        hotel11, hotel21 = 'Blank','Blank'
        hotel12, hotel22 = 'Blank','Blank'
        preu_min1, preu_min2 =  'Blank','Blank'




    

    
    return render_template('result.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0,ciutat1=ciutat1 , dates1=dates1, hotel10=hotel10, hotel11=hotel11, hotel12= hotel12 , preu1=preu_min1,ciutat2=ciutat2 , dates2=dates2, hotel20=hotel20, hotel21=hotel21, hotel22=hotel22 , preu2=preu_min2, moneda = coin)
    #return render_template('result.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")