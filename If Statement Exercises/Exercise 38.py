month=(input('month:'))
days_in_month = {
    'January' and 'january' and '1': 31,
    'February' and 'february' and '2': '28 or 29',  
    'March' and 'march' and '3': 31,
    'April' and 'april' and '4': 30,
    'May' and 'may' and '5': 31,
    'June' and 'june' and '6': 30,
    'July' and 'july' and '7': 31,
    'August' and 'august' and '8': 31,
    'September' and 'september' and '9': 30,
    'October' and 'october' and '10': 31,
    'November' and 'november' and '11': 30,
    'December' and 'december' and '12': 31}
if month in days_in_month:
    print('This month has',f'{days_in_month[month]} days.')
else:
    print('Invalid month.')