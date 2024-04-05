import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name = "Kevin", size = "xl"),
        rx.text("Kevin", size = "xl"),
        rx.text("Software Developer", size = "sm")
    )