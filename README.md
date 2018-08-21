[![Coverage Status](https://coveralls.io/repos/github/oxenprogrammer/StackOverflow-lite/badge.svg?branch=develop)](https://coveralls.io/github/oxenprogrammer/StackOverflow-lite?branch=develop)
[![Build Status](https://travis-ci.org/oxenprogrammer/StackOverflow-lite.svg?branch=develop)](https://travis-ci.org/oxenprogrammer/StackOverflow-lite)
[![Maintainability](https://codeclimate.com/github/oxenprogrammer/StackOverflow-lite)](https://codeclimate.com/github/oxenprogrammer/StackOverflow-lite)

# StackOverflow-lite
Find the Site here [GitHub Pages](https://oxenprogrammer.github.io/StackOverflow-lite/UI/)

# StackOverflow-lite
Project Overview
StackOverflow-lite is a platform where people can ask questions and provide answers.

### Features
```
- Users can create an account and log in.
- Users can post questions.
- Users can delete the questions they post.
- Users can post answers.
- Users can view the answers to questions.
- Users can accept an answer out of all the answers to his/her question as the preferred answer. 
```
## Main Branches
* **Master** - production ready project
* **Feature** - Frontend Features
* **Develop** - Api endpoints code and tests

## Getting Started

Clone the project into your local machine,
``` git clone https://github.com/oxenprogrammer/StackOverflow-lite.git```
change directory StackOverflow-lite checkout develop.
To see all branches, ```git branch -a``` shows both local and remote branches

### Prerequisites

- pip
- python 3.6


### Installing
```
- download python 3.6+ from https://www.python.org/downloads/
- install pip, follow this instructions https://www.tecmint.com/install-pip-in-linux/
- create a virtual env and activate it https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b
- Navigate to the project folder in the terminal and run ```pip install -r requirements.txt```
```

## Running the tests
Tests are written using unittest
```pytest tests/tests.py -v```

### What the tests do

They tests test the questions and answers api endpoints

```
- ask_question(POST)
- get_all_questions(GET)
- get_specific_question(GET)
- post_answer(POST)
```

## Deployment
```
A copy is deployed at heroku
https://andela-stackoverflow-lite.herokuapp.com
```

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pure Flask Rest] - Restful Application

## Contributing

Please email me at emmy1000okello@gmail.com

## Versioning

This is v1

## Authors

* **emanuel okello**


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Dzone](https://dzone.com/)
* Youtube
* StackOverflow.com
