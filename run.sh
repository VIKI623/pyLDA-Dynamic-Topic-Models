#!/usr/bin/env bash

echo 'install dependencies ...'
pip install numpy
pip install scipy
pip install IPython
pip install -U gensim
pip install pyLDAvis
echo 'done!'

echo 'run dtm model ...'
python dtm.py
echo 'done!'