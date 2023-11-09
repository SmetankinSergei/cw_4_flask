from flask import render_template, request

import main
from main import app
from src.checks import check_data


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        source = request.form.get('source_choice')
        keyword = request.form.get('keyword')
        pages_amount = request.form.get('pages_amount')
        top_amount = request.form.get('top_amount')
        action = request.form.get('action')
        if check_data(source, keyword, pages_amount, top_amount):
            vacancies = main.work_session.get_vacancies(action, source, keyword, pages_amount, top_amount)
            print(vacancies)
            return render_template('index.html', vacancies=vacancies)
        else:
            error = 'Fill in all the fields! "Pages amount" and "Top amount" must be numbers!!!'
            return render_template('index.html', error=error)
    """Главная и единственная страница"""
    return render_template('index.html')
