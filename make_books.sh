#!/bin/bash
FORMAT="$1"
if [[ -z "$FORMAT" ]]; then
  FORMAT="pdf"
fi
if ! [ "$FORMAT" == "pdf" -o "$FORMAT" == "epub" ]; then
  exit
fi

#Torah
bash run.sh $FORMAT source_texts/Torah/1_Bereshit he
bash run.sh $FORMAT source_texts/Torah/1_Bereshit he cs

bash run.sh $FORMAT source_texts/Torah/2_Shemot he
bash run.sh $FORMAT source_texts/Torah/2_Shemot he cs

bash run.sh $FORMAT source_texts/Torah/3_Vayikra he
bash run.sh $FORMAT source_texts/Torah/3_Vayikra he cs

bash run.sh $FORMAT source_texts/Torah/4_Bemidbar he
bash run.sh $FORMAT source_texts/Torah/4_Bemidbar he cs

bash run.sh $FORMAT source_texts/Torah/5_Devarim he
bash run.sh $FORMAT source_texts/Torah/5_Devarim he cs

#Neviim
bash run.sh $FORMAT source_texts/Ktuvim/Daniel he
bash run.sh $FORMAT source_texts/Ktuvim/Daniel he cs

#Ktuvim
bash run.sh $FORMAT source_texts/Neviim/Yechezkel he
bash run.sh $FORMAT source_texts/Neviim/Yechezkel he cs

# Mishna
bash run.sh $FORMAT source_texts/Mishna/Avot he
bash run.sh $FORMAT source_texts/Mishna/Avot he en
bash run.sh $FORMAT source_texts/Mishna/Rosh_HaShanah he en
bash run.sh $FORMAT source_texts/Mishna/Yoma he en

# Midrash
bash run.sh $FORMAT source_texts/Midrash/Tanchuma/Korach he en

#Liturgy
bash run.sh $FORMAT source_texts/Liturgy/Unetaneh_Tokef he en
