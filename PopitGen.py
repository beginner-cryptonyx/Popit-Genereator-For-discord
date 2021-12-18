#Imports
from random import randint
import win32clipboard

class PopGen():
    # initilaizing the class to active self 
    def __init__(self):

        # Definitions of color based on output
        self.COLORDICT = {1:'||:red_square:||', 2:'||:blue_square:||',
        3:"||:yellow_square:||", 4:"||:green_square:||", 5:"||:orange_square:||",
        6:"||:purple_square:||", 7:"||:brown_square:||"}
    

    # generates a 'perfect' pop game
    def GeneratePerfect(self, is_copy=False) -> str:

        '''
        This function generates a amount of colors as x and y axis
        amount of colors:x_axis * amount of colors:y_axis

        parameters:
        is_copy : copies popit code to clipboard : default : False
        '''
        # pop variable to return 
        pop = ''

        # code to add colors ( in line ) to pop
        for i in range(1, len(self.COLORDICT)+1):
            pop += self.COLORDICT[i] * len(self.COLORDICT) + '\n'
        
        # copy to clipboard
        if is_copy == True:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(pop)
            win32clipboard.CloseClipboard()
        # returing pop
        return 'Made by https://github.com/beggainer-crypto \n' + pop


    def GenerateRandom(self, grid_y=6, grid_x=6, is_copy=False) -> any:
        '''
        this function randomly generates a popit for discord, takes 3 parameters:
        
        grid_y : height of pop : default : 6
        grid_x : width of pop : default : 6
        is_copy: copies the pop command to clipboard : default : False

        '''
        # Generates the popit
        pop = ''

        # for every line
        for i in range(grid_y):
            
            # add random colors
            for j in range(grid_x):
                # adding colors to pop variable
                pop += self.COLORDICT[randint(1, len(self.COLORDICT))]
            
            # adding a new line
            pop += '\n'
        
        # if user wants to copy pop code to clipboard
        if is_copy == True:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(pop)
            win32clipboard.CloseClipboard()
        
        # returns pop
        return 'Made by https://github.com/beggainer-crypto \n' + pop


# Exectute the folowing if the file is not imported
if '__main__' == __name__:

    # define what is PopGen 
    bot = PopGen()
    print(bot.GenerateRandom(grid_y=20, grid_x=20, is_copy=True))
    # print(bot.GeneratePerfect(is_copy=True))
    

