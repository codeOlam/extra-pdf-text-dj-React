![Django Logo](dj_react.png)

## About

Django is a web-framework written in Python and runs the backend for many of the internet's most popular websites. This is a multi-user type auth app, it is built ontop of Django 3.2.8 and Django Rest Framework 3.12.4

This app features the following:

-- Allow user upload document and authomatically extract text from the pdf.

## Technology and Requirements

1. Django==3.2.8
2. Python3
3. djangorestframework==3.12.4
4. Reactjs==^17.0.2
5. Typescript==^4.1.2
6. axios==^0.24.0
7. pymupdf==1.19.2 (for the text extraction)

## Installations

1. [installing Python3](https://www.python.org/downloads/)
2. [installing Django 3.x](https://docs.djangoproject.com/en/3.2/topics/install/)
3. [installing Django Rest Framework](https://www.django-rest-framework.org/#installation)
4. [installing Virtualenv](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
5. installing requirements from requirements.txt. After activating vitualenv run:

`(venv)path/to/app/src$ pip install -r requirements.txt `

6. [psycopg2](http://initd.org/psycopg/docs/install.html)
7. set up an env file with:

`SECRET_KEY={your secret key value} `

## Run App

1. After cloning this repo, make sure your virtualenv is ativated and change your path to $app root/.

`(venv)path/to/app$ `

2. install packages required by running

   `(venv)path/to/app$ pip install -r requirements.txt `

3. change director to src/ make sure you are in the same directory where manage.py is then run

`(venv)path/to/app/src$ python manage.py makemigrations `

4. The migrate the app
   `(venv)path/to/app/src$ python manage.py migrate `

5. To run the development server
   `(venv)path/to/app/src$ python manage.py runserver `

6. install frontend react dependencies using yarn you can also use npx
   `path/to/Frontend/src$ yarn install`

7. to start frontend react server
   `path/to/Frontend/src$ yarn start`

## Recommendations

This App is not designed to be used full in deployement. You are free to make any adjustments to it and include in you project

## Resources

1. [Django 3.x Doc](https://docs.djangoproject.com/en/3.2/)
2. [DRF 3.X](https://www.django-rest-framework.org/)
3. [My Previous Repo](https://github.com/codeOlam/dj-multi-user-auth)
4. [axios](https://www.npmjs.com/package/axios)
5. [Reactjs](https://reactjs.org/docs/getting-started.html)
6. [Typescript](https://www.typescriptlang.org/docs/)
7. [pymupdf](https://github.com/pymupdf/PyMuPDF)

### Other Resources

1. [Customizing authentication in Django](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/)
