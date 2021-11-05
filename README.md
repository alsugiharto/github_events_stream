# Readme of 

Github event streamer

## Assumptions
A few assumptions made if you want to run this solution:
- You have a conda installed for environtment management: https://conda.io/projects/conda/en/latest/index.html
- You have git installed
- There is no limit in using the GitHub API requests (there is)
- You have no python virtual environtment named github_event_streamer yet

## How to run the solution

Clone the code from GitHub:
```bash
git clone https://github.com/alsugiharto/github_events_stream
cd github_events_stream
```

Create a new python virtual environtment and install all the dependencies in it
```bash
conda env create -f environtment.yml
```

Activate the new environtment
```bash
conda activate github_event_streamer
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

## API Endpoints

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

## Files

- `flask_restful`: Folder of the flask API framework.

- `C4 Diagram`: Folder of C4 Diagram Documentation

- `api.py`: The RESTful API app. Run this app to be able to make the API request.
 
- `github_event_streamer.py`: The script that streams the GitHub events saving important data into events.csv.
 
- `overview_visualisation.py`: The script that updates the overview.png file to plot a bar chart.
 
- `events.csv`: The CSV file consist of all the events recorded by the streaming script. The file already consists of some records for testing purposes. The file has 4 columns (from left to right): Event ID, Event Type, Date, Repository ID, Repository Name.

- `overview.png`: The image file of a bar chart of the number of events of each event recorded in the events.csv in the last 1 day.

- `environtment.yml`: List all the environtment dependencies
