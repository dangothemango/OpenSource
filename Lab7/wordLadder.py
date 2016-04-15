
from networkx import *
import re,sys,gzip

#returns distance between 2 words
def dist(a,b):
	if len(a)!=len(b):
		return -1
	d=0
	for l in a:
		try:
			i=b.index(l)
			b=b[:i]+b[i+1:]
		except:
			d+=1
	return d

def make_graph(filename,wordlength):
	if '.gz' in filename:
		f=gzip.open(filename,'r')
	else:
		f=open(filename,'r')
	print ('Opened File...')
	graph=Graph(name="words"+str(wordlength))
	for line in f.readlines():
		if line[0]=='*':
			continue
		w=line[0:wordlength]
		graph.add_node(w)
	print ('Added nodes...')
	numNodes=number_of_nodes(graph)
	wordlist=graph.nodes()
	for word in range(numNodes):
		for otherWord in range(word,numNodes):
                  if dist(wordlist[word],wordlist[otherWord])==1:
                      graph.add_edge(wordlist[word],wordlist[otherWord])
	print ('Added Edges...')
	return graph

if __name__ == '__main__':
    print ('Loading 5 letter words...')
    G5=make_graph('words_dat.txt',5)
    print ('Loading 4 letter words...')
    G4=make_graph('words4.dat',4)
    wordpairs=[('chaos','order'),('nodes','graph'),('pound','marks'),('moron','smart'),('cold','warm'),('love','hate'),('main','lame')]
    for wordpair in wordpairs:
        if len(wordpair[0])==5:
            g=G5
        else:
            g=G4
        try:
            sp=shortest_path(g, wordpair[0], wordpair[1])
            print ("shortest path between '"+ wordpair[0] + "' and '"+ wordpair[1] + "' is:\n", sp)
        except:
            print ("no path found between '"+ wordpair[0] + "' and '"+ wordpair[1] + "'")



