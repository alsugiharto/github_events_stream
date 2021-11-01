import csv
import time
import json
import pandas as pd
import requests
from datetime import datetime, timedelta
from io import StringIO
import base64
from matplotlib import pyplot as plt

const_timer = 10
offset = 60

def overview(offset):
	colnames = ['id', 'type', 'date', 'repo_id', 'repo_name']
	FMT = '%Y-%m-%dT%H:%M:%SZ'
	try:
		offset = int(offset)
	except:
		return ({'message': 'invalid input'})
	# get now time + offsets
	now = datetime.now() - timedelta(minutes=offset)
	now = now.strftime(FMT)

	# load events, filtered, sorted
	event_list = pd.read_csv('events.csv', names=colnames, header=None)
	filtered_event_list = event_list.loc[event_list['date'] > now]

	# count size each grouped
	grouped_counted_event = filtered_event_list.groupby(['type']).size()

	# return as json
	json_event = grouped_counted_event.to_json(orient='columns')
	return (json.loads(json_event))

def main():
	const_timer = 60
	# a day
	offset = 86400

	while True:

		# get the data
		table = overview(offset)

		if (len(table) != 0):
			# draw
			fig = plt.figure()
			ax = fig.add_axes([0, 0, 1, 1])
			x = list(table.keys())
			y = list(table.values())
			ax.bar(x, y)
			fig.savefig('overview.png', bbox_inches='tight')
			plt.close(fig)
			print('new events image is updated')
			time.sleep(const_timer)
		else:
			print('no new events')

if __name__ == '__main__':
	print('Github overview update is running')
	print('=============')
	main()
