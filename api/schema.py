import strawberry
from typing import List
from .models import Post
from .types import PostType

# Query (GET)


@strawberry.type
class Query:
    @strawberry.field
    def get_post(self, title: str = None) -> List[PostType]:
        if title:
            post = Post.objects.filter(title=title)
            return post
        return Post.objects.all()

# Mutation (Create, Update, Patch, Delete)


@strawberry.type
class Mutation:
    @strawberry.field
    def create_post(self, title: str, author: str, message: str) -> PostType:
        post = Post(title=title, author=author, message=message)
        post.save()
        return post

    @strawberry.field
    def update_post(self, id: int, title: str, author: str, message: str) -> PostType:
        post = Post.objects.get(id=id)
        post.title = title
        post.author = author
        post.message = message
        post.save()
        return post

# Define Schema


schema = strawberry.Schema(query=Query, mutation=Mutation)
