import reflex as rx
from Mi_portafolio.components.layout import layout, back_link
from Mi_portafolio.backend.state import PortfolioState


def project_card(project: dict) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.image(
                    src=project["image"],
                    width="100%",
                    height="150px",
                    object_fit="cover",
                ),
                rx.box(
                    rx.heading(project["title"], size="4", margin_bottom="2"),
                    rx.text(project["description"], size="2", color="var(--gray-11)"),
                    padding="16px",
                ),
            ),
            border="1px solid var(--gray-4)",
            border_radius="8px",
            overflow="hidden",
            _hover={"border_color": "var(--gray-8)", "bg": "var(--gray-2)"},
            transition="all 0.2s ease",
        ),
        href=project["url"],
        is_external=True,
        text_decoration="none",
    )


def projects() -> rx.Component:
    return layout(
        rx.heading("projects", size="6"),
        rx.grid(
            rx.foreach(PortfolioState.projects, project_card),
            columns="2",
            spacing="4",
            width="100%",
        ),
        back_link(),
    )
