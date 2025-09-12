import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel
)
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator Sederhana")
        self.setGeometry(200, 200, 300, 200)

        # Layout utama
        layout = QVBoxLayout()

        # Input ekspresi
        self.input = QLineEdit()
        self.input.setPlaceholderText("Masukkan ekspresi, misal: 5+3*2")
        self.input.setAlignment(Qt.AlignRight)
        layout.addWidget(self.input)

        # Tombol operasi
        btn_layout = QHBoxLayout()
        self.btn_hitung = QPushButton("Hitung")
        self.btn_clear = QPushButton("Clear")
        self.btn_hitung.clicked.connect(self.hitung)
        self.btn_clear.clicked.connect(self.clear)
        btn_layout.addWidget(self.btn_hitung)
        btn_layout.addWidget(self.btn_clear)

        layout.addLayout(btn_layout)

        # Label hasil
        self.label_hasil = QLabel("Hasil akan ditampilkan di sini")
        self.label_hasil.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    def hitung(self):
        ekspresi = self.input.text()
        try:
            # Ganti simbol agar sesuai dengan Python
            ekspresi = ekspresi.replace("^", "**")  # pangkat
            hasil = eval(ekspresi)
            self.label_hasil.setText(f"Hasil: {hasil}")
        except ZeroDivisionError:
            self.label_hasil.setText("Error: Pembagian dengan nol!")
        except Exception:
            self.label_hasil.setText("Ekspresi tidak valid!")

    def clear(self):
        self.input.clear()
        self.label_hasil.setText("Hasil akan ditampilkan di sini")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Kalkulator()
    window.show()
    sys.exit(app.exec_())
