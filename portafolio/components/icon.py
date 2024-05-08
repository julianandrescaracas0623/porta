import reflex as rx 
from portafolio.style.styles import EmSize

def icon(icon: str)-> rx.Component:
    return rx.badge(
        rx.icon(
            icon,
            size=32
        ),
        aspect_ratio="1",
        variant="soft"
    )