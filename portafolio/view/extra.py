import reflex as rx 
from portafolio.components.heading import heading
from portafolio.components.card_detail import card_detail 
from portafolio.style.styles import Size

def extra() -> rx.Component:
    return rx.vstack(
        heading("Extra"),
        rx.hstack(
            *[card_detail() for _ in range(0,3)],
            spacing=Size.DEFAULT.value,
        ),
        spacing=Size.SMALL.value,
        width="100%"
    )