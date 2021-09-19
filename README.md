# FastAPI HTML TailwindCSS Markdown Blog Template

This template was created using [FastAPI](https://github.com/tiangolo/fastapi) and [TailwindCSS](https://tailwindcss.com) to display [Markdown](https://daringfireball.net/projects/markdown/) content for a blog.  

# With some help from:

[Tailwind Toolbox](https://github.com/tailwindtoolbox/Minimal-Blog) for the navigation bar.  
[Shinichi Okada](https://github.com/shinokada/fastapi-web-starter) for a template to learn from.  

## Get Started

Clone repo.  
Create virtual environment.  
pip install -r requirements.txt 

Run the program  
python3 run.py  

Launch a browser and navigate to the home page  
Browse to localhost:8000  

This will run the environment with reload enabled on port 8000. Ctrl+C to exit.  

## Customize template

Add images for the site to app/static/img  
Add or modify css for the site by adding or modifying the files in app/static/img  
Add javascript for the site to app/static/js  

Update Title between {% block title %} {% endblock %} in app/templates/main.html and app/templates/post.html  

### Add a post

Add markdown file to app/posts  
Add an entry in app/main/blog.md for the post  
Update app/blog.py with a new route including the URI of your new post that is referenced by the entry in app/main/blog.md  

## References

https://fastapi.tiangolo.com/  
[Tailwind Typography](https://github.com/tailwindlabs/tailwindcss-typography)  
[Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)  
[Python-markdown](https://github.com/Python-Markdown/markdown)  
A python module for converting Markdown to HTML  



