# Django ABLine API
This is a simple Django REST API for managing ABLine objects.

## Installation
### Clone the repository:
```
git clone https://github.com/<username>/<repository-name>.git
cd <repository-name>
```
### Install dependencies:
```
pip install -r requirements.txt
```

### Run migrations:
```
python manage.py migrate
```
### Start the server:
```
python manage.py runserver
```
## Usage
You can interact with the API through HTTP requests. The following endpoints are available:

### List ABLines
GET `/ablines/`
Returns a list of all ABLines.

Get ABLine Details

GET `/ablines/<id>/`
Returns the details of a single ABLine.

### Create ABLine
POST `/ablines/create/`
Creates a new ABLine.

### Update ABLine
POST `/ablines/<id>/update/`
Updates an existing ABLine.

### Delete ABLine
GET `/ablines/<id>/delete/`
Deletes an existing ABLine.

### Import ABLines
GET `/ablines/import/`
Imports ABLine data from an external API.