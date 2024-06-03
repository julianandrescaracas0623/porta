from enum import Enum
import reflex as rx

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

class EmSize(Enum):
    DEFAULT = "1em"  # 16PX
    MEDIUM = "2em"  # 32PX
    BIG = "4em"  # 48PX
    
class Size(Enum):
    ZERO = "0"
    SMALL = "2"  # 8PX
    DEFAULT = "4"  # 16PX
    MEDIUM = "6"  # 32PX
    BIG = "8"  # 48PX

STYLESHEETS=[
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}