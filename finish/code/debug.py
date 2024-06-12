import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10):
    """
    Display debug information on the screen.
    
    Args:
        info (str): The information to display.
        y (int, optional): The y-coordinate of the debug text. Defaults to 10.
        x (int, optional): The x-coordinate of the debug text. Defaults to 10.
    """
	# Get the display surface	
    display_surface = pygame.display.get_surface()
	# Render the debug information
    debug_surf = font.render(str(info),True,'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
	# Draw a black rectangle as the background
    pygame.draw.rect(display_surface,'Black',debug_rect)
	# Blit the debug information onto the display surface
    display_surface.blit(debug_surf,debug_rect)
