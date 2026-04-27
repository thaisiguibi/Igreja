from repository import posts as post_repository
from repository import users as user_repository
from fastapi import HTTPException

def get_post(post_id):
    post = post_repository.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


def create_post(post, user_id):
    post_id = post_repository.create_post(
            post.title,
            post.content,
            user_id
            )
    return post_repository.get_post(post_id)


def delete_post(post_id, user_id):
    post = post_repository.get_post_raw(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post ["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Not Allowed")

    post = post_repository.delete_post(post_id)

    return True

def update_post(post_id, title, content, user_id):
    post  = post_repository.get_post_raw(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Not Allowed")

    post_repository.update_post(
            post_id,
            title,
            content
            )

    return post_repository.get_post(post_id)

def list_posts(limit, offset, title, order):
    posts = post_repository.get_posts(limit, offset, title, order)
    total = post_repository.count_posts(title)

    return posts, total
