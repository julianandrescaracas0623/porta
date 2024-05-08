import reflex as rx 
from portafolio.components.heading import heading
from portafolio.style.styles import Size
from portafolio.components.media import media
def header()-> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.BIG.value),
        rx.vstack(
            heading("Nombre",True),
            heading("Habilidad Principal"),
            rx.text(
                rx.icon("map-pin"),
                "Localización",
                display="inherit"
            ),
            media(),
            spacing=Size.SMALL.value,
        ),
            spacing=Size.DEFAULT.value,
        
    )