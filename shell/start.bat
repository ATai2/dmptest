echo "start bengin"
echo "download preposed-machine.jar"
curl -o %~dp0\preposed-machine.jar http://10.110.87.202:9998/preposed-machine.jar  && echo "preposed-machine.jar finished" ||  echo " preposed-machine.jar  failed"

echo "download preposed-machine.jar"
curl -o %~dp0\dmp-datafactory.jar http://10.110.87.202:9998/dmp-datafactory.jar  && echo "dmp-datafactory.jar finished" ||  echo " dmp-datafactory.jar  failed"

