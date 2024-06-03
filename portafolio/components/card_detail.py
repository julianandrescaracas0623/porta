import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.style.styles import Size,EmSize,Enum,IMAGE_HEIGHT
#from portafolio.style.styles import MAX_WIDTH, EmSize, Size,BASE_STYLE,STYLESHEETS
from portafolio.data import Extra


def card_detail(extra:Extra)-> rx.Component:
    return rx.card(
        rx.link(
        rx.inset(
             rx.image(
                src=extra.image,
                height=IMAGE_HEIGHT,
                width="100%",
                object_fit="cover"
        ),
             pb=Size.SMALL.value
        ),
        rx.text.strong(extra.title),
        rx.text(
            extra.description,
            size=Size.SMALL.value,
            color_scheme="gray"
        )
        ),
         width="100%",
         href=extra.url, 
         is_external=True,
        #style=BASE_STYLE
    )