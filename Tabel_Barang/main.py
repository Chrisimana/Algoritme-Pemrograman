import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
)


class TabelBarang(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Barang")
        self.setGeometry(200, 200, 400, 300)

        # Layout utama
        layout = QVBoxLayout()

        # Input form
        form_layout = QHBoxLayout()
        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText("Nama Barang")
        self.harga_input = QLineEdit()
        self.harga_input.setPlaceholderText("Harga Barang")
        self.btn_tambah = QPushButton("Tambah")
        self.btn_tambah.clicked.connect(self.tambah_data)

        form_layout.addWidget(QLabel("Barang:"))
        form_layout.addWidget(self.nama_input)
        form_layout.addWidget(QLabel("Harga:"))
        form_layout.addWidget(self.harga_input)
        form_layout.addWidget(self.btn_tambah)

        # Tabel
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Nama Barang", "Harga"])

        # Tambahkan ke layout
        layout.addLayout(form_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def tambah_data(self):
        nama = self.nama_input.text().strip()
        harga = self.harga_input.text().strip()

        if nama and harga:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(nama))
            self.table.setItem(row, 1, QTableWidgetItem(harga))

            # Kosongkan input setelah tambah
            self.nama_input.clear()
            self.harga_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabelBarang()
    window.show()
    sys.exit(app.exec_())
