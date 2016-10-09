from flask import Flask, redirect, url_for, request, render_template


from datetime import date, datetime
from calculations import ask_me, generate_dates_list
from calculations import disp_coin

global from_city; global to_city; global to_country; global num_days; global travellers_num
global budget; global coin; global inoutdates; global gmm

app = Flask(__name__, template_folder= 'static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_more', methods=['POST', 'GET'])
def show_more_options():
    x,y = gmm
    gmm = (x,y+1)

    d = ask_me(from_city, to_city, to_country, inoutdates, budget, num_days, travellers_num, coin, gmm )
    print len(d)
    print d

    gmm = d['gmm']
    
    ciutat0 = d['o0'][0]
    dates0 = d['o0'][1]
    hotel00 = d['o0'][2][0][0]
    
    if len(d['o0'][2]) > 1:
        hotel01 = d['o0'][2][1][0]
    else:
        hotel01 = ' '

    if len(d['o0'][2]) > 2:
        hotel02 = d['o0'][2][2][0]
    else:
        hotel02 = ' '
    preu_min0 = round(d['o0'][2][0][1],2)

    if len(d)>2:
        ciutat1 = d['o1'][0]
        dates1 = d['o1'][1]
        hotel10 = d['o1'][2][0][0]
        if len(d['o1'][2]) > 1:
            hotel11 = d['o1'][2][1][0]
        else:
            hotel11 = ' '
        if len(d['o1'][2]) > 2:
            hotel12 = d['o1'][2][2][0]
        else:
            hotel12 = ' '
        preu_min1 =  round(d['o1'][2][0][1],2)

        if len(d)>3:
            ciutat2 = d['o2'][0]
            dates2 = d['o2'][1]
            hotel20 = d['o2'][2][0][0]
            if len(d['o2'][2]) > 1:
                hotel21 = d['o2'][2][1][0]
            else:
                hotel21 = ' '
            if len(d['o0'][2]) > 2:
                hotel22 = d['o2'][2][2][0]
            else:
                hotel22 = ' '
            preu_min2 =  round(d['o2'][2][0][1],2)

            return render_template('result.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0,ciutat1=ciutat1 , dates1=dates1, hotel10=hotel10, hotel11=hotel11, hotel12= hotel12 , preu1=preu_min1,ciutat2=ciutat2 , dates2=dates2, hotel20=hotel20, hotel21=hotel21, hotel22=hotel22 , preu2=preu_min2, moneda = coin)
        else:
            return render_template('result2.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0,ciutat1=ciutat1 , dates1=dates1, hotel10=hotel10, hotel11=hotel11, hotel12= hotel12 , preu1=preu_min1, moneda = coin)
    

    else:
        return render_template('result2.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0, moneda = coin)



@app.route('/next_options', methods=['POST', 'GET'])
def next_options():
    x,y = gmm
    gmm = (x+1,y)

    d = ask_me(from_city, to_city, to_country, inoutdates, budget, num_days, travellers_num, coin )
    print len(d)
    print d

    gmm = d['gmm']
    
    ciutat0 = d['o0'][0]
    dates0 = d['o0'][1]
    hotel00 = d['o0'][2][0][0]
    
    if len(d['o0'][2]) > 1:
        hotel01 = d['o0'][2][1][0]
    else:
        hotel01 = ' '

    if len(d['o0'][2]) > 2:
        hotel02 = d['o0'][2][2][0]
    else:
        hotel02 = ' '
    preu_min0 = round(d['o0'][2][0][1],2)

    if len(d)>2:
        ciutat1 = d['o1'][0]
        dates1 = d['o1'][1]
        hotel10 = d['o1'][2][0][0]
        if len(d['o1'][2]) > 1:
            hotel11 = d['o1'][2][1][0]
        else:
            hotel11 = ' '
        if len(d['o1'][2]) > 2:
            hotel12 = d['o1'][2][2][0]
        else:
            hotel12 = ' '
        preu_min1 =  round(d['o1'][2][0][1],2)

        if len(d)>3:
            ciutat2 = d['o2'][0]
            dates2 = d['o2'][1]
            hotel20 = d['o2'][2][0][0]
            if len(d['o2'][2]) > 1:
                hotel21 = d['o2'][2][1][0]
            else:
                hotel21 = ' '
            if len(d['o0'][2]) > 2:
                hotel22 = d['o2'][2][2][0]
            else:
                hotel22 = ' '
            preu_min2 =  round(d['o2'][2][0][1],2)

            return render_template('result.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0,ciutat1=ciutat1 , dates1=dates1, hotel10=hotel10, hotel11=hotel11, hotel12= hotel12 , preu1=preu_min1,ciutat2=ciutat2 , dates2=dates2, hotel20=hotel20, hotel21=hotel21, hotel22=hotel22 , preu2=preu_min2, moneda = coin)
        else:
            return render_template('result2.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0,ciutat1=ciutat1 , dates1=dates1, hotel10=hotel10, hotel11=hotel11, hotel12= hotel12 , preu1=preu_min1, moneda = coin)
    

    else:
        return render_template('result2.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0, moneda = coin)



@app.route('/result', methods=['POST'])
def calculate_result():
    
    from_city = request.form['from_city'].encode('ascii','ignore')
    to_city = request.form['to_city'].encode('ascii','ignore')
    to_city = [str(x) for x in to_city.split(',')]
    to_country = request.form['to_country'].encode('ascii','ignore')
    to_country = [str(x) for x in to_country.split(',')]

    depart_date = datetime.strptime(request.form['depart_date'].encode('ascii','ignore'), "%Y-%m-%d").date()
    return_date = datetime.strptime(request.form['return_date'].encode('ascii','ignore').encode('ascii','ignore'), "%Y-%m-%d").date()
    num_days = int(request.form['num_days'].encode('ascii','ignore'))
    travellers_num = int(request.form['travellers_num'].encode('ascii','ignore'))
    budget = int(request.form['budget'].encode('ascii','ignore'))

    chosen_currency = request.form.get('Currency')
    
    coin = disp_coin(chosen_currency)

    
    inoutdates = generate_dates_list(depart_date, return_date, num_days)

    
    
    d = ask_me(from_city, to_city, to_country, inoutdates, budget, num_days, travellers_num, coin )
    print len(d)
    print d

    gmm = d['gmm']
    
    ciutat0 = d['o0'][0]
    dates0 = d['o0'][1]
    hotel00 = d['o0'][2][0][0]
    
    if len(d['o0'][2]) > 1:
        hotel01 = d['o0'][2][1][0]
    else:
        hotel01 = ' '

    if len(d['o0'][2]) > 2:
        hotel02 = d['o0'][2][2][0]
    else:
        hotel02 = ' '
    preu_min0 = round(d['o0'][2][0][1],2)

    if len(d)>2:
        ciutat1 = d['o1'][0]
        dates1 = d['o1'][1]
        hotel10 = d['o1'][2][0][0]
        if len(d['o1'][2]) > 1:
            hotel11 = d['o1'][2][1][0]
        else:
            hotel11 = ' '
        if len(d['o1'][2]) > 2:
            hotel12 = d['o1'][2][2][0]
        else:
            hotel12 = ' '
        preu_min1 =  round(d['o1'][2][0][1],2)

        if len(d)>3:
            ciutat2 = d['o2'][0]
            dates2 = d['o2'][1]
            hotel20 = d['o2'][2][0][0]
            if len(d['o2'][2]) > 1:
                hotel21 = d['o2'][2][1][0]
            else:
                hotel21 = ' '
            if len(d['o0'][2]) > 2:
                hotel22 = d['o2'][2][2][0]
            else:
                hotel22 = ' '
            preu_min2 =  round(d['o2'][2][0][1],2)

            return render_template('result.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0,ciutat1=ciutat1 , dates1=dates1, hotel10=hotel10, hotel11=hotel11, hotel12= hotel12 , preu1=preu_min1,ciutat2=ciutat2 , dates2=dates2, hotel20=hotel20, hotel21=hotel21, hotel22=hotel22 , preu2=preu_min2, moneda = coin)
        else:
            return render_template('result2.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0,ciutat1=ciutat1 , dates1=dates1, hotel10=hotel10, hotel11=hotel11, hotel12= hotel12 , preu1=preu_min1, moneda = coin)
    

    else:
        return render_template('result1.html', ciutat0=ciutat0 , dates0=dates0, hotel00=hotel00, hotel01=hotel01, hotel02=hotel02 , preu0=preu_min0, moneda = coin)




    

    
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")