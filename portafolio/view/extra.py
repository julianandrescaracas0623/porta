import reflex as rx
from portafolio.components.heading import heading
from portafolio.components.card_detail import card_detail
from portafolio.style.styles import Size

def extra() -> rx.Component:
    # Creamos una lista de componentes en card_details
    cards = [card_detail() for _ in range(3)]
    
    return rx.vstack(
        heading("Extra"),  
        rx.mobile_only(
            rx.vstack(
                *cards,
                spacing=Size.DEFAULT.value,  
                width="100%"  
            )
        ),
        rx.tablet_and_desktop(
            rx.grid(
                *cards,
                spacing=Size.DEFAULT.value,  
                columns="3",
                width="100%"  
            )
        ),
        spacing=Size.SMALL.value,  
        width="100%" 
    )
