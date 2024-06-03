import reflex as rx 
from portafolio.style.styles import Size
from portafolio.components.icon_button import icon_button
from portafolio.data import Media

def media(data:Media)->rx.Component:
 return rx.flex(
    icon_button(
        "mail",
        f"mailto:{data.email}",
        data.email,
        solid=True
    ),
    
    rx.hstack(
    icon_button(
        "file-text",
        data.cv,
    ),
    icon_button(
        "github",
        data.github
    ),
    icon_button(
        "linkedin",
        data.linkedin
    ),
    spacing=Size.SMALL.value
    ),
    spacing=Size.SMALL.value,
    flex_direction=["column","column","row"]
)