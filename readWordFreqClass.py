import re
wc_pat=re.compile(" *(\d+)\t(.*)");
wf_hkl={} # for lookup of word frequency class of a word
hklwl=[]  # for lookup of list of words of a given frequency class
i=0;
while i<22:
  hklwl.append([])
  i+=1
# types.hkl contains prepared word frequency class list
with open("types.hkl",encoding='utf-8') as f:
  for line in f:
    l=wc_pat.match(line)
    wf_hkl.update({l.group(2): int(l.group(1))})
    hklwl[int(l.group(1))].append(l.group(2))
