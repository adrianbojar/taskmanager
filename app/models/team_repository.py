from app.entities.models import Team
from db.database import SessionLocal

def create_team(team_data):
    db = SessionLocal()
    team = Team(**team_data)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_team_by_id(team_id):
    db = SessionLocal()
    return db.query(Team).filter(Team.id == team_id).first()

def get_all_teams():
    db = SessionLocal()
    return db.query(Team).all()

def update_team(team_id, new_data):
    db = SessionLocal()
    team = db.query(Team).filter(Team.id == team_id).first()
    for key, value in new_data.items():
        setattr(team, key, value)
    db.commit()
    return team

def delete_team(team_id):
    db = SessionLocal()
    team = db.query(Team).filter(Team.id == team_id).first()
    db.delete(team)
    db.commit()
