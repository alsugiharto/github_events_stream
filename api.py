from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
from datetime import datetime, timedelta
import json
from flask import send_file
from io import StringIO
import base64
from matplotlib import pyplot as plt
import overview_visualisation

app = Flask(__name__)
api = Api(app)

class AveragePullTime(Resource):
    def get(self, repo_id):

        colnames=['id', 'type', 'date', 'repo_id', 'repo_name']
        FMT = '%Y-%m-%dT%H:%M:%SZ'
        try:
            repo_id = int(repo_id)
        except:
            return({'message':'invalid input'})

        # load events, filtered, sorted
        event_list = pd.read_csv('events.csv', names=colnames, header=None)
        filtered_event_list = event_list.loc[(event_list['repo_id'] == repo_id) & (event_list['type'] == 'PullRequestEvent')]

        # if there is only one repo history
        if (len(filtered_event_list) == 0):
            return({'message':'this repo does not exists in our database'})
        
        # if there is only two repo history
        elif (len(filtered_event_list) == 1):
            return({'message':'This repo only has one pull request. It needs at least two requests'})
        
        # if there are enough repo history
        else:
            timelist = sorted(filtered_event_list['date'].tolist())

            # calculate time different
            time_list = []
            for i in range(0,len(filtered_event_list)-1):    
                t1 = timelist[i]
                t2 = timelist[i+1]
                different_time = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
                time_list.append(different_time)

            # calculate average time
            total_time = time_list[0]
            for i in range(0, len(time_list)):
                if (i != 0):
                    total_time += time_list[i]
            average_time = total_time/len(time_list)
            
            return({'days':average_time.days,'seconds':average_time.seconds})

class Overview(Resource):
    def get(self, offset):
        return(overview_visualisation.overview(offset))

class Visualize(Resource):
    def get(self):

        #return image
        return(send_file('overview.png', mimetype='image/png'))

api.add_resource(AveragePullTime, '/averagepulltime/<string:repo_id>')
api.add_resource(Overview, '/overview/<string:offset>')
api.add_resource(Visualize, '/overview_visualize')


if __name__ == '__main__':
    app.run()
