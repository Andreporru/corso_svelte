#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,Dict,Any

class DefaultResponse(BaseModel):
    data:Optional[Dict[str, Any]]= None
    error:Optional[Dict[str, Any]]= None

class Book(BaseModel):
    isbn:str
    title:str
    author:str

class BookUpdateRequest(BaseModel):
    title:Optional[str]=None
    author:Optional[str]=None


books=[]
app=FastAPI()

@app.get("/books/clear",response_model=DefaultResponse)
async def _book_clear():
    books.clear()
    return DefaultResponse(data={"ok":True})

@app.post("/books/add", response_model=DefaultResponse)
async def _book_add(book:Book):
    books.append(book.dict())
    return DefaultResponse(data=book.dict())

@app.get("/books/list", response_model=DefaultResponse)
async def _book_list():
    return DefaultResponse(data={"books":books})

@app.get("/books/{isbn}",response_model=DefaultResponse)
async def _book_get(isbn:str):
    for book in books:
        if book["isbn"]==isbn:
            return DefaultResponse(data=book)

    return DefaultResponse(
            error={
                "message":"Book not found",
                "code":1001,
                "isbn":isbn,
            }
        )

@app.delete("/books/del/{isbn}",response_model=DefaultResponse)
async def _book_del(isbn:str):
    for book in books:
        if book["isbn"]==isbn:
            books.remove(book)
            return DefaultResponse(data={"isbn":isbn})

    return DefaultResponse(
            error={
                "message":"Book not found",
                "code":1001,
                "isbn":isbn,
            }
        )

@app.patch("/books/update/{isbn}",response_model=DefaultResponse)
async def _book_update(isbn:str,data:BookUpdateRequest):
    title=data.title
    author=data.author
    
    for b in books:
        if b["isbn"]==isbn:
            if title:
                b["title"]=title
            if author:
                b["author"]=author

            return DefaultResponse(data=b)

    return DefaultResponse(
            error={
                "message":"Book not found",
                "code":1001,
                "isbn":isbn,
            }
        )
    
