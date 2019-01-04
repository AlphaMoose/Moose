import operator
scores = []
scores.append({'name':'No Record', 'score':0})
scores = sorted(scores, key=lambda k: k["score"], reverse=True)

scores.append({'name':' moose', 'score': 1500})
scores = sorted(scores, key=lambda k: k['score'], reverse=True)
