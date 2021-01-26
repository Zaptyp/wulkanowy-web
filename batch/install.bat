::To jest to samo co w pliku install.exe
pip install -r requirements.txt
echo SECRET_KEY = VULCANWEBKEY > .env
::Kiedyś to SECRET_KEY będzie generowany przez skrypt NIE RUSZAĆ!!!
::setLocal EnableDelayedExpansion
::set str=ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
::set /a P=!random!%%36
::set znak1=!str:~%P%,1!
::set /a P=!random!%%36
::set znak2=!str:~%P%,1!
::set /a P=!random!%%36
::set znak3=!str:~%P%,1!
::set /a P=!random!%%36
::set znak4=!str:~%P%,1!
::set /a P=!random!%%36
::set znak5=!str:~%P%,1!
::set /a P=!random!%%36
::set znak6=!str:~%P%,1!
::set /a P=!random!%%36
::set znak7=!str:~%P%,1!
::set /a P=!random!%%36
::set znak8=!str:~%P%,1!
::set /a P=!random!%%36
::set znak9=!str:~%P%,1!
::set "key=%znak1%%znak2%%znak3%%znak4%%znak5%%znak6%%znak7%%znak8%%znak9%"
::echo SECRET_KEY = %key% > .env
python manage.py makemigrations
python manage.py migrate
npm install
pause
