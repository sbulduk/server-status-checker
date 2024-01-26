class Credentials(object):
	_host="192.168.2.3"
	_username="sbulduk"
	_password="VAE1eyr9yty!gnt9vxe"

	@staticmethod
	def GetCredentials():
		return Credentials._host,Credentials._username,Credentials._password
	
	@staticmethod
	def PrintCredentials():
		print(f"{Credentials._host}\n{Credentials._username}\n{Credentials._password}")