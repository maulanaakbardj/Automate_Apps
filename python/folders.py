import calendar
from pathlib import Path

from webob import day

month_names = list(calendar.month_name[1:])
days = ['Day 1', 'Day 10', 'Day 20', 'Day 30']

Path('2022/January').mkdir(parents = True, exist_ok = True)