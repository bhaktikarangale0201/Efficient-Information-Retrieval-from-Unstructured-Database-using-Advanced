 from parse import *
from query import QueryProcessor
import operator


def main():
	qp = QueryParser(filename='D:\\Sem-6\\AI\\pythonProject5\\text\\queries.txt')
	cp = CorpusParser(filename='D:\\Sem-6\\AI\\pythonProject5\\text\\corpus.txt')
	qp.parse()
	queries = qp.get_queries()
	# print(queries)
	cp.parse()
	corpus = cp.get_corpus()
	# print(corpus)
	proc = QueryProcessor(queries, corpus)
	results = proc.run()
	qid = 0
	for result in results:
		sorted_x = sorted(result.items(), key=operator.itemgetter(1))
		sorted_x.reverse()
		index = 0
		for i in sorted_x[:100]:
			tmp = (qid, i[0], index, i[1])
			print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
			index += 1
		qid += 1


if __name__ == '__main__':
	main()
