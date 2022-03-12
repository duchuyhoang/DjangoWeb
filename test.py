class Parent():
	def say(x):
		print("parent")


class Child(Parent):
	def goi(self,param):
		self.say();
		print(param);
		print("Goi child")


child=Child();
child.goi("đâ");