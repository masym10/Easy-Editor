from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, 
    QPushButton,QVBoxLayout, QHBoxLayout,
    QListWidget,QFileDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter

app = QApplication([])

#app window
main_window = QWidget()
main_window.setStyleSheet("background-color: #D500FF; color: #000")
main_window.show()
main_window.setWindowTitle("Easy Editor")
main_window.resize(700,500)

#list_widget
list_images_label = QLabel('Images')
list_images = QListWidget()
list_images.setStyleSheet("background: #FFDC00; color #000")

#app_button_push
btn_R_Image = QPushButton("Right")
btn_R_Image.setStyleSheet("background-color: #fff; color: #000")
btn_L_Image = QPushButton("Left")
btn_L_Image.setStyleSheet("background-color: #fff; color: #000")
btn_reflection = QPushButton("Reflection")
btn_reflection.setStyleSheet("background-color: #fff; color: #000")
btn_focus = QPushButton("Focus")
btn_focus.setStyleSheet("background-color: #fff; color: #000")
btn_BW = QPushButton("B/W")
btn_BW.setStyleSheet("background-color: #fff; color: #000")
btn_folder = QPushButton("Folder")
btn_folder.setStyleSheet("background-color: #fff; color: #000")
btn_lf = QPushButton("Lightfocus")
btn_lf.setStyleSheet("background-color: #fff; color: #000")
btn_br = QPushButton("Bluar")
btn_br.setStyleSheet("background-color: #fff; color: #000")
btn_cr = QPushButton("Countour")
btn_cr.setStyleSheet("background-color: #fff; color: #000")
btn_fd = QPushButton("Detail")
btn_fd.setStyleSheet("background-color: #fff; color: #000")
btn_ee = QPushButton("EdgeEnhance")
btn_ee.setStyleSheet("background-color: #fff; color: #000")
btn_eem = QPushButton("EdgeEnhanceMore")
btn_eem.setStyleSheet("background-color: #fff; color: #000")
btn_eb = QPushButton("Emboss")
btn_eb.setStyleSheet("background-color: #fff; color: #000")
btn_fe = QPushButton("FindEdges")
btn_fe.setStyleSheet("background-color: #fff; color: #000")
btn_sh = QPushButton("Sharpen")
btn_sh.setStyleSheet("background-color: #fff; color: #000")

#Layout
layout_main = QHBoxLayout()
tool_box = QHBoxLayout()
tool_box1 = QHBoxLayout()
tool_box2 = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

#col_1 connect
col_1.addWidget(btn_folder)
col_1.addWidget(list_images)

#tool_box connect
tool_box.addWidget(btn_L_Image)
tool_box.addWidget(btn_R_Image)
tool_box.addWidget(btn_reflection)
tool_box.addWidget(btn_focus)
tool_box.addWidget(btn_BW)
tool_box1.addWidget(btn_lf)
tool_box1.addWidget(btn_br)
tool_box1.addWidget(btn_cr)
tool_box1.addWidget(btn_fd)
tool_box1.addWidget(btn_ee)
tool_box2.addWidget(btn_eem)
tool_box2.addWidget(btn_eb)
tool_box2.addWidget(btn_fe)
tool_box2.addWidget(btn_sh)

#col_2 connect
col_2.addWidget(list_images_label)
col_2.addLayout(tool_box)
col_2.addLayout(tool_box1)
col_2.addLayout(tool_box2)

#main_window
layout_main.addLayout(col_1)
layout_main.addLayout(col_2)
main_window.setLayout(layout_main)

#Label
Label_main = QLabel()

workdir = ''

#def's
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files):
    extensions = ['.png', '.jpg', '.jpeg', '.gif']
    result = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    
    return result

def showFilenameList():
    chooseWorkdir()
    files = filter(os.listdir(workdir))
    list_images.clear()
    for file in files:
        list_images.addItem(file)

#class
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.original = None
        self.save_dir = "modefied/"

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)

        if os.path.exists(path) or os.path.isdir(path):
            fullpath = os.path.join(path, self.filename)
            self.image.save(fullpath)
        else:
            os.mkdir(path)
        

    def load_image(self, filename):
        self.filename = filename
        fullpath = os.path.join(workdir, filename)
        self.image = Image.open(fullpath)

    def showImage(self, path):
        list_images_label.hide()
        pixmapimage = QPixmap(path)
        w,h = list_images_label.width(), list_images_label.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)    
        list_images_label.setPixmap(pixmapimage)
        list_images_label.show()

    def left_image(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def right_image(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def bluar(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def countour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)
        
    def detail(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)
    
    def edge_enhance(self):        
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def edge_enhance_more(self):        
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def emboss(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def find_edges(self):
        self.image = self.image.filter(ImageFilter.FIND_EDGES)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def smooth(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def smooth_more(self):
        self.image = self.image.filter(ImageFilter.SMOOTH_MORE)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

    def reflection(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        fullpath = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(fullpath)

workimage = ImageProcessor()

def showChosenImage():
    if list_images.currentRow() >= 0:
        filename = list_images.currentItem().text()
        workimage.load_image(filename)
        workimage.showImage(os.path.join(workdir, workimage.filename))

#btn_connect
btn_folder.clicked.connect(showFilenameList)
btn_BW.clicked.connect(workimage.do_bw)
btn_focus.clicked.connect(workimage.smooth_more)
btn_lf.clicked.connect(workimage.smooth)
btn_L_Image.clicked.connect(workimage.left_image)
btn_R_Image.clicked.connect(workimage.right_image)
btn_reflection.clicked.connect(workimage.reflection)
btn_br.clicked.connect(workimage.bluar)
btn_cr.clicked.connect(workimage.countour)
btn_eb.clicked.connect(workimage.emboss)
btn_ee.clicked.connect(workimage.edge_enhance)
btn_eem.clicked.connect(workimage.edge_enhance_more)
btn_fd.clicked.connect(workimage.detail)
btn_fe.clicked.connect(workimage.find_edges)
btn_sh.clicked.connect(workimage.sharpen)
list_images.currentRowChanged.connect(showChosenImage)



app.exec_()