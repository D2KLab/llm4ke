from argparse import ArgumentParser
from os import path

import yaml
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

SIMILARITY_THRESHOLD = 0.3  # TODO TO BE CHANGED


def run(input_path, prediction_path):
    with open(path.join(input_path, 'cqs', 'cqs.yml')) as f:
        ground_truth = yaml.safe_load(f)
    cqs = [c['question'] for c in ground_truth['ontology']['cqs']]

    with open(prediction_path) as f:
        predictions = f.readlines()

    # Compute embeddings
    gt_embeddings = model.encode(cqs, convert_to_tensor=True)
    pred_embeddings = model.encode(predictions, convert_to_tensor=True)

    # Compute cosine-similarities for each sentence with each other sentence
    cosine_scores = util.cos_sim(gt_embeddings, pred_embeddings)
    # Find the pairs with the highest cosine similarity scores
    pairs = []
    for i in range(len(cosine_scores)):
        for j in range(len(cosine_scores[0])):
            pairs.append({"index": [i, j], "score": cosine_scores[i][j]})

    # Sort scores in decreasing order
    pairs = sorted(pairs, key=lambda x: x["score"], reverse=True)
    true_positive = []

    for pair in pairs:
        i, j = pair["index"]
        if pair['score'] > SIMILARITY_THRESHOLD:
            true_positive.append(j)
            # print("{} \t\t {} \t\t Score: {:.4f}".format(
            #     cqs[i], predictions[j], pair["score"]
            # ))
        # print(f'{i} - {j} => {pair["score"]}')

    print(true_positive)
    precision = len(set(true_positive)) / len(predictions)
    print(str(precision * 100) + '%')

    return precision


