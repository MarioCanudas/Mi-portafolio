import reflex as rx
from .views.header import header
from .views.about_me import about_me
from .views.projects import projects

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        
        rx.color_mode.button(position="bottom-right"),
        
        header(),
        about_me(),
        rx.divider(margin= '2em'),
        projects(),

    )

app = rx.App()
app.add_page(index)