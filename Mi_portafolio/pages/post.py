import reflex as rx
from Mi_portafolio.components.layout import layout, back_link
from Mi_portafolio.backend.state import PortfolioState


class PostState(PortfolioState):
    @rx.var
    def current_post(self) -> dict:
        slug = self.router.page.params.get("slug", "")
        for p in self.posts:
            if p["slug"] == slug:
                return p
        return {
            "title": "post no encontrado",
            "content": "este post no existe.",
            "date": "",
        }


def post() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading(
                PostState.current_post["title"],
                size="6",
                margin_bottom="2",
                color="var(--gray-12)",
            ),
            rx.text(
                PostState.current_post["date"], color="var(--gray-9)", margin_bottom="4"
            ),
            rx.box(
                rx.markdown(
                    PostState.current_post["content"],
                    component_map={
                        "h1": lambda *args, **kwargs: rx.heading(
                            *args, **kwargs, size="5", margin_top="4", margin_bottom="2"
                        ),
                        "h2": lambda *args, **kwargs: rx.heading(
                            *args, **kwargs, size="4", margin_top="4", margin_bottom="2"
                        ),
                        "h3": lambda *args, **kwargs: rx.heading(
                            *args, **kwargs, size="3", margin_top="4", margin_bottom="2"
                        ),
                        "p": lambda *args, **kwargs: rx.text(
                            *args, **kwargs, margin_bottom="4", line_height="1.6"
                        ),
                        "a": lambda *args, **kwargs: rx.link(
                            *args,
                            **kwargs,
                            color="var(--gray-11)",
                            text_decoration="underline",
                        ),
                    },
                ),
                width="100%",
                text_align="left",
            ),
            back_link("<- back to blog", "/blog"),
            align_items="start",
            width="100%",
            class_name="animate-child-stagger",
        )
    )
