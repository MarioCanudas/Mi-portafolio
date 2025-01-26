import reflex as rx
from Portafolio.styles import Color
from Portafolio import constants

def about_me() -> rx.Component:
    return rx.container(
        
        rx.vstack(
            rx.heading(
                    'Sobre mí',
                    size= '8',
                    align= 'left',
                    color= Color.HEADERS.value
                    
                ),
            rx.box(
                rx.flex(
                    rx.text(
                        """
                        Estudiante de Actuaría con habilidades en Python para el análisis y visualización de datos. Con experiencia práctica en 
                        el desarrollo de soluciones analíticas y un interés constante en aprender técnicas de Machine Learning y Data Science. 
                        Busco aplicar mis conocimientos para resolver problemas complejos en el sector actuarial.
                        """,
                        align= 'left',
                        color= Color.PRINCIPAL_TEXT.value
                        
                    ),
                        
                    rx.image(
                        src= "/me.jpg",
                        width= '150px',
                        height= 'auto',
                        border_radius= constants.BORDERS_RADIUS,
                        flex= '1',
                        box_shadow= constants.BOX_SHADOW,
                        
                    ),
                    align_items="center", 
                    justify_content="space-between",  
                    width="100%",
                    spacing= constants.SPACING_IN_STACKS,
                    padding= constants.PADDING_BOXES,
                    
                ),
                background_color= Color.SECUNDARY_BACKGROUND.value,
                border= constants.BORDERS,
                border_radius= constants.BORDERS_RADIUS,
                box_shadow= constants.BOX_SHADOW,
                
            ),
            spacing= constants.SPACING_IN_STACKS
        ),
        align_items= 'center',
        justify_content= 'center',
        spacing= constants.SPACING_IN_CONTAINERS,
        margin = constants.DIVIDER_MARGIN
        
    )
    