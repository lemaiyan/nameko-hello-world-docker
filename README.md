# Intro

This applications showcases the core functionality of Nameko(RPC & http). 

## RPC

To run the application make sure you have `docker` and `docker-compose` installed then follow 
the steps below

* Run `docker-compose up` to start the service and wait for the app to start
* In another terminal  run the command `docker-compose run  hello_service nameko shell --config config.yml` 
and run the following the shell that appears
```python
 n.rpc.greeting_service.hello(name='World')
```

You should get the response below

```bash
 'Hello World'
```


## HTTP
Paste the Url below in a browser http://localhost:5000/greeting/World and you should 
getting a JSON response below

```json
{
  greeting: "Hello World"
}
```

## Tests
To run the tests run the command `docker-compose run hello_service python tests.py`