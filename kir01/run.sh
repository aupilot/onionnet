DECOY=e_dec_0.94.pdb

#python split_rec_lig.py $DECOY .
#python split_rec_lig.py $DECOY .
#pdb_selchain.py -A $DECOY > lig.pdb
#pdb_selchain.py -H,L $DECOY > rec.pdb
#./prepare_complex.sh rec.pdb lig.pdb complex.pdb
python prep_complex.py $DECOY
python ../generate_features.py -nt 0 -inp input.dat -out features.csv
python ../predict.py -fn  features.csv -out predicted.csv -weights ../../models/CNN_final_model_weights.h5 -scaler ../../models/StandardScaler.model
#cat predicted.csv
