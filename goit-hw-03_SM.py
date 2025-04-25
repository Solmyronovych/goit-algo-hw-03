from datetime import datetime

date = '2020-10-09'

def get_days_from_today(date):
    try:
        specified_date = datetime.strptime(date, '%Y-%m-%d').date()
        #print(specified_date)
    except ValueError:
        print (f"Incorrect date format. It should be 'YYYY-MM-DD'")
        return None
    current_data = datetime.today().date()
    #print(current_data)
    delta = current_data - specified_date
    #print(delta)
    return delta.days

get_days_from_today(date)
