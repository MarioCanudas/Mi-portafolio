import reflex as rx

class State(rx.State):
    
    numero_cel = '5639265819'
    correo = 'mario.cz24@outlook.com'
    
    def redirigir_github(self):
        return rx.redirect('https://github.com/MarioCanudas', is_external= True)
    
    def redirigir_linkedin(self):
        return rx.redirect('https://www.linkedin.com/in/Mario-Canudas/', is_external= True)
    
    def redirigir_whatsapp(self):
        return rx.redirect(f'https://wa.me/{self.numero_cel}', is_external= True)
    
    @rx.event
    def copiar_correo(self):
        yield rx.set_clipboard(self.correo)
        
        yield rx.toast(
            'Correo copiado al portapapeles, ¡Espero tu mensaje!', 
            duration= 3000, 
            close_button= True
        )

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        
        rx.color_mode.button(position="bottom-right"),
        
        rx.vstack(
            
            rx.heading('Hola, soy Mario Canudas y este es mi portafolio.', 
                size= '9'
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
                )
            
            ),
            
            align_items= 'center',
            spacing="5",
            justify="center",
            min_height="85vh"
        ),
    )


app = rx.App()
app.add_page(index)
