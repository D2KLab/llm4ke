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
import logging

# === Init ====================================================================

model = SentenceTransformer("all-MiniLM-L6-v2")

SIMILARITY_THRESHOLD = 0.6
ROOT_PRED = 'data_out'
ROOT_INPUT = 'data'

# ----------------------------------------------------------------------------

logBaseName = "eurecom.llm4ke.prompt"
logFileName = logBaseName + ".log"

loggingFormatString = (
    "%(asctime)s:%(levelname)s:%(threadName)s:%(funcName)s:%(message)s"
)


# === Functions ===============================================================

def run_single(
        input_path,
        prediction_path,
        threshold=SIMILARITY_THRESHOLD):
    """
    Compute similarity score based on embeddings for a given set of Competency Questions.

    :param input_path:
    :param prediction_path:
    :param threshold:
    :return:
    """

    logging.debug("PROCESS:RUN_PREDICTION:input_path=%s:prediction_path=%s", input_path, prediction_path)

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
        logging.debug("PROCESS:RUN_PREDICTION:STATS:prediction_path=%s:pair_score(%s - %s)=%s", prediction_path, i, j, pair["score"])

    logging.debug("PROCESS:RUN_PREDICTION:STATS:prediction_path=%s:true_positive=%s", prediction_path, true_positive)

    precision = len(set(true_positive)) / len(predictions)
    logging.debug("PROCESS:RUN_PREDICTION:STATS:prediction_path=%s:precision=%s", prediction_path, str(precision * 100) + '%')

    return precision


def run_onto(
        onto_name,
        threshold=SIMILARITY_THRESHOLD):
    """
    Orchestrate similarity analysis for a given ontology by looking at all the related sets of Competency Questions.

    :param onto_name: the name of the ontology to scrutinize
    :param threshold: the report threshold
    :return: a data structure with ontology, LLM and scores
    """

    logging.debug("PROCESS:SPECIFIC_ONTO:onto_name=%s", onto_name)
    scores = []

    for mode in tqdm(os.listdir(path.join(ROOT_PRED, onto_name))):
        if mode == 'archive' or not path.isdir(path.join(ROOT_PRED, onto_name, mode)):
            continue
        for file in os.listdir(path.join(ROOT_PRED, onto_name, mode)):
            if not file.endswith('.txt'):
                continue
            prediction_path = path.join(ROOT_PRED, onto_name, mode, file)
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
    """
    Orchestrate similarity analysis for all available ontologies by looking at all their related sets of Competency Questions.

    :param threshold: the report threshold
    :return: a data structure with ontologies, LLMs and scores
    """
    res = [run_onto(onto, threshold)
           for onto in os.listdir(ROOT_PRED)
           if path.isdir(path.join(ROOT_PRED, onto))]
    return flatten(res)


# === Main ====================================================================

if __name__ == '__main__':

    # Define argument parser
    parser = ArgumentParser(
        description='Evaluate output on the base of a ground truth.'
    )
    parser.add_argument(
        'name',
        help='Name of the ontology to evaluate or "all".',
        default="all"
    )
    parser.add_argument(
        '-t-',
        '--threshold',
        type=float,
        help='Similarity threshold to apply.',
        default=SIMILARITY_THRESHOLD
    )
    parser.add_argument(
        "--log",
        type=int,
        choices=[10, 20, 30, 40, 50],
        action="store",
        default=20,
        help="Verbosity (default: INFO) : DEBUG = 10, INFO = 20, WARNING = 30, ERROR = 40, CRITICAL = 50",
    )

    # Instanciate argument parser
    args = parser.parse_args()

    # Configure logger
    logging.basicConfig(
        format=loggingFormatString,
        level=args.log
    )

    # Call the processing function
    logging.info("PROCESS:START:name=%s:threshold=%s", args.name, args.threshold)
    if args.name != 'all':
        res = run_onto(args.name, args.threshold)
    else:
        res = run_all(args.threshold)
    logging.debug("PROCESS:RESULTS:res=%s", res)

    # Save results
    outfile_path = f"results_{args.name}.json"
    with open(outfile_path, "w") as outfile:
        outfile.write(json.dumps(res, indent=4))
    logging.info("SAVE:RESULTS:outfile_path=%s", outfile_path)

    logging.info("DONE")
