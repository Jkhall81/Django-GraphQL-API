import strawberry
from typing import List
from . import models


@strawberry.django.type(models.Post)
class PostType:
    id: int
    title: str
    author: str
    message: str
