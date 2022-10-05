#!/bin/bash
FORMAT="$1"
if [[ -z "$FORMAT" ]]; then
  FORMAT="pdf"
fi
if ! [ "$FORMAT" == "pdf" -o "$FORMAT" == "epub" ]; then
  exit
fi

#Torah
bash run $FORMAT source_texts/Torah/1_Bereshit he
bash run $FORMAT source_texts/Torah/1_Bereshit he cs

bash run $FORMAT source_texts/Torah/2_Shemot he
bash run $FORMAT source_texts/Torah/2_Shemot he cs

bash run $FORMAT source_texts/Torah/3_Vayikra he
bash run $FORMAT source_texts/Torah/3_Vayikra he cs

bash run $FORMAT source_texts/Torah/4_Bemidbar he
bash run $FORMAT source_texts/Torah/4_Bemidbar he cs

bash run $FORMAT source_texts/Torah/5_Devarim he
bash run $FORMAT source_texts/Torah/5_Devarim he cs

bash run $FORMAT source_texts/Mishna/Avot he
bash run $FORMAT source_texts/Mishna/Avot he en --one-per-page

bash run $FORMAT source_texts/Mishna/Yoma he
bash run $FORMAT source_texts/Mishna/Yoma he en --one-per-page

bash run $FORMAT source_texts/Mishna/Berachot he
bash run $FORMAT source_texts/Mishna/Berachot he en --one-per-page
