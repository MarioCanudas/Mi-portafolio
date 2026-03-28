import reflex as rx
from Mi_portafolio.components.layout import layout
from Mi_portafolio.backend.state import PortfolioState

def index() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading(PortfolioState.name, font_size="2.5em", font_weight="bold", color="var(--gray-12)"),
            rx.text(PortfolioState.role, font_size="1.1em", color="var(--gray-9)", margin_bottom="3em"),
            rx.vstack(
                rx.link(rx.text("projects", _hover={"color": "var(--gray-12)"}), href="/projects", color="var(--gray-10)", text_decoration="none", font_size="1.2em"),
                rx.link(rx.text("about", _hover={"color": "var(--gray-12)"}), href="/about", color="var(--gray-10)", text_decoration="none", font_size="1.2em"),
                rx.link(rx.text("blog", _hover={"color": "var(--gray-12)"}), href="/blog", color="var(--gray-10)", text_decoration="none", font_size="1.2em"),
                align_items="start",
                spacing="4",
                class_name="animate-child-stagger"
            ),
            align_items="start",
            width="100%",
            class_name="animate-child-stagger"
        ),
        max_width="280px"
    )
