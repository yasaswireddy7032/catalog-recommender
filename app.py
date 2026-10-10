import json,math
from collections import Counter,defaultdict
class Recommender:
    def __init__(self,events):
        self.users=defaultdict(set);self.items=defaultdict(set)
        for user,item in events:self.users[user].add(item);self.items[item].add(user)
        self.popularity=Counter({item:len(users) for item,users in self.items.items()})
    def similarity(self,a,b):
        x=self.items.get(a,set());y=self.items.get(b,set())
        return len(x&y)/math.sqrt(len(x)*len(y)) if x and y else 0
    def recommend(self,user,k=3):
        if k<1:raise ValueError('Positive k required')
        seen=self.users.get(user,set());rows=[]
        for item in self.items:
            if item in seen:continue
            reasons=sorted([(self.similarity(item,s),s) for s in seen],reverse=True)
            score=sum(s for s,_ in reasons)
            rows.append({'item':item,'score':score,'reason':f'co-occurs with {reasons[0][1]}' if reasons and reasons[0][0]>0 else 'popularity fallback','popularity':self.popularity[item]})
        return sorted(rows,key=lambda r:(-r['score'],-r['popularity'],r['item']))[:k]

def evaluate(train,holdout,k=3):
    if not holdout:raise ValueError('Holdout required')
    model=Recommender(train);recalls=[];ndcgs=[]
    for user,expected in holdout.items():
        if not expected:raise ValueError('Expected items required')
        if set(expected)&model.users.get(user,set()):raise ValueError('Train/test interaction leakage')
        hits=[r['item'] in expected for r in model.recommend(user,k)]
        recalls.append(sum(hits)/len(expected));ideal=sum(1/math.log2(i+2) for i in range(min(k,len(expected))))
        ndcgs.append(sum(v/math.log2(i+2) for i,v in enumerate(hits))/ideal)
    return {'recall_at_k':sum(recalls)/len(recalls),'ndcg_at_k':sum(ndcgs)/len(ndcgs),'users':len(holdout),'k':k}
if __name__=='__main__':
    events=[('a','python'),('a','ml'),('b','python'),('b','ml'),('b','cloud'),('c','cloud'),('c','data')]
    print(json.dumps({'recommendations':Recommender(events).recommend('a'),'evaluation':evaluate(events,{'a':['cloud']})},indent=2))
