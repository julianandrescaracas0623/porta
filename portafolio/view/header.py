import reflex as rx 
from portafolio.components.heading import heading
from portafolio.style.styles import Size
from portafolio.components.media import media
from portafolio.data import Data 

def header(data: Data) -> rx.Component:
    return rx.hstack(
        rx.avatar(
                    src=data.avatar,
                    size=Size.BIG.value
                ),
        rx.vstack(
            heading(data.name, True),
            heading(data.title),
            rx.text(
                rx.icon("map-pin"),
                data.location,
                display="inherit"
            ),
            media(data.media),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    )