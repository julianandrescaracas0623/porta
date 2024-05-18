import reflex as rx
from portafolio.components.icon import icon
from portafolio.style.styles import EmSize, Size, IMAGE_HEIGHT
from portafolio.components.icon_button import icon_button

def info_detail() -> rx.Component:
    # Define the badges
    badges = [
        rx.badge(f"Badge{index}", color_scheme="gray") for index in range(5)
    ]

    # Define the icon buttons
    icon_buttons = rx.hstack(
        icon_button("link", "url"),
        icon_button("github", "url"),
    )

    # Define the text content
    text_content = rx.vstack(
        rx.text.strong("Titulo"),
        rx.text("Subtitulo"),
        rx.text(
            "Descripcion",
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
        rx.flex(
            *badges,
            wrap="wrap",
            spacing=Size.SMALL.value,
        ),
        icon_buttons,
        spacing=Size.SMALL.value,
        width="100%"
    )

    # Define the image
    image = rx.image(
        src="favicon.ico",
        height=IMAGE_HEIGHT,
        width="auto",
        border_radius=EmSize.DEFAULT.value,
        object_fit="cover"
    )

    # Define the badge and icon button
    badge_icon_button = rx.vstack(
        rx.badge("Años"),
        icon_button(
            "shield-check",
            "url",
            solid=True
        ),
        spacing=Size.SMALL.value,
        align="end"
    )

    return rx.flex(
        rx.hstack(
            icon("box-select"),
            text_content,
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        image,
        badge_icon_button,
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
