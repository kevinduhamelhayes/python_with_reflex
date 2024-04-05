import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name = "Kevin", size = "6"),
        rx.text("Kevin"),
        rx.text("Software Developer")
    )