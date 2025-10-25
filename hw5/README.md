

### Build docker image
```
docker build --platform linux/amd64 -t predict-service .
```

### Run the container:
```
docker run -it --rm --platform linux/amd64 -p 9696:9696 predict-service
```

### Get prediction from API
```
python predict_api.py 
```