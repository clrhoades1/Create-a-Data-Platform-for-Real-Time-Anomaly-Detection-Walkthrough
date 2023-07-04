```
docker build -t connor/lp-jupyter jupyter/.

docker run -d --rm --name liveproject -p 8888:8888 --mount type=bind,source="C:/Users/clrho/Create a Data Platform for Real-Time Anomaly Detection Walkthrough/jupyter/",target=/src connor/lp-jupyter 

docker run -d --rm --name liveproject -p 8888:8888 -v //f/Repositories/Anomaly-Detection/jupyter/data/:/src connor/lp-jupyter 

docker run -d --rm --name liveservice -p 8000:8000 connor/lp-service 

docker-compose up
```

## Issues I had: 
* Having a space in my path used by Docker will result in Docker not seeing the file/folder. 
* Accessing my model outside of the service folder does not work (because of how Docker context works), I had to use docker-compose to get around it. 
* Getting the docker-compose stuff working 