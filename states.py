import os

#Ways to Create the State

#1) typed DICT (most commmon approch)
from typing import TypedDict
class State(TypedDict):
    topic: str
    summary : str
    score : int
    

#2)pydentic approch
#it is good at data validation and checking at run time

from pydantic import BaseModel , field_validator

class State(BaseModel):
    topic: str
    summary : str =""
    score : int
    
    @field_validator
    def score_positve(cls, val):
        if val < 0:
            return ValueError("Score must be positive")

#3) python dataclasses
#standart python dataclasses but it used rarely

from dataclasses import dataclass ,field

@dataclass
class State:
    topic: str
    summary : str =""
    score : int
    messages : list = field(default_factory=list)
    
#4) using langgraph

from langgraph.graph import MessagesState

class State(MessagesState):
    #messages filed is already include with add_message reducer
    #just add your extra field
    
    user_name: str
    language : str
 