import reflex as rx

def links() -> rx.Component:
    return rx.hstack(
        rx.text("Links"),
        rx.text("Github"),
        rx.text("Linkedin"),
        rx.text("Email"),
        rx.text("Resume"),
        rx.text("Projects"),
        rx.text("About"),
        rx.text("Contact")
    )
