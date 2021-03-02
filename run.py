import sys
import json
import os

sys.path.insert(0, 'src')
from etl import move_data
from eda import main_eda
from utils import convert_notebook
from evaluate import find_best_model

def main(targets):

    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/eda-params.json'))
    evaluate_config = json.load(open('config/evaluate-params.json'))
    inference_config = json.load(open('config/inference-params.json'))
    test_config = json.load(open('config/test-params.json'))
