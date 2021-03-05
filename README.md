# autonomous_navigation_light_sensitivity

Evaluation of Intel Realsense D455 Depth camera's sensitivity to light. Focuses on the tuning work of camera configuration settings with ROS rqt plugin by using SSIM and MSE as a metric to find the best parameter combination that displays high structural similarity to the image under default setting conditions (non-bright).

To run the repository, run ```python run.py test```

## What does it do


## Targets

1. data:

Allows you to move data into the main repository.

2. eda:

Runs a basic EDA on the data.

3. comparison:

Performs and displays comparative metric results between our baseline (non-bright vs. bright under default settings) and tuned (non-bright under default settings vs. bright under tuned settings) data.

4. evaluate:



5. test:

Runs all the previous targets on test data to confirm that all the results we output is shown in the main repository.
