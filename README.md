# Keras_MLP-GRU_Regressor

## Introduction
This is my contribution for the master's degree thesis. In this project I present two types of nonlinear regressors for predicting time series. The first one is implemented with a classic Multi Layer Perceptron Neural Network (MLP). The second one is implemented with a Recurrent Neural Network, Gated Recurrent Unit (GRU) scheme.
At first I focused only on Forex price time series and later extended my interest in Crypto / Fiat price time series.

The purpose of this project is to show an easy way to create a good dataset, to train the desired model (MLP or GRU) and to use it in real time forecasting.

## Requirements
If you have a GPU with support to CUDA i strongly recommend to install:
* See this [guide](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4KKVroazE) to install CUDA
* Download and set up [CUDA-Toolkit](https://developer.nvidia.com/cuda-downloads)
To correctly execute the program we need to install and set up:
* _Python3_, _Tensorflow_ and _Keras_. I found a great presentation made by [Jaff Hauton](https://github.com/jeffheaton) using Anaconda, follow the guide [here](https://www.youtube.com/watch?v=dj-Jntz-74g).  If you prefer a classic installation type the following commands (Debian/Ubuntu):
  * $ sudo apt-get update
  * $ sudo apt-get install python3.8
* verify _python_ and _pip_ installation:
  * $ python --version 
  * $ pip --version 
* If the installation is done type:
  * $ pip install --upgrade tensorflow tensorflow-gpu
* _PyWavelets_ is a useful python package apply wavelet decomposition to time series, [pywt](https://pywavelets.readthedocs.io/en/latest/)

The project is composed by some parts that allow the user to clean and construct a dataset. Starting from the Tick prices movements (i.e. each price movements registered into a minute), construct a 1 minute price movements (one can choose if use Open, Close, High or Low price). During the preparation of the data, will be created two time series. The first will be formed by a sequence of prices chossen, the second one will be formed by a smoothed version of the same price.

# Work in progress...
