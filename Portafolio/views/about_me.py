import reflex as rx 

def about_me() -> rx.Component:
    return rx.container(
        
        rx.flex(
            rx.vstack(
                rx.heading(
                    'Sobre mí',
                    size= '8',
                    align= 'left'
                    
                ),
                
                rx.hstack(
                    rx.text(
                        """
                        Estudiante de Actuaría con habilidades en Python para el análisis y visualización de datos. Con experiencia práctica en 
                        el desarrollo de soluciones analíticas y un interés constante en aprender técnicas de Machine Learning y Data Science. 
                        Busco aplicar mis conocimientos para resolver problemas complejos en el sector actuarial.
                        """,
                        align= 'left'
                        
                    ),
                    
                ),
                
            ),
            rx.image(
                src= "/me.jpg",
                width= '170px',
                height= 'auto',
                border_radius="15px",
                
            ),
            spacing= '5'

        ),
        align_items= 'center',
        justify_content= 'center',
        spacing= '5'
        
    )