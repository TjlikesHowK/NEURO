from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from pygame import mixer
import youtubeMusic as ym
import playerU5
import os

class Player(QWidget, playerU5.Ui_MainWindow):
	def __init__(self):
		super(Player, self).__init__()
		self.setupUi(self)

		self.setFixedSize(self.size())

		self.prevPushButton.clicked.connect(self.prev_music)
		self.playPushButton.clicked.connect(self.play_music)
		self.nextPushButton.clicked.connect(self.next_music)
		self.addPushButton.clicked.connect(self.add_music)

		self.musicListWidget.doubleClicked.connect(self.play_music)

		self.dir = ""
		self.music_mixer = mixer
		self.music_mixer.init()

	def prev_music(self):
		pass

	def play_music(self):
		item = self.musicListWidget.currentItem()

		if item:
			file = os.path.join(self.dir, item.text())
			
			self.music_mixer.music.load(file)

		else:
			self.musicListWidget.currentRow(0)

		self.music_mixer.music.play()

	def next_music(self):
		pass

	def add_music(self):
		self.musicListWidget.clear()

		dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")

		if dir:
			for file in os.listdir(dir):
				if file.endswith(".wav"):
					self.musicListWidget.addItem(os.path.join(file))

			self.dir = dir

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	player = Player()
	player.show()
	app.exec()