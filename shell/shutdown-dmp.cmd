@echo off&setlocal EnableDelayedExpansion  
set Port=
set Dstport=9981
 
for /F "usebackq skip=4 tokens=2,5" %%a in (`"netstat -ano -p tcp"`) do (  
  for /F "tokens=2 delims=:" %%k in ("%%a") do (  
    set  Port=%%k  
  )  
  echo !Port! %%b >>portandpid.tmp  
)  
for /F "tokens=2 delims=:" %%c in ("%1") do (  
    set  Port=%%c  
  )  
for /F "tokens=1,2 delims= " %%d in (portandpid.tmp) do (  
    echo %%d   
    echo %Dstport%  
    if %%d == %Dstport% taskkill /f /pid %%e  
  )  
del portandpid.tmp
set Port=  
set Dstport=  
goto :eof
 
echo '结束了'
pause