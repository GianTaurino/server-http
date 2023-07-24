# HTTP API realized with FastAPI and uvicorn
#
# Terminal command:
#   uvicorn main:app --reload --host "192.168.1.15"
# close with ctrl + C

from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB
import uvicorn

app = FastAPI()

class Danger(BaseModel):
    risk_uuid: str
    team_id: int
    date: str

# Define database file
db = TinyDB('db.json')

@app.get('/')
def get():
    return "Hello world"

@app.post('/registerDanger', status_code=201) # 201 created
def add_danger(danger: Danger):
    # Create dictionary
    new_danger = {
        'risk_id': danger.risk_uuid,
        'team_id': danger.team_id,
        'date': danger.date
    }
    # Add danger in database
    db.insert(new_danger)

    return new_danger

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
