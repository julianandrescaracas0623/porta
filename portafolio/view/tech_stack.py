import reflex as rx 
from portafolio.components.heading import heading
from portafolio.style.styles import Size
from portafolio.data import Technology

def tech_stack(technologies:list[Technology])-> rx.Component:
    return rx.vstack(
        heading("Tecnologias"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(class_name = technology.icon,
                           font_size="24px"),
                    rx.text(technology.name),
                    color_scheme="gray",
                    size="1"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )