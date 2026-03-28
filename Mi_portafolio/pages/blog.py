import reflex as rx
from Mi_portafolio.components.layout import layout, back_link
from Mi_portafolio.backend.state import PortfolioState

def post_item(post: dict) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(post["title"], color="var(--gray-12)", font_weight="bold"),
            rx.spacer(),
            rx.text(post["date"], color="var(--gray-9)", font_size="0.9em"),
            width="100%",
            padding_y="3",
            padding_x="2",
            border_bottom="1px dashed var(--gray-4)",
            _hover={"bg": "var(--gray-2)", "border_radius": "4px"},
            align_items="center"
        ),
        href=f"/blog/{post['slug']}",
        text_decoration="none",
        width="100%"
    )

def blog() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("blog", font_size="1.5em", font_weight="bold", color="var(--gray-12)", margin_bottom="1em"),
            rx.foreach(PortfolioState.posts, post_item),
            back_link(),
            align_items="start",
            width="100%",
            spacing="1",
        )
    )
