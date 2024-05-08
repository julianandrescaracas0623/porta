import reflex as rx 
from portafolio.style.styles import Size
from portafolio.components.icon_button import icon_button

def media()->rx.Component:
 return rx.hstack(
    icon_button(
        "mail",
        "url",
        "example@gmail.com",
        solid=True
    ),
    icon_button(
        "file-text",
        "url",
    ),
    icon_button(
        "github",
        "url"
    ),
    icon_button(
        "linkedin",
        "url"
    ),
    spacing=Size.SMALL.value
)