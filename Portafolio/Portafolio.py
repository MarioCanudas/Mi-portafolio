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
    return rx.box(
        
        rx.color_mode.button(position="bottom-right"),
        
        rx.center(
            
            rx.vstack(
            
                rx.box(
                    
                    rx.container(
                        
                        rx.vstack(
                            
                            rx.heading('Hola, soy Mario Canudas y este es mi portafolio.', 
                                size= '8',
                                align= 'center',
                                color= 'black'
                            ),
                            
                            rx.inset(
                                rx.text(
                                    'Soy estudiante de Actuaría, apasionado por el análisis de datos, los modelos de Machine Learning y la tecnología.',
                                    align= 'center',
                                    color= 'black'
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
                        min_height= '85vh',
                        
                    ),
                    background_image= "url('/background_1st_part.jpg')",
                    background_size= 'cover',
                    background_position= 'center',
                    height= "70vh",
                    border_bottom_left_radius="10px",
                    border_bottom_right_radius="10px"
                    
                ),

            ),
            
        ), 
        
    )

app = rx.App()
app.add_page(index)