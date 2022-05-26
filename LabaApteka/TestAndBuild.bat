@echo off 
set a=1
set emptyrow=! 
set good=TEST COMPLETED, BUILD COMPLETED 
set good=TEST COMPLETED, BUILD COMPLETED
set bad=TEST NOT COMPLETED, BUILD NOT START
pytest test_all.py>TestLog.txt
findstr "FAILURES"  TestLog.txt>pupa.txt
set /p pupa=< pupa.txt
del pupa.txt
if defined pupa (echo %emptyrow% & echo %emptyrow% & echo %bad%) else (@pyinstaller --noconfirm GUI.py & echo %emptyrow% & echo %emptyrow% & echo %good%)
pause