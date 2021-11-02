from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from vrmlplayersearcher import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(575, 600)
        
        # Top line
        self.line_3 = QtWidgets.QFrame(Widget)
        self.line_3.setGeometry(QtCore.QRect(0, 90, 575, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")


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
        

        ### For Pubs stats, not completed yet!

        # Player pub stats label
        self.label_6 = QtWidgets.QLabel(Widget)
        self.label_6.setGeometry(QtCore.QRect(20, 0, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        # IP address label
        self.label_7 = QtWidgets.QLabel(Widget)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        # IP input
        self.IpInput = QtWidgets.QTextEdit(Widget)
        self.IpInput.setGeometry(QtCore.QRect(20, 60, 140, 31))
        self.IpInput.setObjectName("IpInput")

        # 'Leave blank for pc' label
        self.label_8 = QtWidgets.QLabel(Widget)
        self.label_8.setGeometry(QtCore.QRect(110, 40, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        # Pub search button
        self.searchButton_2 = QtWidgets.QPushButton(Widget)
        self.searchButton_2.setGeometry(QtCore.QRect(370, 40, 115, 45))
        self.searchButton_2.setFlat(False)
        self.searchButton_2.setObjectName("searchButton_2")
        self.searchButton_2.clicked.connect(self.searchPub)

        """
        # 'Current not' label
        self.label_9 = QtWidgets.QLabel(Widget)
        self.label_9.setGeometry(QtCore.QRect(220, 30, 115, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        # 'Finished yet' label
        self.label_10 = QtWidgets.QLabel(Widget)
        self.label_10.setGeometry(QtCore.QRect(220, 45, 110, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        # '(Output in CLI)' label
        self.label_11 = QtWidgets.QLabel(Widget)
        self.label_11.setGeometry(QtCore.QRect(220, 60, 110, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        """
        self.foundTeamName = ""
        self.foundRanking = ""
        self.foundDivision = ""

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
        self.label_6.setText(_translate("Widget", "Player Pub Stats"))
        self.label_7.setText(_translate("Widget", "IP Address"))
        self.label_8.setText(_translate("Widget", "(leave blank if on PC)"))
        self.searchButton_2.setText(_translate("Widget", "Begin Search"))

        self.lplayer1.setText(_translate("Widget", f"{self.player1}"))
        self.lplayer2.setText(_translate("Widget", f"{self.player2}"))
        self.lplayer3.setText(_translate("Widget", f"{self.player3}"))
        self.lplayer4.setText(_translate("Widget", f"{self.player4}"))
        self.lplayer5.setText(_translate("Widget", f"{self.player5}"))
        self.lplayer6.setText(_translate("Widget", f"{self.player6}"))
        self.lplayer7.setText(_translate("Widget", f"{self.player7}"))
        self.lplayer8.setText(_translate("Widget", f"{self.player8}"))


        """
        self.label_9.setText(_translate("Widget", "CURRENTLY NOT"))
        self.label_10.setText(_translate("Widget", "FINISHED YET"))
        self.label_11.setText(_translate("Widget", "(Outputs in CLI)"))
        """
    
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

        self.displayNames()

        for i in range(0, len(self.playerList)):
            main = Main('https://api.vrmasterleague.com/', str(self.playerList[i]))
            results = main.completeSearch()
            print(self.playerList[i] + ': ' + str(results)) # Display in CLI




    def getNames(self):
        self.playerList = []
        stop = False
        try:
            #url_request = requests.get('http://' + ip + ':' + port + '/session', timeout=5)
            echo_url = 'http://' + self.userIP + ':6721/session'
            url_request = requests.get(echo_url, timeout=4)

        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Could not connect to session")
            msgBox.setWindowTitle("Ensure Echo is open and the IP is correct")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
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

    def displayNames(self):

        if len(self.playerList) > 0:
            self.player1 = self.playerList[0]
            if len(self.playerList) > 1:
                self.player2 = self.playerList[1]
                if len(self.playerList) > 2:
                    self.player3 = self.playerList[2]
                    if len(self.playerList) > 3:
                        self.player4 = self.playerList[3]
                        if len(self.playerList) > 4:
                            self.player5 = self.playerList[4]
                            if len(self.playerList) > 5:
                                self.player6 = self.playerList[5]
                                if len(self.playerList) > 6:
                                    self.player7 = self.playerList[6]
                                    if len(self.playerList) > 1:
                                        self.player8 = self.playerList[7]
        
        self.retranslateUi(Widget)







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
