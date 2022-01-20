# -*- coding: utf-8 -*-

from estexare import Estexare
from PySide6.QtWidgets import QApplication, QMainWindow
from main_form import Ui_MainWindow

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    es = Estexare()
    if es.errorMsg != '':
        ui.descriptionLbl.setText(es.errorMsg)
    else:
        def newEstexareBtnClick():
            newEs = es.newEstexare()
            ui.resultLbl.setText(newEs['fa_result'])
            ui.descriptionLbl.setText(newEs['fa_comment'])
            ui.suraLbl.setText(
              f"سوره: {newEs['sure']} ({newEs['sure_no']})"
            )
            ui.ayeLbl.setText(
              f"آیه: {newEs['aye_no']}"
            )
            ui.ayeTextLbl.setText(newEs['aye'])
        ui.newBtn.clicked.connect(newEstexareBtnClick)

    MainWindow.show()
    sys.exit(app.exec())
