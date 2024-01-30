from injector import Injector
from infrastructure.dimodule.diconfig import DIConfig
from core.virtualization.ivm import IVM
import sys

class MainMenu(object):
	injector=Injector([DIConfig()])
	virtualMachineInstance=injector.get(IVM)

	@staticmethod
	def MainMenuScreen():
		selectedVirtualMachine=MainMenu.virtualMachineInstance.SelectVirtualMachine()
		if selectedVirtualMachine:
			MainMenu.RunOperations(selectedVirtualMachine)

	@staticmethod
	def ShowMainMenu():
		print("----------------------------------------")
		print("Virtual Machine Operations Menu:")
		print("1. Show Status")
		print("2. Power On")
		print("3. Power Off")
		print("4. Restart")
		print("9. Main Menu")
		print("0. Exit")
		print("----------------------------------------")

	@staticmethod
	def RunOperations(selectedVirtualMachine):
		while True:
			MainMenu.ShowMainMenu()
			vmOperationChoice=input("Enter choice: ")
			print("----------------------------------------")
			if vmOperationChoice=="1":
				MainMenu.virtualMachineInstance.ShowStatus(selectedVirtualMachine)
				print("----------------------------------------")
			elif vmOperationChoice=="2":
				MainMenu.virtualMachineInstance.PowerOn(selectedVirtualMachine)
				print("----------------------------------------")
			elif vmOperationChoice=="3":
				MainMenu.virtualMachineInstance.PowerOff(selectedVirtualMachine)
				print("----------------------------------------")
			elif vmOperationChoice=="4":
				MainMenu.virtualMachineInstance.Restart(selectedVirtualMachine)
				print("----------------------------------------")
			elif vmOperationChoice=="9":
				MainMenu.MainMenuScreen()
			elif vmOperationChoice=="0":
				sys.exit()
			else:
				print("Invalid choice. Please try again.")