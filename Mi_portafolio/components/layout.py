import reflex as rx

def back_link(text="<- back", url="/") -> rx.Component:
    return rx.box(
        rx.link(text, href=url, color="var(--gray-9)", _hover={"color": "var(--gray-12)"}, text_decoration="none"),
        margin_top="3em",
        width="100%",
        text_align="left"
    )

def footer() -> rx.Component:
    from Mi_portafolio.backend.state import PortfolioState
    return rx.box(
        rx.center(
            rx.hstack(
                rx.link("email", href=f"mailto:{PortfolioState.email}", color="var(--gray-9)", _hover={"color": "var(--gray-12)"}, text_decoration="none"),
                rx.text("·", color="var(--gray-5)"),
                rx.link("github", href=PortfolioState.github, is_external=True, color="var(--gray-9)", _hover={"color": "var(--gray-12)"}, text_decoration="none"),
                rx.text("·", color="var(--gray-5)"),
                rx.link("linkedin", href=PortfolioState.linkedin, is_external=True, color="var(--gray-9)", _hover={"color": "var(--gray-12)"}, text_decoration="none"),
                spacing="4",
            ),
            width="100%",
            height="100%",
        ),
        position="fixed",
        bottom="0",
        left="0",
        width="100%",
        height="120px",
        bg="var(--gray-1)",
        border_top="1px solid var(--gray-3)",
        z_index="10",
        class_name="animate-fade-in"
    )

def layout(*children, max_width="600px", **props) -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="top-right", margin="4", color="var(--gray-9)", class_name="animate-fade-in"),
        rx.center(
            rx.vstack(
                *children,
                width="100%",
                max_width=max_width,
                align_items="start",
                spacing="6",
                padding_x="4",
            ),
            min_height="100vh",
            padding_top="10em",
            padding_bottom="120px",
            align_items="start"
        ),
        footer(),
        font_family='"Geist Mono", monospace',
        text_transform="lowercase",
        bg="var(--gray-1)",
        color="var(--gray-12)",
        transition="background-color 0.2s ease",
        class_name="animate-fade-in",
        **props
    )
