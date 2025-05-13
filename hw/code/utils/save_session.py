import json

def write_session_to_file(cookies, local_storage, filename='session.json'):
    with open(filename, 'w') as f:
        json.dump({'cookies': cookies, 'local_storage': local_storage}, f)

def read_session_from_file(filename='session.json'):
    try:
        with open(filename, 'r') as f:
            session = json.load(f)
            return {
                'cookie': session['cookies'],
                'local_storage': session['local_storage']
            }
    except FileNotFoundError:
        return None
