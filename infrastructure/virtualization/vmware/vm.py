from core.virtualization.ivm import IVM
from infrastructure.virtualization.vmware.credentials import Credentials
from pyVim import connect
import ssl
from pyVmomi import vmodl,vim

class VM(IVM):
	def __init__(self):
		super().__init__()
		self.host,self.username,self.password=Credentials.GetCredentials()

	def Connect(self):
		context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)
		context.verify_mode=ssl.CERT_NONE

		try:
			vmServiceInstance=connect.SmartConnect(host=self.host,user=self.username,pwd=self.password,sslContext=context)
			print("ESXi Connection Established Successfully!")
		except vmodl.MethodFault as error:
			print(f"vmodl fault: {error.msg}")
			return -1
		
		content=vmServiceInstance.RetrieveContent()
		container=content.rootFolder
		viewType=[vim.VirtualMachine]
		recursive=True
		containerView=content.viewManager.CreateContainerView(container,viewType,recursive)
		children=containerView.view

		for child in children:
			print(f"{child.name}")

		self.CloseConnection(vmServiceInstance)
		
	def CloseConnection(self,serviceInstance):
		connect.Disconnect(serviceInstance)

	def PerformOperation(self,operation:str):
		if operation=="power_on":
			self.PowerOn()
		elif operation=="shutdown":
			self.Shutdown()
		elif operation=="restart":
			self.Restart()
		else:
			return None
		
	def PowerOn(self):
		pass

	def Shutdown(self):
		pass

	def Restart(self):
		pass