# CPS-PA1
Using accelrometer in smartwatch to clarify hand_washing vs non_handwashing activities

To pull data from Smartwatch to local directory

adb shell 'ls /sdcard/wada/data/*.wada' | tr -d '\r' | xargs -n1 adb pull

To push config file from local directory to Smartwatch

adb push config.txt /sdcard/wada/config/


