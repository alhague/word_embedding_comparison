# takes a startword from a gensim model and draws a simple graph for similar words
import gensim
from graphviz import Graph

model=gensim.models.word2vec.Word2Vec.load(MYMODEL)

f = Graph('test',filename='graph.gv')
f.attr('node')
startword=MYSTARTWORD
f.node(startword,color="yellow")
f.node_attr.update(color='lightblue2', style='filled',fontsize='7',fixedsize='false',margin='0',fontname="Arial")
f.edge_attr.update(fontsize='7',splines="ortho")
f.graph_attr.update(fontsize='7',ranksep='0.25',nodesep="0.1",dim="10")
slist=model.wv.most_similar(positive=[startword],topn=16)
nodes=set()
edges=[]
for i,(k,v) in enumerate(slist):
    nodes.add(k)
    edges.append([startword,k,v])
    for j,(k2,v2) in enumerate(slist):
        if(i!=j):
            w=model.wv.similarity(k,k2)
            if(i<j):
                edges.append([k,k2,w])

for node in nodes:
    f.node(node)

for edge in edges:
    #print(edge)
    if(float(edge[2])>0.6):
        f.edge(edge[0],edge[1],weight=str(100*edge[2]))
