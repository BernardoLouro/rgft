from rouge import Rouge
import json

filename = 'file_name'

results = {}

with open(f'./rouge/{filename}.json', 'r') as f:
    data = json.load(f)

hyps, refs = map(list, zip(*[[d['hyp'], d['ref']] for d in data]))

rouge = Rouge()
scores = rouge.get_scores(hyps, refs, avg=True)
print(scores)

with open(f'./rouge/{filename}_results.json', 'w') as results:
    json.dump(scores, results)


