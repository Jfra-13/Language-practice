from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uid4

app = FastAPI()

posts = []

class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime] = None 
    published: bool = False
    
@app.get("/")
def root():
    return {
        "Message": "Server Online"
    }
    
@app.get("/posts")
def get_post():
    return posts

@app.post("/posts")
def save_post(post: Post):
    post.id = str(uid4())
    posts.append(post)
    return posts[-1]

@app.get("/posts/{post_id}")
def get_post(post_id: str):
    for post in posts:
        if post.id == post_id:
            return post 
        
    raise HTTPException (
        status_code=404,
        detail="Id not Found"
    )

@app.delete("/post/{post_id}")
def delete_post(post_id: str):
    for i, post in enumerate(posts):
        if post.id == post_id:
            posts.pop(i)
            return {
                "Message": "Post has been deleted successfully"
            }
    raise HTTPException (
        status_code=404,
        detail="Id not Found"
    )
    
@app.put("/posts/{post_id}")
def update_post(post_id: str, new_post: Post):
    for index, post in enumerate(posts):
        if post.id == post_id:
            posts[index].title = new_post.title
            posts[index].content = new_post.content
            posts[index].author = new_post.author
            return {
                "Message": "Post has been updated successfully"
            }
            
    raise HTTPException (
        status_code=404,
        detail="Id not Found"
    )