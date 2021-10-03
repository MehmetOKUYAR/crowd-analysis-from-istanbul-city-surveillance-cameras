from PyQt5.QtWidgets import QApplication
from live_camera_codes import istanbul_city_surveillance_cameras


app = QApplication([])
window = istanbul_city_surveillance_cameras()
window.show()
app.exec_()