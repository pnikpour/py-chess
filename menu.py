

class Menu:
    def getInput(self):
        isValid = False
        option = ''
        validOptions = ['1', 'q']
        while not isValid:
            print('Welcome to py-chess')
            print('Select a game mode')
            print('[1] Two Player Game')
            option = input()
            if option in validOptions:
                break
            else:
                print('Invalid option')
        return option

if __name__ == '__main__':
    menu = Menu()
    menu.getInput()
