# Readme of 

Github event streamer

## How to run the solution

Install all the [Libraries to install](#libraries-to-install)

Clone the code from GitHub:

```bash
git clone https://github.com/alsugiharto/github_events_stream
```

Run the streamer script
```bash
python github_event_streamer.py
```

Run the overview visualization script
```bash
python overview_visualisation.py
```

Run the API app
```bash
python api.py
```

Try some API requests! in [The API Endpoints](#the-api-endpoints)

## The API Endpoints

#### Average Pull Request Time
Calculating the average time between pull requests for a repository. It is mandatory to give a repository ID as an input. Below is the example of a request asking for a repository id of "213547521". 
```bash
curl http://localhost:5000/averagepulltime/213547521
```

#### Overview using offset
Returning the total number of events grouped by the event type for a given offset. An offset is mandatory. The offset determines how much time we want to look back i.e., an offset of 10 means we count only the events which have been created in the last 10 minutes, for example:
```bash
curl http://localhost:5000/overview/10
```
        
#### Overview Bar Chart
Drawing a bar chart showing the number of events grouped by the event type in the last 1 day. No input is required.
```bash
curl http://localhost:5000/overview_visualize
```


## Assumptions

Assumptions made:
- There is no limit in using the GitHub API requests
- All the last versions of libraries and their dependencies used in this solution are installed

## Libraries to install
- git
- python 3
- CSV
- time
- JSON
- requests
- pandas
- DateTime
- io
- base64
- matplotlib
- flask-restful

## Files

- `flask_restful`: Folder of the flask API framework.

- `C4 Diagram`: Folder of C4 Diagram Documentation

- `api.py`: The RESTful API app. Run this app to be able to make the API request.
 
- `github_event_streamer.py`: The script that streams the GitHub events saving important data into events.csv.
 
- `overview_visualisation.py`: The script that updates the overview.png file to plot a bar chart.
 
- `events.csv`: The CSV file consist of all the events recorded by the streaming script. The file already consists of some records for testing purposes. The file has 4 columns (from left to right): Event ID, Event Type, Date, Repository ID, Repository Name.

- `overview.png`: The image file of a bar chart of the number of events of each event recorded in the events.csv in the last 1 day.