import re,sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.text1 = QtWidgets.QTextEdit()
        self.text2 = QtWidgets.QTextEdit()
        self.le = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("Search")
        self.lbl = QtWidgets.QLabel("Insert text here:")
        self.lbl2 = QtWidgets.QLabel("Text found:")


        self.create_widgets()

    def create_widgets(self):

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.lbl)
        h_box.addStretch()
        h_box.addWidget(self.lbl2)
        h_box.addStretch()

        ht_box = QtWidgets.QHBoxLayout()
        ht_box.addStretch()
        ht_box.addWidget(self.text1)
        ht_box.addStretch()
        ht_box.addWidget(self.text2)
        ht_box.addStretch()

        hb_box = QtWidgets.QHBoxLayout()
        hb_box.addStretch()
        hb_box.addWidget(self.btn)
        hb_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(ht_box)
        v_box.addWidget(self.le)
        v_box.addLayout(hb_box)

        self.btn.clicked.connect(self.reg)



        self.setLayout(v_box)
        self.show()


    def search(self):

        email = re.compile(r"\w+\@\w+\.\w+")
        text = self.text1.toPlainText()
        mo = email.findall(text)
        self.text2.setText("\n".join(mo))

    def reg(self):
        tle = str(self.le.text())
        texto = self.text1.toPlainText()
        thing = re.compile(tle)
        mo = thing.findall(texto)
        self.text2.setText("\n".join(mo))

class Regapp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = Window()
        self.setCentralWidget(self.w)

        self.create_widgets()

    def create_widgets(self):

        bar = self.menuBar()

        file = bar.addMenu("File")
        regex = bar.addMenu("Regex")

        quit_action = QtWidgets.QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")

        email_action = QtWidgets.QAction("Email",self)
        postcode_action = QtWidgets.QAction("Post code",self)
        time_action = QtWidgets.QAction("Time",self)
        fullurl_action = QtWidgets.QAction("Url",self)
        isbn_action = QtWidgets.QAction("Isbn",self)
        credit_action = QtWidgets.QAction("Credit card",self)
        reg = [email_action, postcode_action, time_action, fullurl_action, isbn_action, credit_action ]

        file.addAction(quit_action)
        for i in reg:
            regex.addAction(i)


        quit_action.triggered.connect(self.quitt)
        for i in reg:
            i.triggered.connect(self.put_in_le)


        self.show()
        self.setWindowTitle("PyReg")

    def quitt(self):
        QtWidgets.qApp.exit()

    def put_in_le(self):
        signal = self.sender().text()

        if signal == "Email":
            self.w.le.setText(r"\w+\@\w+\.\w+")
        elif signal == "Post code":
            self.w.le.setText("[a-z]{1,2}\d{1,2}[a-z]?\s*\d[a-z]{2}")
        elif signal == "Time":
            self.w.le.setText("\d{1,2}:\d{1,2}(?:\s*[aApP]\.?[mM]\.?)?")
        elif signal == "Url":
            self.w.le.setText("https?://[-a-z0-9\.]{4,}(?::\d+)?/[^#?]+(?:#\S+)?")
        elif signal == "Isbn":
            self.w.le.setText("(?:[\d]-?){9}[\dxX]")
        elif signal == "Credit card":
            self.w.le.setText("5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}")
        else:
            print(signal)


app = QtWidgets.QApplication(sys.argv)
w = Regapp()
sys.exit(app.exec_())



