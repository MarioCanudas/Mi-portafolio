import reflex as rx
from Mi_portafolio.components.layout import layout, back_link
from Mi_portafolio.backend.state import PortfolioState

def about() -> rx.Component:
    return layout(
        rx.vstack(
            rx.box(
                rx.markdown(
                    PortfolioState.about_md,
                    component_map={
                        "h1": lambda *args, **kwargs: rx.heading(*args, **kwargs, size="5", margin_top="4", margin_bottom="2"),
                        "h2": lambda *args, **kwargs: rx.heading(*args, **kwargs, size="4", margin_top="4", margin_bottom="2"),
                        "h3": lambda *args, **kwargs: rx.heading(*args, **kwargs, size="3", margin_top="4", margin_bottom="2"),
                        "p": lambda *args, **kwargs: rx.text(*args, **kwargs, margin_bottom="4", line_height="1.6"),
                        "a": lambda *args, **kwargs: rx.link(*args, **kwargs, color="var(--gray-11)", text_decoration="underline"),
                    }
                ),
                width="100%",
                text_align="left"
            ),
            back_link(),
            align_items="start",
            width="100%",
            class_name="animate-child-stagger"
        )
    )
