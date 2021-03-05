import sys
import json
import os
import cv2

sys.path.insert(0, 'src')
from etl import copy_data
#from eda import main_eda
#from utils import convert_notebook
from compare import view_results
#from evaluate import runtime_performance_eval

def main(targets):

    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/eda-params.json'))
    comparison_config = json.load(open('config/comparison-params.json'))
    #evaluate_config = json.load(open('config/evaluate-params.json'))
    test_config = json.load(open('config/test-params.json))

    if 'data' in targets:
        copy_data(**data_config)
        
    
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
        baseline_runtime_performance = runtime_performance_eval(**evaluate_config)
        tuned_runtime_performance = runtime_performanc_eval(**evaluate_config)
        
    
    if 'test' in targets:
        move_data(**test_config)
        main_eda(data, **eda_config)
        convert_notebook(**eda_config)
        view_results(**comparison_config)
        baseline_runtime_performance = runtime_performance_eval(**evaluate_config)
        tuned_runtime_performance = runtime_performanc_eval(**evaluate_config)
        print("Baseline runtime performance: {}".format(baseline_runtime_performance))
        print("Best tuned runtime performance: {}".format(tuned_runtime_performance))
        
        
    if 'all' in targets:
        move_data(**data_config)
        main_eda(data, **eda_config)
        convert_notebook(**eda_config)
        view_results(**comparison_config)
        baseline_runtime_performance = runtime_performance_eval(**evaluate_config)
        tuned_runtime_performance = runtime_performanc_eval(**evaluate_config)
        print("Baseline runtime performance: {}".format(baseline_runtime_performance))
        print("Best tuned runtime performance: {}".format(tuned_runtime_performance))
    
if __name__ == '__main__':
    
    targets = sys.argv[1:]
    main(targets)
