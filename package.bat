@ECHO OFF
cls
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --add-data "F:/pranavs/Projects/mycontacts/contact-management/contacts;contacts/"  "F:/pranavs/Projects/mycontacts/contact-management/ui.py"