from inspect import getframeinfo, stack

annotators=['tokenize','ssplit','pos','lemma','depparse','ner']+\
           ['natlog','openie']
trace=1
force=0

class talk_params:
  def __init__(self):
    self.force = False

    self.sum_count = 4
    self.key_count = 10
    self.max_answers = 6
    self.cloud_size = 24
    self.subgraph_size = 38

    self.quiet = True
    self.answers_by_rank = True

    self.pers = True
    self.expand_query = 2
    self.guess_wh_word_NERs=0

    self.compounds = True
    self.svo_edges = True
    self.subject_centered = True

    self.show_pics = 1  # 1 : just generate files, 2: interactive
    self.show_rels = 0
    self.to_prolog = 0
    
    self.think_depth=5

# decides between '_' and ' ' as separator
#def join(*xs) : return ' '.join(xs)
def join(*xs) : return xs

def ppp(*args) :
  if trace<1 : return
  caller = getframeinfo(stack()[1][0])

  print('DEBUG:',
        caller.filename.split('/')[-1],
        '->',caller.lineno,end=': ')
  print(*args)
