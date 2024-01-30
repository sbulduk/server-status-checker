from abc import ABC,abstractmethod

class IVM(ABC):
	@abstractmethod
	def Connect(self):
		pass

	@abstractmethod
	def GetVirtualMachineList(self):
		pass

	@abstractmethod
	def SelectVirtualMachine(self):
		pass

	@abstractmethod
	def ShowStatus(self,virtualMachine):
		pass

	@abstractmethod
	def PowerOn(self,virtualMachine):
		pass

	@abstractmethod
	def PowerOff(self,virtualMachine):
		pass

	@abstractmethod
	def Restart(self,virtualMachine):
		pass

	@abstractmethod
	def CloseConnection(self):
		pass