import datetime


def date_in_future(days):
    if not isinstance(days, int):
        current_date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return current_date
    else:
        future_date = (datetime.datetime.today() + datetime.timedelta(days=days)).strftime('%d-%m-%Y %H:%M:%S')
        return future_date