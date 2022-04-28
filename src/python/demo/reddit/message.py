from grongier.pex import Message

from dataclasses import dataclass

from obj import PostClass

@dataclass
class PostMessage(Message):

    post:PostClass = None
    to_email_address:str = None
    found:str = None

@dataclass
class MyRequest(Message):

    ma_string:str = None

@dataclass
class MyMessage(Message):
    toto:str = None