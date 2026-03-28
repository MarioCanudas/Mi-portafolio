import json
import os
import glob
import frontmatter
import reflex as rx

CONTENT_FILE = "content.json"
BLOG_DIR = "blog_posts"
ABOUT_FILE = "about.md"

def load_content():
    if os.path.exists(CONTENT_FILE):
        with open(CONTENT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def load_blog_posts():
    posts = []
    if os.path.exists(BLOG_DIR):
        for filepath in glob.glob(f"{BLOG_DIR}/*.md"):
            with open(filepath, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)
                filename = os.path.basename(filepath)
                slug = filename.replace(".md", "")
                
                posts.append({
                    "slug": slug,
                    "title": post.metadata.get("title", slug),
                    "date": str(post.metadata.get("date", "")),
                    "description": post.metadata.get("description", ""),
                    "content": post.content
                })
    posts.sort(key=lambda x: x.get("date", ""), reverse=True)
    return posts

def load_about():
    if os.path.exists(ABOUT_FILE):
        with open(ABOUT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return "about.md no encontrado"

class PortfolioState(rx.State):
    content: dict = load_content()
    posts: list[dict] = load_blog_posts()
    about_md: str = load_about()
    
    @rx.var
    def name(self) -> str:
        return self.content.get("name", "Name")
        
    @rx.var
    def role(self) -> str:
        return self.content.get("role", "Role")
        
    @rx.var
    def email(self) -> str:
        return self.content.get("email", "")
        
    @rx.var
    def github(self) -> str:
        return self.content.get("github", "")
        
    @rx.var
    def linkedin(self) -> str:
        return self.content.get("linkedin", "")
        
    @rx.var
    def projects(self) -> list[dict]:
        return self.content.get("projects", [])
        
    @rx.var
    def font_family(self) -> str:
        return self.content.get("fonts", {}).get("primary", "Inter, system-ui, sans-serif")
        
    @rx.var
    def bg_color(self) -> str:
        return self.content.get("colors", {}).get("background", "var(--gray-1)")
        
    @rx.var
    def text_color(self) -> str:
        return self.content.get("colors", {}).get("text", "var(--gray-12)")
