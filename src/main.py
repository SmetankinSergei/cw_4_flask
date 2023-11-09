from flask import Flask

from src.work_session import WorkSession

# import app_state

"""Неоднозначная конструкция, к которой пришёл после ряда экспериментов, 
для уверенности подглядев у архитектора из одной небольшой компании.."""

app = Flask(__name__)
work_session = WorkSession()
# state_now = app_state.State.WORK

import routes