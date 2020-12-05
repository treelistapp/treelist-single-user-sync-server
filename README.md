# Single-user sync server for Treelist
This server persists a single, over-writeable json object. Configure the secret path in secret.py, and after that the json object can be POST to the secret path and GET from there as well. No history is preserved and all data must be written in every request.

## Install
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`

## Configure
- Create `secret.py`
- Here’s an example content:
```
secret_path = '/asdf'
port = 3000
```
- `secret_path` should not be empty as the root path has other functionality.

### Nginx
Add this to `server` block to enable big file upload:

`client_max_body_size 100M;`

## Run
- `python treelist_single_user_server.py`

## Example usage with curl

Write:

`curl -X POST -H 'Content-Type: application/json' -d '{"test": 123}' http://localhost:3000/asdf`

Write from file `data.json`:

`curl -X POST -H 'Content-Type: application/json' -d @data.json http://localhost:3000/asdf`

Read:

`curl http://localhost:3000/asdf`
