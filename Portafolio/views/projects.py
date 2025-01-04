import reflex as rx 

def projects() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading(
                'Proyectos',
                size= '8',
                align= 'left'
            ),
            
            rx.flex(
                
                rx.card(
                    rx.heading(
                        'Proyecto # 1',
                        size= '7',
                        
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
                
                rx.card(
                    rx.heading(
                        'Proyecto # 2',
                        size= '7',
                        
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
                
                rx.card(
                    rx.heading(
                        'Proyecto # 3',
                        size= '7',
                        
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
                gap= '2em',
                wrap= 'wrap',
                width= '100%',
                
            ),
            spacing= '3',
            
        ),
        align_items= 'center',
        justify_content= 'center',
        spacing= '5'
    )