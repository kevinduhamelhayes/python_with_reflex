import reflex as rx 
def navbar() -> rx.Component:
   return rx.hstack(
        rx.text(
             "kevin",
                height= 40,
        ),
        position= "center",
        bg="red",
    )