from dataclasses import dataclass, field
from typing import Optional
import datetime
from enum import Enum

class MsgType(Enum):
    USER_TEXT = "text"
    MODEL_TEXT = "model_text"
    FUNC_CALL = "func_call"
    FUNC_RESP = "func_response"

@dataclass
class Message:
    id: str
    channel_id: str
    role: str
    content: str
    timestamp:str
    author:Optional[str] = None
    author_id:Optional[str] = None
    message_type: MsgType = MsgType.USER_TEXT
    metadata: dict = field(default_factory=dict)
