counts_glove=[]
counts_sg=[]
counts_cbow=[]
counts_agre_g_s=[]
counts_agre_g_c=[]
counts_agre_s_c=[]
for hkl in range(6,22):
  print(hkl)
  (counts1,counts2,counts3,counts4,counts5,counts6)=test(wv_glove,wv_sg,wv_cbow,hkl,1000,10)
  counts_glove.append([hkl] + counts1[6:])
  counts_sg.append([hkl] + counts2[6:])
  counts_cbow.append([hkl] + counts3[6:])
  counts_agre_g_s.append([hkl] + counts4[6:])
  counts_agre_g_c.append([hkl] + counts5[6:])
  counts_agre_s_c.append([hkl] + counts6[6:])
