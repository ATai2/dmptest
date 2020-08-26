@echo off

title ¹ú×ÊÎ¯_9981
echo "start dmp..."

cd /d "%~dp0\apps"&&"%~dp0\java\amd64-win\bin\java" -Dloader.path="validate" -jar dmp-datafactory.jar
