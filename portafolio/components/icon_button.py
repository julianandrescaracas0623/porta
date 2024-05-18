from pydantic_core import Url
import reflex as rx 

def icon_button(icon:str,url:str,text="", solid=False)-> rx.Component:
    return rx.button(
        rx.icon(icon),
        text,
        variant="solid" if solid else "surface",
        on_click=rx.redirect(Url,True)
    )