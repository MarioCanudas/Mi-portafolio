import reflex as rx
from Mi_portafolio.components.layout import layout, back_link
from Mi_portafolio.backend.state import PortfolioState


class PostState(PortfolioState):
    @rx.var
    def current_post(self) -> dict:
        path = self.router.url.path or ""
        slug = path.split("/")[-1] if path else ""

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
