import requests
import json

def ask_skyscanner(originplace,destinationplace,outbounddate,inbounddate,country='ES',currency='EUR',locale='spa',adults=1,groupPricing=False):
    info = {'apiKey': 'prtl6749387986743898559646983194', 'country': country, 'currency': currency, 'locale': locale,\
            'originplace': originplace, 'destinationplace': destinationplace, 'outbounddate': outbounddate,\
            'inbounddate': inbounddate, 'adults': adults, 'groupPricing':groupPricing}
    r = requests.post('http://partners.api.skyscanner.net/apiservices/pricing/v1.0', data=info)
    g = requests.get(r.headers['Location']+'?apiKey=prtl6749387986743898559646983194')
    ucode  = g.text
    ucode  = ucode.encode('ascii','ignore')
    
    d = json.loads(ucode)
    print('d')
    print(d)
    return d['Itineraries'][0]['PricingOptions'][0]['Price']

def ask_hotelscanner(entityid,checkindate,checkoutdate,budget,guests=1,rooms=1,market='ES',currency='EUR',locale='spa'):
    headers = {'Accept': 'application/json'}
    a = requests.get('http://partners.api.skyscanner.net/apiservices/hotels/autosuggest/v2/'+market+'/'+currency+'/'+locale+'/'+entityid[0:3]+'?apikey=prtl6749387986743898559646983194', headers = headers)
    ucode = a.text
    ucode = ucode.encode('ascii','ignore')
    a     = json.loads(ucode)
    print 'We suppose you mean '+ a['results'][0]['display_name']+'.'
    
    entityid = a['results'][0]['individual_id']
    
    d = requests.get('http://partners.api.skyscanner.net/apiservices/hotels/liveprices/v2/'+market+'/'+currency+'/'+locale+'/'+entityid+'/'+checkindate+'/'+checkoutdate+'/'+str(guests)+'/'+str(rooms)+'?apiKey=prtl6749387986743898559646983194', headers = headers)
    g = requests.get('http://partners.api.skyscanner.net'+d.headers['Location']+'&sortColumn=rating&sortOrder=desc')
    
    ucode  = g.text
    ucode  = ucode.encode('ascii','ignore')

    d  = json.loads(ucode)
    h  = []
    lh = 0
    
    print(d)
    for i in xrange(len(d['hotels_prices'])):
        print(i)
        price = d['hotels_prices'][i]['agent_prices'][0]['price_total']
        if price < budget:
            h.append((d['hotels'][i]['name'],price))
        if len(h) >= 3:
            return h
    return h

def life_costs(destinationplace,delta):
    d = {"Bermuda":61.5, "Switzerland":55.1,"Bahamas":46.62, "Norway":45.72,\
    "Iceland":43.71,"Japan":40.8, "Singapore":38.2, "Denmark":37,"New Zealand":35.8,\
    "Luxembourg":35.72,"Kuwait":35.1,"Australia":35, "Ireland":34.5,"Hong Kong":34.3,\
    "Sweden":34,"France":33.7,"Belgium":33.4,"Israel":33,"South Corea":32.6,\
    "Finland":32.6,"United States":32.1,"Netherlands":32,"United Kingdom":31.9,\
    "Austria":31.5,"Italy":30.5,"Canada":30.3,"Qatar":29.8,"Germany":29.3,"United Arab Emirates":28.8, "Spain":25,\
    "Taiwan":25.2,"Greece":24.4, "Argentina":24.2,"Portugal":21.8,"Brazil":21.5,"China":20,"Mexico":14.5,"India":10.5}
       
    if False:
        return d[destinationplace]*delta
    else:
        return 100

def ask_me(originplace, destinationplacelist, inoutbounddatelist, budget, delta):
    hlist = []
    for destinationplace in destinationplacelist:
        for inoutbounddate in inoutbounddatelist:
            inbounddate, outbounddate = inoutbounddate
            price  = ask_skyscanner(originplace,destinationplace,inbounddate,outbounddate)
            lcosts = life_costs(destinationplace, delta)
            if price < (budget - lcosts):
                ll         = [originplace,destinationplace,inbounddate,outbounddate]
                hotelprice = ask_hotelscanner(destinationplace,inbounddate,outbounddate,budget-lcosts-price)
                if hlist != []:
                    hlist.append(hotelprice)
            if len(hlist) >= 3:
                return hlist
    return hlist

#print(ask_hotelscanner('bcn','2016-10-20','2016-10-21',1000))
print(ask_me('bcn-sky', ['stn-sky','edi-sky','mad-sky'], llistadates, 1000, 4))