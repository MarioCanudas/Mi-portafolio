import reflex as rx

from Mi_portafolio.pages.index import index
from Mi_portafolio.pages.about import about
from Mi_portafolio.pages.projects import projects
from Mi_portafolio.pages.blog import blog
from Mi_portafolio.pages.post import post

theme = rx.theme(
    appearance="inherit",
    has_background=False,
    radius="none",
    accent_color="gray",
    gray_color="slate",
)

app = rx.App(
    theme=theme,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Geist+Mono:wght@300;400;500;600&display=swap",
        "/styles.css",
    ],
)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(projects, route="/projects")
app.add_page(blog, route="/blog")
app.add_page(post, route="/blog/[slug]")
