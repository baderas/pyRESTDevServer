# pyRESTDevServer
A small python server that helps developing/debugging a REST client. It simply prints out every received POST request.

## Requirements
* Python3
* Flask
  * install with pip: `pip install flask`
  * or use your distributions package, e.g. Debian package: `sudo apt-get install python-flask`
  
## Usage
* Start Server: `./pyRESTDevServer.py`
* Test with curl: `curl -i -H "Content-Type: application/json" -X POST -d @test.json http://localhost:5000/write`