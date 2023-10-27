import datetime
import json
from typing import List

from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, Float,
                        ForeignKey, Integer, MetaData, Sequence, String, Table,
                        Text, func)
                        
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Base = declarative_base(metadata=MetaData(schema='gold_list_method'))
Base = declarative_base()
metadata = Base.metadata


class SentenceModel(Base):
    __tablename__  = 'sentence'
    # __table_args__ = {"schema": "gold_list_method"}

    id               = Column(Integer, primary_key=True)
    created_at       = Column(Date, default=func.current_date())
    foreign_language = Column(String)
    mother_tongue    = Column(String)
    foreign_idiom    = Column(String)
    mother_idiom     = Column(String)