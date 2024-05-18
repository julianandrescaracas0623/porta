import reflex as rx 
from portafolio.style.styles import Size
from portafolio.components.icon_button import icon_button

def media()->rx.Component:
 return rx.flex(
    icon_button(
        "mail",
        "url",
        "example@gmail.com",
        solid=True
    ),
    
    rx.hstack(
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
    ),
    spacing=Size.SMALL.value,
    flex_direction=["column","column","row"]
)