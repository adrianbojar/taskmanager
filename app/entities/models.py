
from datetime import datetime
from enum import Enum
from sqlalchemy import (
    Column, Integer, String, Text, DateTime,
    ForeignKey, Enum as SqlEnum, Table
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# --- Enumy ---

class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    BLOCKED = "Blocked"

class TaskPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

# --- Tabela pośrednia (User <-> Team) ---

user_team_table = Table(
    'user_team', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('team_id', Integer, ForeignKey('teams.id'))
)

# --- Modele główne ---

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="member")  # np. admin / member

    teams = relationship("Team", secondary=user_team_table, back_populates="members")
    tasks_assigned = relationship("Task", back_populates="assignee", foreign_keys="Task.assignee_id")
    tasks_created = relationship("Task", back_populates="creator", foreign_keys="Task.creator_id")

    def __repr__(self):
        return f"<User(name={self.name})>"


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text)

    members = relationship("User", secondary=user_team_table, back_populates="teams")
    projects = relationship("Project", back_populates="team")

    def __repr__(self):
        return f"<Team(name={self.name})>"


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship("Team", back_populates="projects")
    tasks = relationship("Task", back_populates="project")

    def __repr__(self):
        return f"<Project(name={self.name})>"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    description = Column(Text)
    status = Column(SqlEnum(TaskStatus), default=TaskStatus.TODO)
    priority = Column(SqlEnum(TaskPriority), default=TaskPriority.MEDIUM)
    created_at = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)

    project_id = Column(Integer, ForeignKey('projects.id'))
    creator_id = Column(Integer, ForeignKey('users.id'))
    assignee_id = Column(Integer, ForeignKey('users.id'))

    project = relationship("Project", back_populates="tasks")
    creator = relationship("User", back_populates="tasks_created", foreign_keys=[creator_id])
    assignee = relationship("User", back_populates="tasks_assigned", foreign_keys=[assignee_id])
    comments = relationship("Comment", back_populates="task")

    def __repr__(self):
        return f"<Task(title={self.title}, status={self.status.name})>"


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    task_id = Column(Integer, ForeignKey('tasks.id'))
    author_id = Column(Integer, ForeignKey('users.id'))

    task = relationship("Task", back_populates="comments")
    author = relationship("User")

    def __repr__(self):
        return f"<Comment(by={self.author_id}, task={self.task_id})>"
