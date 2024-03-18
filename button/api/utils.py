from datetime import date


def automatic_created_filler(data, user):
    today = date.today()
    data.update('created_at', today.year * 10000 + today.month * 100 + today.day)
    data.update('created_by', user.pk)


def automatic_updated_filler(data, user):
    today = date.today()
    data.update('updated_at', today.year * 10000 + today.month * 100 + today.day)
    data.update('updated_by', user.pk)
