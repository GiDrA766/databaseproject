from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    ForeignKey,
    DateTime,
    CheckConstraint,
)

BASE = declarative_base()
