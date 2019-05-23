import gensim

def agreement(word,wv1,wv2,num):
  """ list of agreements between num most similar words to given word  """
  sim1=wv1.most_similar(positive=[word], topn=num)
  sim2=wv2.most_similar(positive=[word], topn=num)
  agreements=[]
  for (w,c) in sim1:
    found=0
    for(w2,c2) in sim2:
      if w == w2:
        found=1
    if found == 1:
      agreements.append(w)
  return(agreements)
