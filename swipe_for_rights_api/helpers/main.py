import datetime
def stringify_all_dates(data):
    if type(data) is list:
        for d in data:
            stringify_all_dates(d)
    if type(data) is dict:
        for key in data.keys():
            if type(data[key]) is datetime.datetime:
                data[key] = str(data[key])
            if type(data[key]) is list:
                stringify_all_dates(data[key])
    return data