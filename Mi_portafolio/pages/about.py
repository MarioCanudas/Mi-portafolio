import reflex as rx
from Mi_portafolio.components.layout import layout, back_link
from Mi_portafolio.backend.state import PortfolioState


def about() -> rx.Component:
    return layout(
        rx.vstack(
            rx.box(
                rx.markdown(PortfolioState.about_md),
                width="100%",
                text_align="left",
            ),
            back_link(),
            align_items="start",
            width="100%",
            class_name="animate-child-stagger",
        )
    )
