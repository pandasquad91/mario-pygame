# mario-pygame
An entry for MFGG Fangame Jam 5

### Installation
This project is built with Python 3.7. It's recommended you create a virtual environment of Python 3.7 to install the project.

### Docker setup [Deprecated]

1) Install docker on your system
2) `docker build -t mario-pygame .` in the main directory.
3) `docker run -it --rm mario-pygame` to launch the application.

Note: This is not currently working with pygame.

### Local build
Install the requirements:
`pip install -r requirements.txt`

After installing the requirements, it's recommended to setup commit hooks:
`pre-commit install`

This will run each added or changed file with every commit through linters. If all goes well, you should see the following after a good commit:
```
black....................................................................Passed
Flake8...................................................................Passed
pylint_workouts..........................................................Passed
pylint_tests.............................................................Passed
pytest...................................................................Passed
```
If `black` detects necessary changes, it will update the file automatically! You'll have to restage and recommit the changes, though.

Finally, you can launch the main script:
`python src/main.py`

### Running unit tests
`python -m unittest discover -s tests` in the main directory. You can also use pytest: `pytest tests/`. They'll be run automatically with commit hooks if you have them installed.

# Disclaimer

Mario and all related assets are property of Nintendo. This fan game is made purely for the purposes of education and entertainment.