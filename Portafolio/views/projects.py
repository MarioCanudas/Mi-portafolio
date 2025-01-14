import reflex as rx 
from Portafolio import constants
from Portafolio.styles import Color

def projects() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading(
                'Proyectos',
                size= constants.HEADINGS_SIZE,
                align= 'left',
                color= Color.HEADERS.value
            ),
            
            rx.flex(
                
                rx.box(
                    rx.heading(
                        'Proyecto # 1',
                        size= constants.SUBHEADINGS_SIZE,
                        align= 'center',
                        color= Color.SUBHEADERS.value
                        
                    ),
                    flex= '1',
                    background_color= Color.SECUNDARY_BACKGROUND.value,
                    border= constants.BORDERS,
                    border_radius= constants.BORDERS_RADIUS,
                    box_shadow= constants.BOX_SHADOW,
                ),
                
                rx.box(
                    rx.heading(
                        'Proyecto # 2',
                        size= constants.SUBHEADINGS_SIZE,
                        align= 'center',
                        color= Color.SUBHEADERS.value
                    ),
                    flex= '1',
                    background_color= Color.SECUNDARY_BACKGROUND.value,
                    border= constants.BORDERS,
                    border_radius= constants.BORDERS_RADIUS,
                    box_shadow= constants.BOX_SHADOW,
                ),
                
                rx.box(
                    rx.heading(
                        'Proyecto # 3',
                        size= constants.SUBHEADINGS_SIZE,
                        align= 'center',
                        color= Color.SUBHEADERS.value
                    ),
                    flex= '1',
                    background_color= Color.SECUNDARY_BACKGROUND.value,
                    border= constants.BORDERS,
                    border_radius= constants.BORDERS_RADIUS,
                    box_shadow= constants.BOX_SHADOW,
                ),
                gap= '2em',
                wrap= 'wrap',
                width= '100%',
                justify_content= 'space-between',
                align= 'center'
                
            ),
            spacing= constants.SPACING_IN_STACKS,
            
        ),
        align_items= 'center',
        justify_content= 'center',
        spacing= constants.SPACING_IN_CONTAINERS,
        margin = constants.DIVIDER_MARGIN
    )