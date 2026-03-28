import reflex as rx

config = rx.Config(
    app_name="Mi_portafolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
