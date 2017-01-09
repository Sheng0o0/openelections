import csv
import locale
import sys

locale.setlocale(locale.LC_ALL, '')

csv_filepath = sys.argv[1]

winner = []
loser = []


with open(csv_filepath, 'rb') as csvfile:
    rows = csv.reader(csvfile)
    is_header = True
    for row in rows:
        if is_header:
            is_header = False
            continue

        title = row[2]
        total_gross = row[5]
        total_gross = int(total_gross[1:].replace(',', ''))
        budget = row[6]
        week = row[7]
        if not budget:
            continue
        budget = int(budget[1:].replace(',', ''))*1000000
        if total_gross > budget:
            winner.append({
            'title':title,
            'total_gross':total_gross,
            'budget':budget,
            'week':week,
            })

        if total_gross < budget:
            loser.append({
            'title':title,
            'total_gross':total_gross,
            'budget':budget,
            'week':week,
            })

for winner in winner:
    title = winner['title']
    total_gross = winner['total_gross']
    budget = winner['budget']
    profit = total_gross - budget
    week = winner['week']
    print '"{0}" Profit:{1} week:{2}'.format(
    title,
    locale.currency(profit, grouping=True),
    week,
    )

for loser in loser:
    title = loser['title']
    total_gross = loser['total_gross']
    budget = loser['budget']
    profit = total_gross - budget
    week = loser['week']
    print '"{0}" Profit:{1} week:{2}'.format(
    title,
    locale.currency(profit, grouping=True),
    week,
    )
