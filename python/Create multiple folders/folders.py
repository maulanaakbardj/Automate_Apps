import calendar
from pathlib import Path

from webob import day, month

month_names = list(calendar.month_name[1:])
days = ['Day 1', 'Day 10', 'Day 20', 'Day 30']

for i, month in enumerate(month_names):
    for day in days:
        Path(f'python/Create multiple folders/results/2022/{i+1}.{month}/{day}').mkdir(parents = True, exist_ok = True)