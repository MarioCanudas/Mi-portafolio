import reflex as rx 
from Portafolio import constants

class State(rx.State):
    def redirigir_github(self):
        return rx.redirect(constants.GITHUB, is_external= True)
    
    def redirigir_linkedin(self):
        return rx.redirect(constants.LINKEDIN, is_external= True)
    
    def redirigir_whatsapp(self):
        return rx.redirect(constants.WHATSAPP, is_external= True)
    
    @rx.event
    def copiar_correo(self):
        yield rx.set_clipboard(self.correo)
        
        yield rx.toast(
            'Correo copiado al portapapeles, ¡Espero tu mensaje!', 
            duration= 3000, 
            close_button= True
        )

def header() -> rx.Component:
    return rx.container(
        
        rx.vstack(
            
            rx.heading('Hola, soy Mario Canudas y este es mi portafolio.', 
                size= '8',
                align= 'center',
            ),
            
            rx.inset(
                rx.text(
                    'Soy estudiante de Actuaría, apasionado por el análisis de datos, los modelos de Machine Learning y la tecnología.',
                    align= 'center',
                ),
                width="50vw",
                
            ),
            
            rx.hstack(
            
                rx.button(
                    rx.hstack(
                        rx.icon('github', color='white'),
                        rx.markdown('GitHub', color='white'),
                        align_items='center'
                    ), 
                    on_click= State.redirigir_github(),
                    bg= 'black',
                    color= 'white',
                ),
                
                rx.button(
                    rx.hstack(
                        rx.icon('linkedin', color='white'),
                        rx.markdown('LinkedIn', color='white'),
                        align_items='center'
                        ), 
                    on_click= State.redirigir_linkedin(),
                    bg= 'blue',
                    color= 'white',
                ),
                
                rx.button(
                    rx.hstack(
                        rx.icon(tag= 'mail', color='white'),
                        rx.markdown('Mail', color='white'),
                        align_items='center'
                    ), 
                    on_click= State.copiar_correo(),
                    bg= 'grey',
                    color= 'white',
                ),
                
                rx.button(
                    rx.hstack(
                        rx.icon(tag='phone', color='white'),
                        rx.markdown('WhatsApp', color='white'),
                        align_items='center'
                    ), 
                    on_click= State.redirigir_whatsapp(),
                    bg= 'green',
                    color= 'white',
                ),
                
            ),
            align= 'center',
            spacing= '4',
            
        ),
        align_items= 'center',
        justify_content= 'center',
        spacing= '5',
        min_height= '75vh',
        background_color= '#494949'
        
    )
