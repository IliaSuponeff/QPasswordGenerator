from PySide6.QtGui import QPixmap, QIcon, QClipboard
from ui.main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
import sys, os, random


class PasswordGenerator:

    LOWER_SYMBOLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UPPER_SYMBOLS = [symbol.upper() for symbol in LOWER_SYMBOLS]
    NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    SPECIAL_SYMBOLS = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    MIN_LENGTH = 8
    MAX_LENGTH = 32

    def __init__(self) -> None:
        self._psw_length = 8
        self._lowercase_mode = False
        self._uppercase_mode = False
        self._special_symbols_mode = False
    
    @property
    def psw_length(self) -> int:
        return self._psw_length

    @psw_length.setter
    def psw_length(self, value: int) -> None:
        if not(self.MIN_LENGTH <= value <= self.MAX_LENGTH):
            return
        
        self._psw_length = value

    @property
    def lowercase_mode(self) -> bool:
        return self._lowercase_mode

    @lowercase_mode.setter
    def lowercase_mode(self, value: bool) -> None:
        self._lowercase_mode = bool(value)

    @property
    def uppercase_mode(self) -> bool:
        return self._uppercase_mode

    @uppercase_mode.setter
    def uppercase_mode(self, value: bool) -> None:
        self._uppercase_mode = bool(value)

    @property
    def special_symbols_mode(self) -> bool:
        return self._special_symbols_mode

    @special_symbols_mode.setter
    def special_symbols_mode(self, value: bool) -> None:
        self._special_symbols_mode = bool(value)

    @property
    def special_symbols_mode(self) -> bool:
        return self._special_symbols_mode

    @special_symbols_mode.setter
    def special_symbols_mode(self, value: bool) -> None:
        self._special_symbols_mode = bool(value)

    def generate_password(self) -> str:
        symbols = self.NUMBERS
        if self.lowercase_mode:
            symbols += self.LOWER_SYMBOLS
        if self.uppercase_mode:
            symbols += self.UPPER_SYMBOLS
        if self.special_symbols_mode:
            symbols += self.SPECIAL_SYMBOLS
        
        return "".join(random.choice(symbols) for i in range(self.psw_length))


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self._ui = Ui_MainWindow()
        self._generator = PasswordGenerator()
        self._root_path = os.path.dirname(os.path.abspath(__file__))
        self._buffer = QClipboard()
        self._initUI()
        self._initCallBack()
    
    def _initUI(self) -> None:
        self.setMinimumSize(960, 640)
        self._ui.setupUi(self)

        # Set icons and pixmaps
        pixmap = QPixmap(os.path.join(self._root_path, "icons", "icon.png"))
        self.setWindowIcon(QIcon(pixmap))
        self._ui.app_icon_lbl.setPixmap(pixmap)
        self._ui.history_list.setIconSize(pixmap.size())
        
        # Set generator info
        self._ui.psw_length_info_lbl.setText(f"## {self._generator.psw_length}")
        self._ui.psw_length_slider.setMinimum(self._generator.MIN_LENGTH)
        self._ui.psw_length_slider.setMaximum(self._generator.MAX_LENGTH)
        self._ui.psw_length_slider.setValue(self._generator.psw_length)
        self._ui.lowercase_mode_btn.setChecked(self._generator.lowercase_mode)
        self._ui.uppercse_mode_btn.setChecked(self._generator.uppercase_mode)
        self._ui.special_symbols_mode_btn.setChecked(self._generator.special_symbols_mode)
        self._ui.result_frame.hide()

        # Set button icons
        self._ui.generate_psw_btn.setIcon(QIcon(os.path.join(self._root_path, "icons", "icon.png")))
        self._ui.copy_psw_btn.setIcon(QIcon(os.path.join(self._root_path, "icons", "copy.png")))
        self._ui.clear_history_btn.setIcon(QIcon(os.path.join(self._root_path, "icons", "clear.png")))
        self._ui.copy_history_psw_btn.setIcon(QIcon(os.path.join(self._root_path, "icons", "copy.png")))

        # Load stylesheet at QSS format
        stylesheet_path = os.path.join(self._root_path, "ui", "styles.qss")
        if not os.path.exists(stylesheet_path):
            return

        with open(stylesheet_path, "r") as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read())

    def _initCallBack(self):
        self._ui.psw_length_slider.valueChanged.connect(self._on_psw_length_slider_changed)
        self._ui.lowercase_mode_btn.stateChanged.connect(self._on_lowercase_mode_changed)
        self._ui.uppercse_mode_btn.stateChanged.connect(self._on_uppercase_mode_changed)
        self._ui.special_symbols_mode_btn.stateChanged.connect(self._on_special_symbols_mode_changed)
        self._ui.generate_psw_btn.clicked.connect(self._on_generate_psw_btn_clicked)
        self._ui.copy_psw_btn.clicked.connect(self._on_copy_psw_btn_clicked)
        self._ui.copy_history_psw_btn.clicked.connect(self._on_copy_history_psw_btn_clicked)
        self._ui.clear_history_btn.clicked.connect(self._on_clear_history_btn_clicked)

    def _on_psw_length_slider_changed(self, value: int) -> None:
        self._generator.psw_length = value
        self._ui.psw_length_info_lbl.setText(f"## {self._generator.psw_length}")

    def _on_lowercase_mode_changed(self, value: int) -> None:
        self._generator.lowercase_mode = bool(value)

    def _on_uppercase_mode_changed(self, value: int) -> None:
        self._generator.uppercase_mode = bool(value)

    def _on_special_symbols_mode_changed(self, value: int) -> None:
        self._generator.special_symbols_mode = bool(value)

    def _on_generate_psw_btn_clicked(self) -> None:
        if self._ui.result_frame.isHidden():
            self._ui.result_frame.show()
        
        self._ui.psw_le.setText(self._generator.generate_password())
        item = QListWidgetItem(
            QIcon(os.path.join(self._root_path, "icons", "icon.png")),
            f"Пароль: {self._ui.psw_le.text()}\nДлинна: {self._generator.psw_length}"
        )
        setattr(item, "password", self._ui.psw_le.text())
        self._ui.history_list.insertItem(0, item)
        self._ui.copy_history_psw_btn.setText("Копировать")
        self._ui.copy_psw_btn.setText("Копировать")

    def _on_copy_psw_btn_clicked(self) -> None:
        self._buffer.clear()
        self._buffer.setText(self._ui.psw_le.text())
        self._ui.copy_history_psw_btn.setText("Копировать")
        self._ui.copy_psw_btn.setText("Скопировано")

    def _on_copy_history_psw_btn_clicked(self) -> None:
        if self._ui.history_list.count() == 0:
            return
        
        items = self._ui.history_list.selectedItems()
        print(items)
        if len(items) == 0:
            return

        item = items[0]
        self._buffer.clear()
        self._buffer.setText(item.text())
        self._ui.copy_history_psw_btn.setText("Скопировано")
        self._ui.copy_psw_btn.setText("Копировать")

    def _on_clear_history_btn_clicked(self) -> None:
        self._ui.history_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
