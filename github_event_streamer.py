import csv
import time
import json
import requests

# constant
const_event_to_watch = ['WatchEvent', 'PullRequestEvent', 'IssuesEvent']
const_api_url_to_watch = 'https://api.github.com/events'
const_timer = 10

def main():
    first_id = '0'
    while True:       
        # get the API 
        complete_api = requests.get(const_api_url_to_watch)
        if complete_api.status_code != 200:
            print('API not success')
        else:
            complete_api = complete_api.json()

            i = 0
            for event in complete_api:

                if(event['type'] in const_event_to_watch):

                    # checking previous ID
                    #print('comparing between'+first_id+' and '+event['id'])
                    if (first_id != event['id']):

                        # id update
                        if (i == 0):
                            print('comparing the previousid '+first_id+' with the new id '+event['id'])
                            first_id = event['id']

                        # prepare new event row
                        new_event = [
                            event['id'],
                            event['type'],
                            event['created_at'],
                            event['repo']['id'],
                            event['repo']['name']
                        ]
                        print(new_event)
                        # save the new event
                        with open(r'events.csv', 'a') as f:
                            writer = csv.writer(f)
                            writer.writerow(new_event)

                        # update i
                        i += 1

                    else:
                        print('same batch as the previous')
                        break;

        print('=============')
        # run every timer seconds
        time.sleep(const_timer)
    
if __name__ == '__main__':
    print('Github events stream is running')
    print('=============')
    main()
