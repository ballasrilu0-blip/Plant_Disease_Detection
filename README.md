\# Plant Disease Detection



Plant Disease Detection system using EfficientNetB0 and TensorFlow/Keras.



\## Project Overview



This project detects plant diseases from leaf images using a trained EfficientNetB0 deep learning model.



The system currently supports 62 classes.



\## Features



\- EfficientNetB0 transfer learning

\- Fine-tuning

\- 62 plant/disease classes

\- Training, validation and testing datasets

\- Class-weight handling

\- Model evaluation

\- Image prediction

\- Python prediction interface

\- Prepared for future Flutter application integration



\## Project Structure



```text

Plant\_Disease\_Detection/

│

├── dataset/

│

├── models/

│   ├── final\_model.keras

│   ├── labels.txt

│   └── class\_indices.pkl

│

├── reports/

├── logs/

├── web\_app/

│

├── train.py

├── predict.py

├── evaluate.py

├── preprocess.py

├── split\_dataset.py

├── check\_database.py

├── requirements.txt

├── README.md

└── .gitignore

