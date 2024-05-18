import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.style.styles import Size,EmSize,Enum,IMAGE_HEIGHT


def card_detail()-> rx.Component:
    return rx.card(
        rx.inset(
             rx.image(
                src="favicon.ico",
                height=IMAGE_HEIGHT,
                width="100%",
                object_fit="cover"
        ),
             pb=Size.SMALL.value
        ),
        rx.text.strong("Titulo"),
        rx.text(
            "Description",
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
         width="100%",
    )