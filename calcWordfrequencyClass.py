import math
import sys
import re

FREQMAXWORD=27124170 # corpus dependent: frequency of most frequent word

def get_hkl(freq):
  """ return word frequency class for a given word frequency """
  hkl=round(math.log(FREQMAXWORD/freq)/math.log(2))
  # tweaked to collect most frequent words in class 6 and merge the tail into class 21
  if hkl < 6:
    hkl = 6
  if hkl > 21:
    hkl = 21
  return hkl

wc_file="default"
if(len(sys.argv)>1):
  wc_file=sys.argv[1]
wc_pat=re.compile(" *(\d+) (.*)");
with open(wc_file,encoding='utf-8') as f:
  for line in f:
    l=wc_pat.match(line)
    if int(l.group(1)) > 9: # we only need the frequency class above cut-off threshold
      print("{}\t{}".format(get_hkl(int(l.group(1))),l.group(2)))
