# Handwriting-Recognition-CS584

## Datasets
For now, datasets are stored in a One Drive folder
[here](https://iit0-my.sharepoint.com/:f:/g/personal/nbaxley_hawk_iit_edu/EtW6kD2M6YBNvg9AGPC0L-cBM1f6evyl5a6kyOFdXgZVGw?e=fEVD7n).
Just download the zip files and then unzip them into the Datasets folder directory (see the README there)

## Setting up Venv
We'll follow these steps to try and keep our environments consistent 
```
python -m venv venv
venv\Scripts\activate
```
Currently, the requirements.txt file is invalid. For now, just install the libraries manually.
```
pip install tensorflow seaborn numpy pandas
```

## Python
Yet to decide on the version of Python we should use, but ideally set this up in
a venv environment to keep versions consistent across all of our machines. Do
```
pip install -r requirements
```
to install all the libraries we are using. The main ones are TensorFlow, Keras
and can't forget numpy and pandas