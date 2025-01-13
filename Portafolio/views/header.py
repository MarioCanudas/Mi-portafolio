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
            ),
            
            rx.inset(
                rx.text(
                    'Actuaría + Python: Explorando el potencial del análisis de datos en el mundo actuarial.',
                    align= 'center',
                ),
                width="50vw",
                
            ),
            
            rx.hstack(
            
                rx.button(
                    rx.hstack(
                        rx.icon('github', color='white'),
                        align_items='center'
                    ), 
                    on_click= State.redirigir_github(),
                    bg= 'black',
                    color= 'white',
                ),
                
                rx.button(
                    rx.hstack(
                        rx.icon('linkedin', color='white'),
                        align_items='center'
                        ), 
                    on_click= State.redirigir_linkedin(),
                    bg= 'blue',
                    color= 'white',
                ),
                
                rx.button(
                    rx.hstack(
                        rx.icon(tag= 'mail', color='white'),
                        align_items='center'
                    ), 
                    on_click= State.copiar_correo(),
                    bg= 'grey',
                    color= 'white',
                ),
                
            ),
            align= 'center',
            spacing= '4',
            
        ),
        align_items= 'center',
        justify_content= 'center',
        min_height= '70vh',
        background_color= Color.SECUNDARY_BACKGROUND.value
        
    )
