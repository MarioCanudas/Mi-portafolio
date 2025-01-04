import reflex as rx 

def about_me() -> rx.Component:
    return rx.container(
        
        rx.vstack(
            rx.heading(
                'Sobre mí',
                size= '8',
                align= 'left'
                
            ),
            
            rx.text(
                'Esto es un prueba',
                align= 'left'
                
            ),
            
            rx.text(
                'Esto es un prueba',
                align= 'left'
                
            ),
            
            rx.text(
                'Esto es un prueba',
                align= 'left'
                
            ),
            
            rx.text(
                'Esto es un prueba',
                align= 'left'
                
            ),
            
        ),
        
        align_items= 'center',
        justify_content= 'center',
        spacing= '5'
        
    )