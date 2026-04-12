from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class Message:
    id: str
    channel_id: str
    role: str
    content: str
    timestamp:str
    author:Optional[str] = None
    author_id:Optional[str] = None
    type: str = "Text"
