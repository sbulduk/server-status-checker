from mainmenu import MainMenu

class Main(object):
	@staticmethod
	def Run()->None:
		MainMenu.MainMenuScreen()

if __name__=="__main__":
	Main.Run()