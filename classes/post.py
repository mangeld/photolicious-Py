class Post:

	def __init__(self):
		self.title    = ""
		self.content  = ""
		self.dateTime = ""
		self.creator  = ""
		self.comments = [ Comment() ]