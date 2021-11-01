from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from vrmlplayersearcher import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(575, 158)

        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(270, 0, 21, 391))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(300, 0, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(300, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.usernameInput = QtWidgets.QTextEdit(Widget)
        self.usernameInput.setGeometry(QtCore.QRect(300, 60, 101, 31))
        self.usernameInput.setObjectName("usernameInput")

        self.searchButton = QtWidgets.QPushButton(Widget)
        self.searchButton.setGeometry(QtCore.QRect(300, 100, 101, 21))
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchForVRMLPlayer)

        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(410, 40, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.teamNameLabel = QtWidgets.QLabel(Widget)
        self.teamNameLabel.setGeometry(QtCore.QRect(485, 40, 71, 16))
        font = QtGui.QFont()
        self.teamNameLabel.setFont(font)
        self.teamNameLabel.setObjectName("teamNameLabel")

        self.label_4 = QtWidgets.QLabel(Widget)
        self.label_4.setGeometry(QtCore.QRect(410, 70, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.rankingLabel = QtWidgets.QLabel(Widget)
        self.rankingLabel.setGeometry(QtCore.QRect(506, 70, 71, 16))
        font = QtGui.QFont()
        self.rankingLabel.setFont(font)
        self.rankingLabel.setObjectName("rankingLabel")

        self.label_5 = QtWidgets.QLabel(Widget)
        self.label_5.setGeometry(QtCore.QRect(410, 100, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.divisionLabel = QtWidgets.QLabel(Widget)
        self.divisionLabel.setGeometry(QtCore.QRect(460, 100, 71, 16))
        font = QtGui.QFont()
        self.divisionLabel.setFont(font)
        self.divisionLabel.setObjectName("divisionLabel")

        self.progressBar = QtWidgets.QProgressBar(Widget)
        self.progressBar.setGeometry(QtCore.QRect(300, 130, 101, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")


        ### Unlabelled UI Elements, not completed yet!
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Widget)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        # IP input
        self.IpInput = QtWidgets.QTextEdit(Widget)
        self.IpInput.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.IpInput.setObjectName("IpInput")

        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setGeometry(QtCore.QRect(90, 40, 101, 16))
        self.label_8.setObjectName("label_8")

        self.searchButton_2 = QtWidgets.QPushButton(Widget)
        self.searchButton_2.setGeometry(QtCore.QRect(10, 100, 101, 21))
        self.searchButton_2.setFlat(False)
        self.searchButton_2.setObjectName("searchButton_2")
        self.searchButton_2.clicked.connect(self.searchPub)


        self.label_9 = QtWidgets.QLabel(Widget)
        self.label_9.setGeometry(QtCore.QRect(160, 70, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Widget)
        self.label_10.setGeometry(QtCore.QRect(170, 80, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.foundTeamName = ""
        self.foundRanking = ""
        self.foundDivision = ""

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "VRML Player Searcher"))
        self.label_2.setText(_translate("Widget", "Username"))
        self.searchButton.setText(_translate("Widget", "Search for Player"))
        self.label_3.setText(_translate("Widget", "Team Name: "))
        self.teamNameLabel.setText(_translate("Widget", f"{self.foundTeamName}"))
        self.rankingLabel.setText(_translate("Widget", f"{self.foundRanking}"))
        self.divisionLabel.setText(_translate("Widget", f"{self.foundDivision}"))
        self.label_4.setText(_translate("Widget", "Worldwide Rank:"))
        self.label_5.setText(_translate("Widget", "Division:"))
        self.label_6.setText(_translate("Widget", "Player Pub Stats"))
        self.label_7.setText(_translate("Widget", "IP Address"))
        self.label_8.setText(_translate("Widget", "(leave blank if on PC)"))
        self.searchButton_2.setText(_translate("Widget", "Begin Search"))
        self.label_9.setText(_translate("Widget", "CURRENTLY NOT"))
        self.label_10.setText(_translate("Widget", "FINISHED YET."))
    
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
            main = Main('https://api.vrmasterleague.com/', str(self.playerName))
            results = main.completeSearchWithGUI(self.progressBar)
            print(results)
            self.foundTeamName = results[0]
            self.foundRanking = str(results[1])
            self.foundDivision = str(results[2])

            self.retranslateUi(Widget)

    def searchPub(self):
        #print("Search pub clicked")

        # If nothing entered
        if self.IpInput.toPlainText() == None or self.IpInput.toPlainText() == '':
            # Set ip to pc 
            self.userIP = '127.0.0.1'
        else:
            # otherwise use quest
            self.userIP = self.IpInput.toPlainText()

        # Get list of players names from echo session
        self.getNames()

        # To test without echo open (comment out when using properly)
        #self.playerList = ['Slaymish','Rosh-','Silveridge','00JayWalker00']

        for i in range(0, len(self.playerList)):
            main = Main('https://api.vrmasterleague.com/', str(self.playerList[i]))
            results = main.completeSearch()
            print(self.playerList[i] + ': ' + str(results)) # Display in CLI




    def getNames(self):
        self.playerList = []
        print("IP used: " + self.userIP)

        try:
            #url_request = requests.get('http://' + ip + ':' + port + '/session', timeout=5)
            echo_url = 'http://' + self.userIP + ':6721/session'
            url_request = requests.get(echo_url, timeout=5)

        except:
            print("Could not connect to session - Ensure echo is open")
            stop = True
    
        if not stop:
            print('')
            if url_request.status_code:
                data = url_request.text # String
                echo_data = json.loads(data) # Dict

                #teams[].players    # An array of objects containing data used to instantiate the team's players.
                    

                teams_data = echo_data['teams']

                for i in range(0,len(teams_data)-1):
                    per_team = teams_data[i]
                    per_team_players = per_team['players']

                    for j in range(0,len(per_team_players)):
                        temp_player = per_team_players[j]
                        self.playerList.append(temp_player['name']) # Add name to list
                
            else:
                print("Error connecting to echo api (" + url_request.status_code + "). Ensure the ip is correct")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
