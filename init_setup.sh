echo [$(date)] : "START"
echo [$(date)] : "CREATING THE CONDA ENV WITH PYTHON VERSION 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)] : "ACTIVATE ENV"
source activate ./env
echo [$(date)] : "INSTALLING REQIREMENTS"
pip install -r requirements.txt
echo [$(date)] : "END"