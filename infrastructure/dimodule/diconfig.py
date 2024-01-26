from injector import Module,inject,Binder
from core.virtualization.ivm import IVM
from infrastructure.virtualization.vmware.vm import VM

class DIConfig(Module):
	@staticmethod
	@inject
	def configure(binder:Binder)->None:
		binder.bind(IVM,to=VM)