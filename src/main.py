from flask import Flask

from src import app_state
from src.dao import DAO
from src.work_session import WorkSession


"""Неоднозначная конструкция, к которой пришёл после ряда экспериментов, 
для уверенности подглядев у архитектора из одной небольшой компании.."""

app = Flask(__name__)
main_dao = DAO(app_state.State.WORK)
work_session = WorkSession(main_dao)

import routes
