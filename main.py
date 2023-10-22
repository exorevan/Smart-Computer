import sqlite3
import sys
from datetime import date, timedelta, datetime
from math import ceil

import matplotlib.pyplot as plt
import numpy as np
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QIcon
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta
from matplotlib import ticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from core.lib.handlers.crypt.substitute.simple_substitute import SimpleSubstitute
from core.lib.handlers.crypt.transposition.simple_transposition import SimpleTransposition


def run():
    simp_sub = SimpleSubstitute()
    simp_sub.sub_type = 'cesar'
    simp_sub.cesar_offset = "5"
    result = simp_sub.encrypt('.Шифр Цезаря?') # .Энщх Ыймехд?
    print(result)
    new_simp_sub = SimpleSubstitute()
    new_result = new_simp_sub.decrypt('.Энщх Ыймехд?') # .Шифр Цезаря?
    print(new_result)

    simp_sub.sub_type = 'atbash'
    result = simp_sub.encrypt('/Шифр Атбаш\\') # /Жцко Ямюяж\
    print(result)
    new_simp_sub.sub_type = 'atbash'
    result = new_simp_sub.encrypt('/Жцко Ямюяж\\') # /Шифр Атбаш\
    print(result)

    simp_trans = SimpleTransposition()
    simp_trans.trans_type = 'route'
    simp_trans.cols_count = 6
    result = simp_trans.encrypt('.Маршрутный шифр?') # шу.итмфнарыр?йш  р
    print(result)
    result = simp_trans.decrypt('шу.итмфнарыр?йш  р') # .Маршрутный шифр?
    print(result)
    

if __name__ == "__main__":
    run()