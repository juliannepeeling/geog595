from gensim.models import Word2Vec

# test model
print('loading model...')
model = Word2Vec.load("assets/gay-seattle.w2v")
print("model details: ", model)
print('similar words to seattle:')
# print(model.wv.most_similar('capitol'))
print(model.wv.distances('seattle', ('gay', 'renton', 'lesbian', 'rain')))
print(model.wv.distance('seattle', 'civil'))
print(model.wv.distance('seattle', 'lesbian'))
print(model.wv.rank('seattle', 'gay'))
print(model.wv.rank('seattle', 'lesbian'))
# print(model.wv.distances('seattle'))
