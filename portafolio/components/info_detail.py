import reflex as rx
from portafolio.components.icon import icon
from portafolio.style.styles import EmSize, Size,  IMAGE_HEIGHT
from portafolio.components.icon_button import icon_button


def info_detail() -> rx.Component:
    return rx.hstack(
        icon("box-select"),
        rx.vstack(
            rx.text.strong("Titulo"),
            rx.text("Subtitulo"),
            rx.text(
                "Descripcion",
                size=Size.SMALL.value,
                color_scheme="gray"
            ),
            rx.flex(
                *[
                    rx.badge(
                        f"Badge{index}",
                        color_scheme="gray"
                    )
                    for index in range(0,5)  # Close the square bracket here
                ],
                wrap="wrap",
                spacing=Size.SMALL.value,
            ),
                rx.hstack(
                    icon_button(
                        "link",
                        "url"
                    ),
                    icon_button(
                        "github",
                        "url"
                    ),
                ),
                spacing=Size.SMALL.value,
                width="100%"
        ),
        rx.hstack(
            rx.image(
                    src="favicon.ico",
                    height=IMAGE_HEIGHT,
                    width="auto",
                    border_radius=EmSize.DEFAULT.value
                ),
            rx.vstack(
             rx.badge("Años"),
            icon_button(
                "shield-check",
                "url",
                solid=True
            ),
            spacing=Size.SMALL.value,
            align="end"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )
