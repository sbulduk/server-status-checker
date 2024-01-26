from abc import ABC,abstractmethod

class IVM(ABC):
	@abstractmethod
	def Connect(self):
		pass

	@abstractmethod
	def CloseConnection(self):
		pass

	@abstractmethod
	def PerformOperation(self,operation:str):
		pass