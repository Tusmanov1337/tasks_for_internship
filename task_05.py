from datetime import datetime, timedelta


def date_in_future(day):
    now = datetime.now()
    if not type(day) == int:
        return now.strftime("%d-%m-%Y %H:%M:%S")
    if day < 0: # Хоть это и ломает логику названия - дата в будущем, но все равно мне кажется это уместно
        return (now - timedelta(days=day * -1)).strftime("%d-%m-%Y %H:%M:%S")
    else:
        future_date = now + timedelta(days=day)
    return future_date.strftime("%d-%m-%Y %H:%M:%S")



