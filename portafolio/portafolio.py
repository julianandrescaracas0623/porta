import reflex as rx
from portafolio.view.header import header
from portafolio.style.styles import MAX_WIDTH
from portafolio.style.styles import EmSize,Size
from portafolio.view.footer import footer 
from portafolio.view.about import about
from portafolio.view.info import info
from portafolio.view.extra import extra
from portafolio.view.tech_stack import tech_stack
def index()->rx.Component:
    return rx.center(
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            tech_stack(),
            info("Experiencia"),
            info("Proyectos"),
            info("Formacion"),
            extra(),
            rx.divider(),
            footer(),
            spacing=Size.MEDIUM.value,
             padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"   
        )
    )

app = rx.App()
app.add_page(index)
