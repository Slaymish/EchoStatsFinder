from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRunnable, pyqtSignal, pyqtSlot, QThreadPool, QObject
from PyQt5.QtWidgets import QMessageBox, QComboBox  
import sys
from vrmlplayersearcher import *
from pubstats import *
import threading


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(575, 300)

  

 

        # Centre line
        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(270, 99, 21, 360))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Bottom line
        self.line_2 = QtWidgets.QFrame(Widget)
        self.line_2.setGeometry(QtCore.QRect(0, 450, 575, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        # VRML PLayer Searcher Label
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(20, 460, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # Username label
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(20, 500, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # Username input
        self.usernameInput = QtWidgets.QTextEdit(Widget)
        self.usernameInput.setGeometry(QtCore.QRect(20, 520, 140, 31))
        self.usernameInput.setObjectName("usernameInput")

        # Search player button
        self.searchButton = QtWidgets.QPushButton(Widget)
        self.searchButton.setGeometry(QtCore.QRect(210, 515, 135, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.searchButton.setFont(font)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchForVRMLPlayer)


        # Team name label
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(400, 500, 80, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Team name output
        self.teamNameLabel = QtWidgets.QLabel(Widget)
        self.teamNameLabel.setGeometry(QtCore.QRect(484, 500, 71, 16))
        font = QtGui.QFont()
        self.teamNameLabel.setFont(font)
        self.teamNameLabel.setObjectName("teamNameLabel")

        # Worldwide rank label
        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(400, 520, 108, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # Worldwide rank output
        self.rankingLabel = QtWidgets.QLabel(Widget)
        self.rankingLabel.setGeometry(QtCore.QRect(520, 520, 71, 16))
        font = QtGui.QFont()
        self.rankingLabel.setFont(font)
        self.rankingLabel.setObjectName("rankingLabel")

        # Division label
        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(400, 540, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        # Division output
        self.divisionLabel = QtWidgets.QLabel(Widget)
        self.divisionLabel.setGeometry(QtCore.QRect(465, 540, 71, 16))
        font = QtGui.QFont()
        self.divisionLabel.setFont(font)
        self.divisionLabel.setObjectName("divisionLabel")

        # Progress bar (Playersearcher)
        self.progressBar = QtWidgets.QProgressBar(Widget)
        self.progressBar.setGeometry(QtCore.QRect(243, 560, 101, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        ### Player lines
        self.line_4 = QtWidgets.QFrame(Widget)
        self.line_4.setGeometry(QtCore.QRect(0, 185, 575, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QFrame(Widget)
        self.line_5.setGeometry(QtCore.QRect(0, 280, 575, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QFrame(Widget)
        self.line_6.setGeometry(QtCore.QRect(0, 370, 575, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")


        ### Username labels

        # Player 1
        self.lplayer1 = QtWidgets.QLabel(Widget)
        self.lplayer1.setGeometry(QtCore.QRect(20, 150, 71, 16))
        font = QtGui.QFont()
        self.lplayer1.setFont(font)
        self.lplayer1.setObjectName("lplayer1")

        # Player 2
        self.lplayer2 = QtWidgets.QLabel(Widget)
        self.lplayer2.setGeometry(QtCore.QRect(290, 150, 71, 16))
        font = QtGui.QFont()
        self.lplayer2.setFont(font)
        self.lplayer2.setObjectName("lplayer2")

        # Player 3
        self.lplayer3 = QtWidgets.QLabel(Widget)
        self.lplayer3.setGeometry(QtCore.QRect(20, 220, 71, 16))
        font = QtGui.QFont()
        self.lplayer3.setFont(font)
        self.lplayer3.setObjectName("lplayer3")

        # Player 4
        self.lplayer4 = QtWidgets.QLabel(Widget)
        self.lplayer4.setGeometry(QtCore.QRect(290, 220, 71, 16))
        font = QtGui.QFont()
        self.lplayer4.setFont(font)
        self.lplayer4.setObjectName("lplayer4")

        # Player 5
        self.lplayer5 = QtWidgets.QLabel(Widget)
        self.lplayer5.setGeometry(QtCore.QRect(20, 330, 71, 16))
        font = QtGui.QFont()
        self.lplayer5.setFont(font)
        self.lplayer5.setObjectName("lplayer5")

        # Player 6
        self.lplayer6 = QtWidgets.QLabel(Widget)
        self.lplayer6.setGeometry(QtCore.QRect(290, 330, 71, 16))
        font = QtGui.QFont()
        self.lplayer6.setFont(font)
        self.lplayer6.setObjectName("lplayer6")

        # Player 7
        self.lplayer7 = QtWidgets.QLabel(Widget)
        self.lplayer7.setGeometry(QtCore.QRect(20, 410, 71, 16))
        font = QtGui.QFont()
        self.lplayer7.setFont(font)
        self.lplayer7.setObjectName("lplayer7")

        # Player 8
        self.lplayer8 = QtWidgets.QLabel(Widget)
        self.lplayer8.setGeometry(QtCore.QRect(290, 410, 71, 16))
        font = QtGui.QFont()
        self.lplayer8.setFont(font)
        self.lplayer8.setObjectName("lplayer8")
        

        ### Unlabelled UI Elements, not completed yet!
        self.pubStatsTitle = QtWidgets.QLabel(Widget)
        self.pubStatsTitle.setGeometry(QtCore.QRect(10, 0, 201, 41))

        font = QtGui.QFont()
        font.setPointSize(20)
        self.pubStatsTitle.setFont(font)
        self.pubStatsTitle.setObjectName("pubStatsTitle")


        self.ipLabel = QtWidgets.QLabel(Widget)
        self.ipLabel.setGeometry(QtCore.QRect(10, 40, 81, 16))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")


        self.ipInput = QtWidgets.QTextEdit(Widget)
        self.ipInput.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.ipInput.setObjectName("IP Input 2")

        self.exceptText = QtWidgets.QLabel(Widget)
        self.exceptText.setGeometry(QtCore.QRect(10, 58, 101, 16))
        self.exceptText.setObjectName("exceptText")


        # Pub search button
        self.searchButton_2 = QtWidgets.QPushButton(Widget)

        self.searchButton_2.setGeometry(QtCore.QRect(10, 120, 101, 21))
        self.searchButton_2.setFlat(False)
        self.searchButton_2.setObjectName("searchButton_2")
        self.searchButton_2.clicked.connect(self.searchForPubPlayer)

        self.portLabel = QtWidgets.QLabel(Widget)
        self.portLabel.setGeometry(QtCore.QRect(140, 40, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portLabel.setFont(font)
        self.portLabel.setObjectName("portLabel")

        self.portInput = QtWidgets.QTextEdit(Widget)
        self.portInput.setGeometry(QtCore.QRect(140, 80, 101, 31))
        self.portInput.setObjectName("Port Input")

        self.exceptText2 = QtWidgets.QLabel(Widget)
        self.exceptText2.setGeometry(QtCore.QRect(140, 58, 101, 16))
        self.exceptText2.setObjectName("exceptText2")

        self.pubPlayers = QComboBox(Widget)
        self.pubPlayers.setGeometry(QtCore.QRect(10,150, 100, 20))
        self.pubPlayers.setObjectName("pubPlayers")
        self.pubPlayers.currentTextChanged.connect(self.updatePubStatViewer)


        self.pubTeamLabel = QtWidgets.QLabel(Widget)
        self.pubTeamLabel.setGeometry(QtCore.QRect(10, 180, 71, 16))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pubTeamLabel.setFont(font)
        self.pubTeamLabel.setObjectName("pubTeamLabel")

        self.pubTeamName = QtWidgets.QLabel(Widget)
        self.pubTeamName.setGeometry(QtCore.QRect(85, 180, 71, 16))
        font = QtGui.QFont()
        self.pubTeamName.setFont(font)
        self.pubTeamName.setObjectName("pubTeamName")

        self.pubRanking = QtWidgets.QLabel(Widget)
        self.pubRanking.setGeometry(QtCore.QRect(110, 210, 101, 16))
        font = QtGui.QFont()
        self.pubRanking.setFont(font)
        self.pubRanking.setObjectName("pubRanking")

        self.pubrankingLabel = QtWidgets.QLabel(Widget)
        self.pubrankingLabel.setGeometry(QtCore.QRect(10, 210, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.pubrankingLabel.setFont(font)
        self.pubrankingLabel.setObjectName("pubrankingLabel")

        self.pubDivision = QtWidgets.QLabel(Widget)
        self.pubDivision.setGeometry(QtCore.QRect(10, 240, 51, 16))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pubDivision.setFont(font)
        self.pubDivision.setObjectName("pubDivision")
        
        self.pubdivisionLabel = QtWidgets.QLabel(Widget)
        self.pubdivisionLabel.setGeometry(QtCore.QRect(60, 240, 71, 16))
        font = QtGui.QFont()
        self.pubdivisionLabel.setFont(font)
        self.pubdivisionLabel.setObjectName("pubdivisionLabel")

        ## pub progress bar
        self.progressBar2 = QtWidgets.QProgressBar(Widget)
        self.progressBar2.setGeometry(QtCore.QRect(10, 265, 101, 23))
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setObjectName("progressBar2")




        self.foundTeamName = "..."
        self.foundRanking = "..."
        self.foundDivision = "..."

        self.pubfoundTeamName = "..."
        self.pubfoundRanking = "..."
        self.pubfoundDivision = "..."


        self.player1 = ""
        self.player2 = ""
        self.player3 = ""
        self.player4 = ""
        self.player5 = ""
        self.player6 = ""
        self.player7 = ""
        self.player8 = ""

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Pub and Player Searcher"))
        self.label.setText(_translate("Widget", "VRML Player Searcher"))
        self.label_2.setText(_translate("Widget", "Username"))
        self.searchButton.setText(_translate("Widget", "Search for Player"))
        self.label_3.setText(_translate("Widget", "Team Name: "))
        self.teamNameLabel.setText(_translate("Widget", f"{self.foundTeamName}"))
        self.rankingLabel.setText(_translate("Widget", f"{self.foundRanking}"))
        self.divisionLabel.setText(_translate("Widget", f"{self.foundDivision}"))
        self.label_4.setText(_translate("Widget", "Worldwide Rank:"))
        self.label_5.setText(_translate("Widget", "Division:"))
        self.pubStatsTitle.setText(_translate("Widget", "Player Pub Stats"))
        self.ipLabel.setText(_translate("Widget", "IP Address"))
        self.exceptText.setText(_translate("Widget", "(leave blank if on PC)"))
        self.portLabel.setText(_translate("Widget", "Port Number"))
        self.exceptText2.setText(_translate("Widget", "(leave blank if on PC)"))
        self.searchButton_2.setText(_translate("Widget", "Begin Search"))


        self.pubTeamLabel.setText(_translate("Widget", "Team Name: "))
        self.pubTeamName.setText(_translate("Widget", f"{self.pubfoundTeamName}"))
        self.pubRanking.setText(_translate("Widget", f"{self.pubfoundRanking}"))
        self.pubdivisionLabel.setText(_translate("Widget", f"{self.pubfoundDivision}"))
        self.pubrankingLabel.setText(_translate("Widget", "Worldwide Rank:"))
        self.pubDivision.setText(_translate("Widget", "Division:"))

    
    def searchForVRMLPlayer(self):
        self.playerName = self.usernameInput.toPlainText()
        if self.playerName == None or self.playerName == "": ##Filter missing names
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Please enter a player name")
            msgBox.setWindowTitle("No Player Entered")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            main = VRMLMain('https://api.vrmasterleague.com/', str(self.playerName))
            results = main.completeSearchWithGUI(self.progressBar)
            self.foundTeamName = results[0]
            self.foundRanking = str(results[1])
            self.foundDivision = str(results[2])

            self.retranslateUi(Widget)


    def searchForPubPlayer(self):
        #Get IP and Port
        self.ip = self.ipInput.toPlainText()
        self.port = self.portInput.toPlainText()


        #Check and fix ports
        if len(self.ip.split(".")) != 4: ##Invalid or missing IP Address
            self.ip = "127.0.0.1"
        if (self.port == None) or (self.port == ""):
            self.port = "6721"
        
        #Execute pub player finder scripts
        #Multithreading to prevent freezing GUI
        self.threadpool = QThreadPool()
        self.pubBackground()
        self.populatePubPlayers()
    
    def populatePubPlayers(self):
        for name in self.names:
            self.pubPlayers.addItem(name)
        self.multithreadWorker = multithreadVRMLSearch(self.names)
        self.multithreadWorker.signals.newValue.connect(self.updatePBarValue)
        self.threadpool.start(self.multithreadWorker)
        
    def pubBackground(self):
        nameFinder = PubMain(self.ip, self.port)
        self.names = nameFinder.findNames()
    
    def updatePubStatViewer(self, value):
        try:
            nameIndex = self.multithreadWorker.names.index(value)
            try:
                foundStats = self.multithreadWorker.stats[nameIndex]
                #foundStats[0] is team name
                #foundStats[1] is global ranking
                #foundStats[2] is tier

                self.pubfoundTeamName = foundStats[0]
                self.pubfoundRanking = foundStats[1]
                self.pubfoundDivision = foundStats[2]
                self.retranslateUi(Widget)
            except Exception as e:
                print("No stats available")
        except:
            pass
    
    def updatePBarValue(self, value):
        self.progressBar2.setProperty("value", value)

class multithreadComms(QObject):
    newValue = pyqtSignal(int)

class multithreadVRMLSearch(QRunnable):
    def __init__(self, names):
        super(multithreadVRMLSearch, self).__init__()
        self.names = names
        self.stats = []
        self.signals = multithreadComms()

    @pyqtSlot()
    def run(self):
        vrmlInfo = VRMLMain("https://api.vrmasterleague.com/", "Placeholder")
        individualStat = [] ##Temporary stat storage

        progressBarTotal = 0
        self.signals.newValue.emit(0)

        # Gets number of segments for progress bar
        progressBarSegment = 100/len(self.names)

        for name in self.names:
            progressBarTotal += int(progressBarSegment)
            self.signals.newValue.emit(progressBarTotal)
            individualStat = []
            vrmlInfo.username = name
            res = vrmlInfo.completeSearch()
            for stat in res: ## Convert stats from dictionary to array
                individualStat.append(stat)
            self.stats.append(individualStat)
        self.signals.newValue.emit(100)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()

    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
