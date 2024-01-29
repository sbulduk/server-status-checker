from core.virtualization.ivm import IVM

class VMOperations(IVM):
	def __init__(self,vm)->None:
		super().__init__()
		self.vm=vm

	