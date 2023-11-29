# Multilabel Semantic Segmentation X-ray images 

## Overview
This project is focused on multilabel semantic segmentation using deep learning techniques, specifically within the field of medical radiology. The objective of this internship project was to explore state-of-the-art models in semantic segmentation and develop a tool for testing a multitude of multilabel semantic segmentation models. The goal was to mimic the precision of a physician in radiology by not only recognizing pathologies in images but also accurately segmenting bones to pinpoint the location of pathologies.

## Installation and Dependencies
This project utilizes the `mmsegmentation` repository, a versatile toolkit for semantic segmentation. Ensure you have Python installed and then clone the `mmsegmentation` repository:

```bash
git clone https://github.com/open-mmlab/mmsegmentation.git
cd mmsegmentation
pip install -r requirements.txt
```

## Project Structure
The project involves developing and testing various deep learning models, including convolutional neural networks and transformers, for semantic segmentation tasks. The repository is structured as follows:

- `models/`: Contains various semantic segmentation models.
- `data/`: Dataset directories used in experiments.
- `experiments/`: Scripts and notebooks for training and testing models.
- `results/`: Output results and comparative analysis of different models.

## Usage
To use this toolkit:

1. Prepare your dataset according to the `mmsegmentation` guidelines.
2. Choose or create a configuration file for the model you want to test.
3. Run the training/testing script with the chosen configuration.

```bash
python tools/train.py configs/your_model_config.py
```

## Experimentation and Results
The internship focused on testing and comparing various models to find the most suitable one for specific semantic segmentation tasks in medical radiology. The results are documented in detailed reports in the `results/` directory.

## Contributing
Contributions to improve the models, add new datasets, or enhance the existing documentation are welcome. Please refer to the contributing guidelines in the `mmsegmentation` repository for more details.

## License
This project inherits the license from the `mmsegmentation` repository. Please refer to their license file for more information.

## Acknowledgements
- The team at [mmsegmentation](https://github.com/open-mmlab/mmsegmentation) for providing the segmentation toolkit.
- My mentors and colleagues at @Milvue during the internship for their guidance and support.
