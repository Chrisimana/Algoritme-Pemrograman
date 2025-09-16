import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)


class InvestasiApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Penghitung Investasi")
        self.setGeometry(200, 200, 400, 200)

        # Layout utama
        layout = QVBoxLayout()

        # Input Modal
        layout_modal = QHBoxLayout()
        self.input_modal = QLineEdit()
        self.input_modal.setPlaceholderText("Modal awal")
        layout_modal.addWidget(QLabel("Modal (Rp):"))
        layout_modal.addWidget(self.input_modal)

        # Input Bunga
        layout_bunga = QHBoxLayout()
        self.input_bunga = QLineEdit()
        self.input_bunga.setPlaceholderText("Bunga per tahun (%)")
        layout_bunga.addWidget(QLabel("Bunga (%):"))
        layout_bunga.addWidget(self.input_bunga)

        # Input Tahun
        layout_tahun = QHBoxLayout()
        self.input_tahun = QLineEdit()
        self.input_tahun.setPlaceholderText("Lama investasi (tahun)")
        layout_tahun.addWidget(QLabel("Tahun:"))
        layout_tahun.addWidget(self.input_tahun)

        # Tombol hitung
        self.btn_hitung = QPushButton("Hitung")
        self.btn_hitung.clicked.connect(self.hitung_investasi)

        # Label hasil
        self.label_hasil = QLabel("Hasil akhir investasi akan ditampilkan di sini.")

        # Tambahkan semua ke layout
        layout.addLayout(layout_modal)
        layout.addLayout(layout_bunga)
        layout.addLayout(layout_tahun)
        layout.addWidget(self.btn_hitung)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    def hitung_investasi(self):
        try:
            modal = float(self.input_modal.text())
            bunga = float(self.input_bunga.text()) / 100
            tahun = int(self.input_tahun.text())

            # Rumus bunga majemuk: A = P * (1 + r)^t
            hasil = modal * ((1 + bunga) ** tahun)

            self.label_hasil.setText(
                f"Hasil akhir setelah {tahun} tahun: Rp {hasil:,.2f}"
            )
        except ValueError:
            self.label_hasil.setText("Input tidak valid! Harap masukkan angka yang benar.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvestasiApp()
    window.show()
    sys.exit(app.exec_())
