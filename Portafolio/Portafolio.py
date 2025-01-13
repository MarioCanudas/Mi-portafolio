import reflex as rx
from .views.header import header
from .views.about_me import about_me
from .views.projects import projects
from .constants import DIVIDER_MARGIN
from .styles import Color

style = {
    'background_color' : Color.BACKGROUND.value,
    'font_family' : "'Montserrat', sans-serif"
} 

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        
        header(),
        rx.box(about_me(), margin= DIVIDER_MARGIN),
        rx.divider(),
        rx.box(projects(), margin= DIVIDER_MARGIN),
        width="100%",
        height= '100%'
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap",
    ],
    
    style= style
)

app.add_page(index)