# Required Software

For the following project I will be using Python 3.10.12, Matplotlib 3.9.2.

Installing python for Ubuntu can be done from the command line by using as such:
```commandline
sudo apt-get update
sudo apt-get install python3.10
```
NOTE: This installation may differ from your linux distribution, please follow the instructions
provided by your system documentation.

Installing the numpy library can be done using pip from any terminal as follows:
```commandline
pip install matplotlib
```
Or if you want to install a certain version of numpy:
```commandline
pip install --force-reinstall matplotlib==3.9.2
```

For testing the python and numpy versions we can use the following code:
```python
import platform
import matplotlib as mp
print("Python version: ", platform.python_version())
print("Matplotlib version: ", mp.__version__)

```