import reflex as rx 
def footer() -> rx.Component:
  return rx.hstack(
        rx.text(
            "footer",
                height= 40,
        ),
        position= "center",
        bg="green",
    )