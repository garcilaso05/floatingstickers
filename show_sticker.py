import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

#Con esta primera versión simplemente coseguimos generar ventanas invisibles y sin bordes
#La imagen no es resizable, solo se puede mover arrastrando
#Como está orientado a Hyprland consideramos que la ventana se podrá cerrar con los atajos normales WIN+C
#También he creado un ejecutable para cerrarlos todos a la vez con: "pkill -f show_sticker.py"
#Para borrar los bordes de la ventana se ha usado la función setWindowFlags(Qt.FramelessWindowHint) 
#Pero además tenemos que crear una regla de ventanas en el hyprland.conf
#   windowrule = float, noborder on, ^(python3)$
#   windowrule = noborder, ^(python3)$
#   windowrule = noblur, ^(python3)$
#   windowrule = norounding, ^(python3)$
#   windowrule = opaque, ^(python3)$
#   windowrule = noshadow, ^(python3)$
#   windowrule = move random, ^(python3)$

class StickerWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        # Eliminar bordes de la ventana
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Hacer la ventana completamente transparente
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Cargar la imagen
        self.pixmap = QPixmap(image_path)
        self.label = QLabel(self)

        # Determinar el tamaño máximo en función de la orientación de la imagen
        if self.pixmap.width() > self.pixmap.height():
            max_size = 320
        else:
            max_size = 200

        # Redimensionar la imagen para que no exceda el tamaño máximo manteniendo la proporción
        self.pixmap = self.pixmap.scaled(max_size, max_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Establecer la imagen inicial
        self.set_image(self.pixmap)

        # Tamaño de la ventana según el tamaño de la imagen redimensionada
        self.setFixedSize(self.pixmap.width(), self.pixmap.height())

        # Posicionar la ventana en una ubicación concreta (ajusta las coordenadas si es necesario)
        self.move(500, 200)

    def set_image(self, pixmap):
        """Actualizar la imagen mostrada en el QLabel"""
        self.label.setPixmap(pixmap)
        self.label.setGeometry(0, 0, pixmap.width(), pixmap.height())

    def resizeEvent(self, event):
        """Ajustar la imagen cuando la ventana cambie de tamaño"""
        new_width = event.size().width()
        new_height = event.size().height()

        # Mantener la proporción de la imagen
        scaled_pixmap = self.pixmap.scaled(new_width, new_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # Establecer la nueva imagen redimensionada
        self.set_image(scaled_pixmap)

        # Llamar al evento original
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if len(sys.argv) < 2:
        print("Por favor, proporciona el path de la imagen.")
        sys.exit(1)

    image_path = sys.argv[1]
    window = StickerWindow(image_path)
    window.show()

    sys.exit(app.exec_())
