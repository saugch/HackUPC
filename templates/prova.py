from calculations import ask_me, generate_dates_list

from_city ='bcn-sky'; to_city=['stn-sky']; 
inoutdates = [('2016-10-08', '2016-10-12'), ('2016-10-09', '2016-10-13'), ('2016-10-10', '2016-10-14'), ('2016-10-11', '2016-10-15'), ('2016-10-12', '2016-10-16'), ('2016-10-13', '2016-10-17'), ('2016-10-14', '2016-10-18')]
budget = 1000
num_days = 4

d = ask_me(from_city, to_city, inoutdates, budget, num_days)

print d