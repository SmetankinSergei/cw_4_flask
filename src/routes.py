from flask import render_template, request

import main
from main import app
from src.checks import check_data
from src.constants import SESSION_ACTIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    """Главная и единственная страница"""
    if request.method == 'POST':
        source = request.form.get('source_choice')
        keyword = request.form.get('keyword')
        pages_amount = request.form.get('pages_amount')
        top_amount = request.form.get('top_amount')
        action_request = request.form.get('action')
        if check_data(source, keyword, pages_amount, top_amount):
            action = SESSION_ACTIONS[action_request]
            vacancies = main.work_session.get_vacancies(action, source, keyword, pages_amount, top_amount)
            return render_template('index.html', vacancies=vacancies)
        else:
            error = 'Fill in all the fields! "Pages amount" and "Top amount" must be numbers!!!'
            return render_template('index.html', error=error)
    return render_template('index.html')
