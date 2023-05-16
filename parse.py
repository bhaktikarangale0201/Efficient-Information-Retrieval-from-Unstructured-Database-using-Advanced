


class CorpusParser:

	def __init__(self, filename):
		self.filename = filename

		self.corpus = dict()

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
			# print(s)
		blobs = s.split('#')[1:]
		# print(blobs)
		for x in blobs:
			text = x.split()
			# print(text)
			docid = text.pop(0)
			# print(text)
			# print(docid)
			self.corpus[docid] = text

	def get_corpus(self):
		# print(self.corpus)
		return self.corpus


class QueryParser:

	def __init__(self, filename):
		self.filename = filename
		self.queries = []

	def parse(self):
		with open(self.filename) as f:
			lines = ''.join(f.readlines())
		self.queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]

	def get_queries(self):
		# print(self.queries)
		return self.queries


if __name__ == '__main__':
	qp = QueryParser('text/queries.txt')
	print(qp.get_queries())