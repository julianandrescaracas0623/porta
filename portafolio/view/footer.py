import reflex as rx 
from portafolio.style.styles import Size,EmSize
from portafolio.components.media import media

def footer ()-> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(),
        spacing=Size.SMALL.value
    )