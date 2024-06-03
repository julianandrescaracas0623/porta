import reflex as rx 
from portafolio.style.styles import Size,EmSize
from portafolio.components.media import media
from portafolio.data import Media

def footer (data:Media)-> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(data),
        spacing=Size.SMALL.value
    )