import reflex as rx 
from Portafolio import constants
from Portafolio.styles import Color

class State(rx.State):
    def redirigir_github(self):
        return rx.redirect(constants.GITHUB, is_external= True)
    
    def redirigir_linkedin(self):
        return rx.redirect(constants.LINKEDIN, is_external= True)
    
    @rx.event
    def copiar_correo(self):
        yield rx.set_clipboard(constants.MAIL)
        
        yield rx.toast(
            'Correo copiado al portapapeles, ¡Espero tu mensaje!', 
            duration= 3000, 
            close_button= True
        )

def header() -> rx.Component:
    return rx.container(
        
        rx.vstack(
            
            rx.heading('Mario Canudas', 
                size= '9',
                align= 'center',
                color= Color.HEADERS.value
            ),
            
            rx.box(
                rx.text(
                    'Actuaría',
                    as_= 'span',
                    color= Color.ACTUARIA_WORD.value
                ),
                
                rx.text(
                    ' + ',
                    as_= 'span',
                    color= Color.SUBHEADERS.value
                ),
                
                rx.text(
                    'Python',
                    as_= 'span',
                    color= Color.PYTHON_WORD.value
                ),
                
                rx.text(
                    ': Explorando el potencial del análisis de datos en el mundo actuarial.',
                    as_= 'span',
                    color= Color.SUBHEADERS.value
                ),
                align= 'center'
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
                    rx.icon('linkedin', color= Color.PRINCIPAL_TEXT.value),
                    on_click= State.redirigir_linkedin(),
                    bg= Color.SECUNDARY_BACKGROUND.value,
                    _hover= {
                        'background_color' : Color.BUTTON_HOVER.value,
                        'color' : Color.PRINCIPAL_TEXT.value
                    },
                    align_items='center',
                ),
                
                rx.button(
                    rx.icon(tag= 'mail', color= Color.PRINCIPAL_TEXT.value),
                    on_click= State.copiar_correo(),
                    bg= Color.SECUNDARY_BACKGROUND.value,
                    _hover= {
                        'background_color' : Color.BUTTON_HOVER.value,
                        'color' : Color.PRINCIPAL_TEXT.value
                    },
                    align_items='center',
                ),
                
            ),
            align= 'center',
            spacing= constants.SPACING_IN_STACKS,
            
        ),
        align_items= 'center',
        justify_content= 'center',
        min_height= '60vh',
        background_color= Color.SECUNDARY_BACKGROUND.value
        
    )
