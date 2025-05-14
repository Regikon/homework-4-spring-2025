import json
from typing import Optional, Dict, List, TypedDict

class Session(TypedDict):
    cookie: Optional[List[Dict[str, str]]]
    local_storage: Optional[Dict[str, str]]

def write_session_to_file(session: Session, filename='session.json'):
    with open(filename, 'w') as f:
        json.dump(
            {
                'cookie': session['cookie'],
                'local_storage': session['local_storage']
            }, f
        )

def read_session_from_file(filename='session.json') -> Optional[Session]:
    try:
        with open(filename, 'r') as f:
            session = json.load(f)
            return Session(
                cookie=session['cookie'],
                local_storage=session['local_storage']
            )
    except FileNotFoundError:
        return None
