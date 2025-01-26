import reflex as rx 
from Portafolio import constants
from Portafolio.styles import Color

class State(rx.State):
    def redirigir_github(self):
        return rx.redirect(constants.DATA_VISUALIZER_GIT, is_external= True)

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
                    rx.image(
                        src= '/vdc-0.1a.png',
                        width= '100%',
                        border_radius= '12px 12px 0px 0px',
                    ),
                    
                    rx.vstack(
                        
                        rx.vstack(
                            rx.flex(
                                rx.box(
                                    rx.text(
                                        'Python',
                                        text_align= 'center',
                                        align= 'center',
                                        color= Color.PYTHON_WORD.value,
                                        font_size= '12px',
                                    ),
                                    flex= '1',
                                    border_radius= constants.BORDERS_RADIUS,
                                    background_color= Color.PYTHON_BACKGROUND.value,
                                    
                                ),
                                rx.box(
                                    rx.text(
                                        'Streamlit',
                                        text_align= 'center',
                                        align= 'center',
                                        color= Color.STREAMLIT_WORD.value,
                                        font_size= '12px',
                                    ),
                                    flex= '1',
                                    border_radius= constants.BORDERS_RADIUS,
                                    background_color= Color.STREAMLIT_BACKGROUND.value,
                                    
                                ),
                                rx.box(
                                    rx.text(
                                        'Pandas',
                                        text_align= 'center',
                                        align= 'center',
                                        color= Color.PANDAS_WORD.value,
                                        font_size= '12px',
                                    ),
                                    flex= '1',
                                    border_radius= constants.BORDERS_RADIUS,
                                    background_color= Color.PANDAS_BACKGROUND.value,
                                    
                                ),
                                spacing= '2',
                                width= '100%',
                            ),
                            rx.flex(
                                rx.box(
                                    rx.text(
                                        'Altair',
                                        text_align= 'center',
                                        align= 'center',
                                        color= Color.ALTAIR_WORD.value,
                                        font_size= '12px',
                                    ),
                                    flex= '1',
                                    border_radius= constants.BORDERS_RADIUS,
                                    background_color= Color.ALTAIR_BACKGROUND.value,
                                    
                                ),
                                rx.box(
                                    rx.text(
                                        'Prophet',
                                        text_align= 'center',
                                        align= 'center',
                                        color= Color.PROPHET_WORD.value,
                                        font_size= '12px',
                                    ),
                                    flex= '1',
                                    border_radius= constants.BORDERS_RADIUS,
                                    background_color= Color.PROPHET_BACKGROUND.value,
                                    
                                ),
                                align= 'center',
                                spacing= '2',
                                width= '60%'
                            ),
                            width= '100%',
                            spacing= '2',
                            justify_content= 'space-between',
                            align_items= 'center',
                        ),
                        
                        rx.box(
                            rx.heading(
                                'Data visualizer',
                                size= constants.SUBHEADINGS_SIZE,
                                align= 'left',
                                color= Color.SUBHEADERS.value
                                
                            ),
                            rx.text(
                                'Aplicación web desarrollada para la visualización  y análisis de datos financieros de un grupo de empresas.',
                                align= 'left',
                                color = Color.PRINCIPAL_TEXT.value,
                                font_size= '13px'
                            ),
                        ),
                        
                        rx.hstack(
                            rx.button(
                                rx.icon('github', color= Color.PRINCIPAL_TEXT.value),
                                on_click= State.redirigir_github(),
                                bg= Color.SECUNDARY_BACKGROUND.value,
                                _hover= {
                                    'background_color' : Color.BUTTON_HOVER.value,
                                    'color' : Color.PRINCIPAL_TEXT.value
                                },
                                align_items='center',
                            ),
                            rx.button(
                                rx.icon('link', color= Color.PRINCIPAL_TEXT.value),
                                on_click= State.redirigir_github(),
                                bg= Color.SECUNDARY_BACKGROUND.value,
                                _hover= {
                                    'background_color' : Color.BUTTON_HOVER.value,
                                    'color' : Color.PRINCIPAL_TEXT.value
                                },
                                align_items='center',
                            ),
                            align_items= 'center',
                            
                        ),
                        padding= '1rem',
                        spacing= '3',
                        justify_content= 'space-between',
                        align_items= 'center',
                    ),
                    spacing= '1.5rem',
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