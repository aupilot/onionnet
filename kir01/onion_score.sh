#!/bin/bash

DECOY=$1

cd /opt/var/ || exit
/usr/bin/python3 /opt/onionnet/kir01/prep_complex.py "$DECOY"
/usr/bin/python3 /opt/onionnet/generate_features.py -nt 0 -inp input.dat -out features.csv
# the huge weights file is stored on google drive and copied to a separate folder models_new
/usr/bin/python3 /opt/onionnet/predict.py -fn features.csv -out predicted.csv -weights /opt/onionnet/models_new/CNN_final_model_weights.h5 -scaler /opt/onionnet/models/StandardScaler.model
