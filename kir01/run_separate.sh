REC=1sy6_Fv.pdb
LIG=1sy6_epitope.pdb
#LIG=6zer_spike.pdb

./prepare_complex.sh $REC $LIG complex.pdb
python ../generate_features.py -nt 8 -inp input.dat -out features.csv
python ../predict.py -fn  features.csv -out predicted.csv -weights ../models/CNN_final_model_weights.h5 -scaler ../models/StandardScaler.model
cat predicted.csv