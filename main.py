from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
import firewall

class FirewallApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Firewall Rule Generator")
        self.layout = QVBoxLayout()

        self.protocol = QComboBox()
        self.protocol.addItems(["tcp", "udp"])
        self.layout.addWidget(QLabel("Protocol"))
        self.layout.addWidget(self.protocol)

        self.port = QLineEdit()
        self.layout.addWidget(QLabel("Port"))
        self.layout.addWidget(self.port)

        self.action = QComboBox()
        self.action.addItems(["ACCEPT", "DROP"])
        self.layout.addWidget(QLabel("Action"))
        self.layout.addWidget(self.action)

        self.button = QPushButton("Apply Rule")
        self.button.clicked.connect(self.apply_rule)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def apply_rule(self):
        protocol = self.protocol.current
