```
docker build -t connor/lp-jupyter jupyter/.

docker run -d --rm --name liveproject -p 8888:8888 --mount type=bind,source="C:/Users/clrho/Create a Data Platform for Real-Time Anomaly Detection Walkthrough/jupyter/",target=/src connor/lp-jupyter 

docker run -d --rm --name liveproject -p 8888:8888 -v //f/Repositories/Anomaly-Detection/jupyter/data/:/src connor/lp-jupyter 
```
