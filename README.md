# Single-user sync server for Treelist

## Install
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`

## Configure
- Create `secret.py`
- Here’s an example content:
```
secret_path = 'asdf'
port = 3000
```

## Run
- `python treelist_single_user_server.py`

## Usage from a client
This server persists a single, over-writeable json object. Configure the secret path in secret.py, and after that the json object can be POST to the secret path and read from the same place.

### Example
`secret.py`:
```
secret_path = 'asdf'
port = 3000
```

Write:

`curl -X POST -H 'Content-Type: application/json -d '{"test": 123}' http://localhost:3000/asdf`

Write from file `data.json`:

`curl -X POST -H 'Content-Type: application/json -d @data.json http://localhost:3000/asdf`

Read:

`curl http://localhost:3000/asdf`
