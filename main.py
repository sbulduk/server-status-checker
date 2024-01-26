from injector import Injector
from infrastructure.dimodule.diconfig import DIConfig
from core.virtualization.ivm import IVM

class Main(object):
	injector=Injector([DIConfig()])
	vm=injector.get(IVM)

	@staticmethod
	def Run()->None:
		Main.vm.Connect()	

if __name__=="__main__":
	Main.Run()