# Watchlist

Example application for flask tutorial "[Flask 入门教程](http://helloflask.com/tutorial)".

Demo: http://watchlist.helloflask.com

![Screenshot](http://helloflask.com/screenshots/watchlist.png)

## Installation

clone:
```
$ git clone https://github.com/greyli/watchlist.git
$ cd watchlist
```
create & active virtual enviroment then install dependencies:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

generate fake data then run:
```
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
