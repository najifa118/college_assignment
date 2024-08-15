def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'
print(check_season('March'))
print(check_season('August'))
print(check_season('November'))
print(check_season('January'))
print(check_season('October'))
print(check_season('abc'))
