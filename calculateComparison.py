import random
def calcComparisons(wv1,wv2,wv3,hkl,num,topn):
  """ Take three word vector models and run num tests with topn words for a frequency class """
  counts1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  counts2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  counts3=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  counts4=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  counts5=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  counts6=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  for i in range(num-1):
    good=0
    while good < 1:
      testword=hklwl[hkl][random.randint(0,len(hklwl[hkl]) - 1)]
      if testword in wv1.vocab and testword in wv2.vocab and testword in wv3.vocab:
        good=1

    for (word,sim) in wv1.most_similar(positive=[testword],topn=topn):
      counts1[wf_hkl[word]]+=1
      
    for (word,sim) in wv2.most_similar(positive=[testword],topn=topn):
      counts2[wf_hkl[word]]+=1

    for (word,sim) in wv3.most_similar(positive=[testword],topn=topn):
      counts3[wf_hkl[word]]+=1
      
    for word in agreement(testword,wv1,wv2,topn):
      counts4[wf_hkl[word]]+=1
      
    for word in agreement(testword,wv1,wv3,topn):
      counts5[wf_hkl[word]]+=1
    
    for word in agreement(testword,wv2,wv3,topn):
      counts6[wf_hkl[word]]+=1

  return counts1,counts2,counts3,counts4,counts5,counts6
