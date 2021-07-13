FROM python:3.8

WORKDIR /app

# Install project python dependencies
ADD ["Pipfile", "Pipfile.lock", "setup.py", "./"]
RUN pip install pipenv && pipenv --python 3.8 && pipenv install && pipenv --clear

ADD app app
RUN pipenv install && pipenv --clear

CMD ["python", "--version"]
