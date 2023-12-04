### train the model
```
poetry run rasa train
```

### start up the application
```
poetry run rasa run actions --cors "*" --debug
```
```
poetry run rasa run --model models/<insert model name.tar.gz> --enable-api --cors "*" --endpoints endpoints.yml --debug
```