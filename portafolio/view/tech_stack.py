import reflex as rx 
from portafolio.components.heading import heading
from portafolio.style.styles import Size

def tech_stack()-> rx.Component:
    return rx.vstack(
        heading("Tecnologias"),
        rx.flex(
            *[
                rx.badge(
                    rx.icon("code"),
                    rx.text(f"Stack{index}"),
                    color_scheme="gray",
                    size="1"
                )
                for index in range (0,5)
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )