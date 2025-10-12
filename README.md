# Watchlist

Example application for flask tutorial "[Flask 入门教程 / Flask for Beginners](https://helloflask.com/book/3)".

Demo: http://watchlist.helloflask.com

![Screenshot](demo.png)


## Installation

Clone the repository:

```
$ git clone https://github.com/helloflask/watchlist.git
$ cd watchlist
```

Create & active virtual enviroment and install dependencies:

```
$ python3 -m venv .venv  # use `python ...` on Windows
$ source .venv/bin/activate  # use `.venv\Scripts\activate` on Windows
(.venv) $ pip install -r requirements.txt
```

Generate fake data then run the app:

```
(.venv) $ flask forge
(.venv) $ flask run
* Running on http://127.0.0.1:5000/
```

Test account:

- username: `admin`
- password: `helloflask`


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
