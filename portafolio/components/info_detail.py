import reflex as rx
from portafolio.components.icon import icon
from portafolio.style.styles import EmSize, Size, IMAGE_HEIGHT
from portafolio.components.icon_button import icon_button
from portafolio.data import Info, Technology

def info_detail(info: Info) -> rx.Component:
    # Define las badges condicionalmente
    badges = []
    if info.technologies:
        badges = [
            rx.badge(
                rx.box(class_name=technology.icon),
                technology.name,
                color_scheme="gray"
            )
            for technology in info.technologies
        ]

    # Crear los icon buttons
    icon_buttons = rx.hstack(
        rx.cond(
            info.url != "",
            icon_button(
                "link",
                info.url
            )
        ),
        rx.cond(
            info.github != "",
            icon_button(
                "github",
                info.github
            )
        )
    )

    # Define el contenido de texto
    text_content = rx.vstack(
        rx.text.strong(info.title),
        rx.text(info.subtitle),
        rx.text(
            info.description,
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
        rx.flex(
            *badges,  # type: ignore
            wrap="wrap",
            spacing=Size.SMALL.value,
        ),
        icon_buttons,
        spacing=Size.SMALL.value,
        width="100%"
    )

    # Define la imagen (condicionalmente)
    image = rx.cond(
        info.image != "",
        rx.image(
            src=info.image if info.image else "favicon.ico",
            height=IMAGE_HEIGHT,
            width="auto",
            border_radius=EmSize.DEFAULT.value,
            object_fit="cover"
        )
    )

    # Define el badge y el icon button (condicionalmente)
    badge_icon_button = rx.vstack(
        rx.cond(
            info.date != "",
            rx.badge(info.date)
        ),
        rx.cond(
            info.certificate != "",
            icon_button(
                "shield-check",
                info.certificate,
                solid=True
            )
        ),
        spacing=Size.SMALL.value,
        align="end"
    )

    return rx.flex(
        rx.hstack(
            icon(info.icon),
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
