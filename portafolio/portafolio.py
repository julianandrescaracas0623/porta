import reflex as rx
from portafolio.view.header import header
from portafolio.style.styles import MAX_WIDTH, EmSize, Size,BASE_STYLE,STYLESHEETS
from portafolio.view.footer import footer 
from portafolio.view.about import about
from portafolio.view.info import info
from portafolio.view.extra import extra
from portafolio.view.tech_stack import tech_stack
from . import data

DATA = data.data

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experiencia"),
            info("Proyectos"),
            info("Formacion"),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )

app = rx.App(
    stylesheets = STYLESHEETS,
    style=BASE_STYLE)
app.add_page(index)
