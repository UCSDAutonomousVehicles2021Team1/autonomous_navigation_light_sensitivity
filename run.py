import sys
import json
import os
import cv2

sys.path.insert(0, 'src')
#from etl import move_data
#from eda import main_eda
#from utils import convert_notebook
from compare import view_results
#from evaluate import find_best_model

def main(targets):

    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/eda-params.json'))
    comparison_config = json.load(open('config/comparison-params.json'))
    evaluate_config = json.load(open('config/evaluate-params.json'))

    if 'data' in targets:
        move_data(**data_config)
        
    
    if 'eda' in targets:
        try:
            data
        except NameError:
            data = cv2.imread(data_config['data_fp'])
            
        main_eda(data, **eda_config)
        # Execute notebook, convert to HTML
        convert_notebook(**eda_config)
        
        
        
    if 'comparison' in targets:
        view_results(**comparison_config)
        
    
    if 'evaluate' in targets:
        best_tuning_result = find_best_model(model_names, **evaluate_config)
        
    
    if 'test' in targets:
        move_data(**data_config)
        main_eda(data, **eda_config)
        convert_notebook(**eda_config)
        model_names = compare_images(**comparison_config)
        best_tuning_result = find_best_model(model_names, **evaluate_config)
        print("Found best tuning result: {}".format(best_tuning_result))
        
    
if __name__ == '__main__':
    
    targets = sys.argv[1:]
    main(targets)
