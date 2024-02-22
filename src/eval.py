#  Copyright 2024. EURECOM
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# === Import ==================================================================
import os
import json
from os import path
from tqdm import tqdm
from argparse import ArgumentParser
import yaml
from sentence_transformers import SentenceTransformer, util
from utils import flatten

# === Init ====================================================================

model = SentenceTransformer("all-MiniLM-L6-v2")

SIMILARITY_THRESHOLD = 0.6
ROOT_PRED = 'data_out'
ROOT_INPUT = 'data'


# === Functions ===============================================================

def run_single(input_path, prediction_path, threshold=SIMILARITY_THRESHOLD):
    with open(prediction_path) as f:
        predictions = f.readlines()

    if len(predictions) <= 0:
        return 0

    with open(path.join(input_path, 'cqs', 'cqs.yml')) as f:
        ground_truth = yaml.safe_load(f)
    cqs = [c['question'] for c in ground_truth['ontology']['cqs']]

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
        if pair['score'] > threshold:
            true_positive.append(j)
            # print("{} \t\t {} \t\t Score: {:.4f}".format(
            #     cqs[i], predictions[j], pair["score"]
            # ))
        # print(f'{i} - {j} => {pair["score"]}')

    # print(true_positive)
    precision = len(set(true_positive)) / len(predictions)
    # print(str(precision * 100) + '%')

    return precision


def run_onto(onto_name, threshold=SIMILARITY_THRESHOLD):
    print(onto_name)
    scores = []

    for mode in tqdm(os.listdir(path.join(ROOT_PRED, onto_name))):
        if mode == 'archive' or not path.isdir(path.join(ROOT_PRED, onto_name, mode)):
            continue
        for file in os.listdir(path.join(ROOT_PRED, onto_name, mode)):
            if not file.endswith('.txt'):
                continue
            prediction_path = path.join(ROOT_PRED, onto_name, mode, file)
            # print(prediction_path)
            input_path = path.join(ROOT_INPUT, onto_name)

            score = run_single(input_path, prediction_path, threshold)

            parts = file.split('_')
            llm = parts[1]
            xpl = parts[2].replace('.txt', '')

            scores.append({
                'onto': onto_name,
                'llm': llm,
                'mode': mode,
                'examples': xpl,
                'score': score
            })

    return scores


def run_all(threshold=SIMILARITY_THRESHOLD):
    res = [run_onto(onto, threshold)
           for onto in os.listdir(ROOT_PRED)
           if path.isdir(path.join(ROOT_PRED, onto))]
    return flatten(res)


parser = ArgumentParser(description='Evaluate output on the base of a ground truth.')
parser.add_argument('name', help='Name of the ontology to evaluate or "all".', default="all")
parser.add_argument('-t-', '--threshold', type=int, help='Similarity threshold to apply.', default=SIMILARITY_THRESHOLD)

args = parser.parse_args()

if args.name != 'all':
    res = run_onto(args.name, args.threshold)
else:
    res = run_all(args.threshold)

with open(f"results_{args.name}.json", "w") as outfile:
    outfile.write(json.dumps(res, indent=4))
