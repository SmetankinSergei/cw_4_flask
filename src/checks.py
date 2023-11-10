def check_data(source, keyword, pages_amount, top_amount):
    """Проверяет валидность данных"""
    if source == 'hh' or source == 'sj':
        if keyword != '':
            if pages_amount.isdigit() and top_amount.isdigit():
                return True
    return False
