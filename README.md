# Piecasso
Приложения для рисования "Piecasso"

Initial setup:

```
pyrcc5 resources.qrc -o resources_rc.py
pyuic5 mainwindow.ui -o MainWindow.py

pip3 install -r requirements.txt
pip3 install PyInstaller
pip3 install PyQt5 PyInstaller
pyinstaller --windowed --icon=icons/piecasso.ico --name Piecasso paint.py
pyinstaller Piecasso.spec
```
