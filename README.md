# CPS-PA1
Using accelrometer in smartwatch to clarify hand_washing vs non_handwashing activities

To pull data from Smartwatch to local directory

adb shell 'ls /sdcard/wada/data/*.wada' | tr -d '\r' | xargs -n1 adb pull

To push config file from local directory to Smartwatch

adb push config.txt /sdcard/wada/config/

To convert .wada files into .csv files
java   -jar Wada.jar   acl   source_folder_path   destination_folder_path

To convert .csv files in .arff files
for file in `\ls csv-data`; do java -jar Wada.jar   arff  csv-data/$file; done


