from app import app
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    with open("app/main/home.md", "r", encoding="utf-8") as md:
        text = md.read()
    title = "Home"
    return templates.TemplateResponse("/main.html", {"request": request, "title": title, "content": markdown.markdown(text)})


@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    with open("app/main/blog.md", "r", encoding="utf-8") as md:
        text = md.read()
    title = "Blog"
    return templates.TemplateResponse("/main.html", {"request": request, "title": title, "content": markdown.markdown(text)})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    with open("app/main/about.md", "r", encoding="utf-8") as md:
        text = md.read()
    title = "About"
    return templates.TemplateResponse("/main.html", {"request": request, "title": title, "content": markdown.markdown(text)})


@app.get("/blog/post", response_class=HTMLResponse)
async def post(request: Request):
    with open("app/posts/post.md", "r", encoding="utf-8") as md:
        text = md.read()
    title = "Post"
    return templates.TemplateResponse("/post.html", {"request": request, "title": title, "content": markdown.markdown(text)})


@app.get("/blog/anotherpost", response_class=HTMLResponse)
async def anotherpost(request: Request):
    with open("app/posts/anotherpost.md", "r", encoding="utf-8") as md:
        text = md.read()
    title = "Another Post"
    return templates.TemplateResponse("/post.html", {"request": request, "title": title, "content": markdown.markdown(text)})