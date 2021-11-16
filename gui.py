from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRunnable, pyqtSignal, pyqtSlot, QThreadPool, QObject
from PyQt5.QtWidgets import QMessageBox, QComboBox  
import sys
from functions.base.vrmlplayersearcher import *
from functions.base.pubstats import *
import threading
import re
import webbrowser
__version__ = "1.1.0"
__beta__ = False


class MainWindow(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(451, 603)
        
        #Multithreading to prevent freezing GUI
        self.threadpool = QThreadPool()

        self.line = QtWidgets.QFrame(Widget)
        self.line.setGeometry(QtCore.QRect(0, 120, 451, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.line_2 = QtWidgets.QFrame(Widget)
        self.line_2.setGeometry(QtCore.QRect(0, 200, 451, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Widget)
        self.line_3.setGeometry(QtCore.QRect(0, 280, 451, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Widget)
        self.line_4.setGeometry(QtCore.QRect(0, 360, 451, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Widget)
        self.line_5.setGeometry(QtCore.QRect(0, 440, 451, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        
        self.line_6 = QtWidgets.QFrame(Widget)
        self.line_6.setGeometry(QtCore.QRect(220, 130, 16, 321))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        
        self.PubTitle = QtWidgets.QLabel(Widget)
        self.PubTitle.setGeometry(QtCore.QRect(10, 0, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PubTitle.setFont(font)
        self.PubTitle.setObjectName("PubTitle")
        
        self.VRMLTitle = QtWidgets.QLabel(Widget)
        self.VRMLTitle.setGeometry(QtCore.QRect(10, 460, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.VRMLTitle.setFont(font)
        self.VRMLTitle.setObjectName("VRMLTitle")
        self.ipInput = QtWidgets.QPlainTextEdit(Widget)
        
        self.ipInput.setGeometry(QtCore.QRect(10, 90, 104, 31))
        self.ipInput.setObjectName("ipInput")
        
        self.portInput = QtWidgets.QPlainTextEdit(Widget)
        self.portInput.setGeometry(QtCore.QRect(120, 90, 104, 31))
        self.portInput.setObjectName("portInput")
        
        self.pubSearchButton = QtWidgets.QPushButton(Widget)
        self.pubSearchButton.setGeometry(QtCore.QRect(240, 90, 101, 31))
        self.pubSearchButton.setObjectName("pubSearchButton")
        self.pubSearchButton.clicked.connect(self.searchForPubPlayer)
        
        self.ipLabel = QtWidgets.QLabel(Widget)
        self.ipLabel.setGeometry(QtCore.QRect(10, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")
        
        self.portLabel = QtWidgets.QLabel(Widget)
        self.portLabel.setGeometry(QtCore.QRect(120, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portLabel.setFont(font)
        self.portLabel.setObjectName("portLabel")
        
        self.ipLabel_2 = QtWidgets.QLabel(Widget)
        self.ipLabel_2.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ipLabel_2.setFont(font)
        self.ipLabel_2.setObjectName("ipLabel_2")
        
        self.ipLabel_3 = QtWidgets.QLabel(Widget)
        self.ipLabel_3.setGeometry(QtCore.QRect(120, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ipLabel_3.setFont(font)
        self.ipLabel_3.setObjectName("ipLabel_3")
        
        self.playerTitle_1 = QtWidgets.QLabel(Widget)
        self.playerTitle_1.setGeometry(QtCore.QRect(10, 140, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_1.setFont(font)
        self.playerTitle_1.setObjectName("playerTitle_1")
        
        self.playerTitle_2 = QtWidgets.QLabel(Widget)
        self.playerTitle_2.setGeometry(QtCore.QRect(240, 140, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_2.setFont(font)
        self.playerTitle_2.setObjectName("playerTitle_2")
        
        self.playerTitle_3 = QtWidgets.QLabel(Widget)
        self.playerTitle_3.setGeometry(QtCore.QRect(10, 220, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_3.setFont(font)
        self.playerTitle_3.setObjectName("playerTitle_3")
        
        self.playerTitle_4 = QtWidgets.QLabel(Widget)
        self.playerTitle_4.setGeometry(QtCore.QRect(240, 220, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_4.setFont(font)
        self.playerTitle_4.setObjectName("playerTitle_4")
        
        self.playerTitle_5 = QtWidgets.QLabel(Widget)
        self.playerTitle_5.setGeometry(QtCore.QRect(10, 300, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_5.setFont(font)
        self.playerTitle_5.setObjectName("playerTitle_5")
        
        self.playerTitle_6 = QtWidgets.QLabel(Widget)
        self.playerTitle_6.setGeometry(QtCore.QRect(240, 300, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_6.setFont(font)
        self.playerTitle_6.setObjectName("playerTitle_6")
        
        self.playerTitle_7 = QtWidgets.QLabel(Widget)
        self.playerTitle_7.setGeometry(QtCore.QRect(10, 380, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_7.setFont(font)
        self.playerTitle_7.setObjectName("playerTitle_7")
        
        self.playerTitle_8 = QtWidgets.QLabel(Widget)
        self.playerTitle_8.setGeometry(QtCore.QRect(240, 380, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerTitle_8.setFont(font)
        self.playerTitle_8.setObjectName("playerTitle_8")
        
        self.teamlabel_1 = QtWidgets.QLabel(Widget)
        self.teamlabel_1.setGeometry(QtCore.QRect(100, 140, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_1.setFont(font)
        self.teamlabel_1.setObjectName("teamlabel_1")
        
        self.workRank_1 = QtWidgets.QLabel(Widget)
        self.workRank_1.setGeometry(QtCore.QRect(100, 160, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_1.setFont(font)
        self.workRank_1.setObjectName("workRank_1")
        
        self.tier_1 = QtWidgets.QLabel(Widget)
        self.tier_1.setGeometry(QtCore.QRect(100, 180, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tier_1.setFont(font)
        self.tier_1.setObjectName("tier_1")
        
        self.vrmlPlayerTitle = QtWidgets.QLabel(Widget)
        self.vrmlPlayerTitle.setGeometry(QtCore.QRect(10, 510, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vrmlPlayerTitle.setFont(font)
        self.vrmlPlayerTitle.setObjectName("vrmlPlayerTitle")
        
        self.PlayerNameInput = QtWidgets.QPlainTextEdit(Widget)
        self.PlayerNameInput.setGeometry(QtCore.QRect(10, 540, 104, 41))
        self.PlayerNameInput.setObjectName("PlayerNameInput")

        
        self.vrmlSearchButton = QtWidgets.QPushButton(Widget)
        self.vrmlSearchButton.setGeometry(QtCore.QRect(120, 540, 81, 41))
        self.vrmlSearchButton.setObjectName("vrmlSearchButton")
        self.vrmlSearchButton.clicked.connect(self.searchForVRMLPlayer)

        self.moreInfoVRML = QtWidgets.QPushButton(Widget)
        self.moreInfoVRML.setGeometry(QtCore.QRect(380, 570, 60, 25))
        self.moreInfoVRML.clicked.connect(self.loadMoreInfoVRML)

        
        self.vrmlRank = QtWidgets.QLabel(Widget)
        self.vrmlRank.setGeometry(QtCore.QRect(250, 540, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.vrmlRank.setFont(font)
        self.vrmlRank.setObjectName("vrmlRank")
        
        self.vrmlTeam = QtWidgets.QLabel(Widget)
        self.vrmlTeam.setGeometry(QtCore.QRect(250, 510, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.vrmlTeam.setFont(font)
        self.vrmlTeam.setObjectName("vrmlTeam")
        
        self.vrmlTier = QtWidgets.QLabel(Widget)
        self.vrmlTier.setGeometry(QtCore.QRect(250, 570, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.vrmlTier.setFont(font)
        self.vrmlTier.setObjectName("vrmlTier")
        
        self.teamL_1 = QtWidgets.QLabel(Widget)
        self.teamL_1.setGeometry(QtCore.QRect(140, 140, 81, 16))
        self.teamL_1.setObjectName("teamL_1")
        self.rank_1 = QtWidgets.QLabel(Widget)
        self.rank_1.setGeometry(QtCore.QRect(170, 160, 51, 16))
        self.rank_1.setObjectName("rank_1")
        self.tierL_1 = QtWidgets.QLabel(Widget)
        self.tierL_1.setGeometry(QtCore.QRect(130, 180, 91, 16))
        self.tierL_1.setObjectName("tierL_1")
        
        self.teamL_2 = QtWidgets.QLabel(Widget)
        self.teamL_2.setGeometry(QtCore.QRect(360, 140, 81, 16))
        self.teamL_2.setObjectName("teamL_2")
        
        self.teamlabel_2 = QtWidgets.QLabel(Widget)
        self.teamlabel_2.setGeometry(QtCore.QRect(320, 140, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_2.setFont(font)
        self.teamlabel_2.setObjectName("teamlabel_2")
        
        self.rank_2 = QtWidgets.QLabel(Widget)
        self.rank_2.setGeometry(QtCore.QRect(390, 160, 51, 16))
        self.rank_2.setObjectName("rank_2")
        self.tierL_2 = QtWidgets.QLabel(Widget)
        self.tierL_2.setGeometry(QtCore.QRect(350, 180, 91, 16))
        self.tierL_2.setObjectName("tierL_2")
        self.tier_2 = QtWidgets.QLabel(Widget)
        self.tier_2.setGeometry(QtCore.QRect(320, 180, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tier_2.setFont(font)
        self.tier_2.setObjectName("tier_2")
        
        self.workRank_2 = QtWidgets.QLabel(Widget)
        self.workRank_2.setGeometry(QtCore.QRect(320, 160, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_2.setFont(font)
        self.workRank_2.setObjectName("workRank_2")
        
        self.teamL_3 = QtWidgets.QLabel(Widget)
        self.teamL_3.setGeometry(QtCore.QRect(140, 220, 81, 16))
        self.teamL_3.setObjectName("teamL_3")
        
        self.teamlabel_3 = QtWidgets.QLabel(Widget)
        self.teamlabel_3.setGeometry(QtCore.QRect(100, 220, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_3.setFont(font)
        self.teamlabel_3.setObjectName("teamlabel_3")
        
        self.rank_3 = QtWidgets.QLabel(Widget)
        self.rank_3.setGeometry(QtCore.QRect(170, 240, 51, 16))
        self.rank_3.setObjectName("rank_3")
        
        self.tierL_3 = QtWidgets.QLabel(Widget)
        self.tierL_3.setGeometry(QtCore.QRect(130, 260, 91, 16))
        self.tierL_3.setObjectName("tierL_3")
        
        self.tier_3 = QtWidgets.QLabel(Widget)
        self.tier_3.setGeometry(QtCore.QRect(100, 260, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tier_3.setFont(font)
        self.tier_3.setObjectName("tier_3")
        
        self.workRank_3 = QtWidgets.QLabel(Widget)
        self.workRank_3.setGeometry(QtCore.QRect(100, 240, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_3.setFont(font)
        self.workRank_3.setObjectName("workRank_3")
        
        self.teamL_4 = QtWidgets.QLabel(Widget)
        self.teamL_4.setGeometry(QtCore.QRect(360, 220, 81, 16))
        self.teamL_4.setObjectName("teamL_4")
        
        self.teamlabel_4 = QtWidgets.QLabel(Widget)
        self.teamlabel_4.setGeometry(QtCore.QRect(320, 220, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_4.setFont(font)
        self.teamlabel_4.setObjectName("teamlabel_4")
       
        self.rank_4 = QtWidgets.QLabel(Widget)
        self.rank_4.setGeometry(QtCore.QRect(390, 240, 51, 16))
        self.rank_4.setObjectName("rank_4")
        
        self.tierL_4 = QtWidgets.QLabel(Widget)
        self.tierL_4.setGeometry(QtCore.QRect(350, 260, 91, 16))
        self.tierL_4.setObjectName("tierL_4")
      
        self.tier_4 = QtWidgets.QLabel(Widget)
        self.tier_4.setGeometry(QtCore.QRect(320, 260, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tier_4.setFont(font)
        self.tier_4.setObjectName("tier_4")
      
        self.workRank_4 = QtWidgets.QLabel(Widget)
        self.workRank_4.setGeometry(QtCore.QRect(320, 240, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_4.setFont(font)
        self.workRank_4.setObjectName("workRank_4")
       
        self.teamL_5 = QtWidgets.QLabel(Widget)
        self.teamL_5.setGeometry(QtCore.QRect(140, 300, 81, 16))
        self.teamL_5.setObjectName("teamL_5")
       
        self.teamlabel_5 = QtWidgets.QLabel(Widget)
        self.teamlabel_5.setGeometry(QtCore.QRect(100, 300, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_5.setFont(font)
        self.teamlabel_5.setObjectName("teamlabel_5")
       
        self.rank_5 = QtWidgets.QLabel(Widget)
        self.rank_5.setGeometry(QtCore.QRect(170, 320, 51, 16))
        self.rank_5.setObjectName("rank_5")
      
        self.tierL_5 = QtWidgets.QLabel(Widget)
        self.tierL_5.setGeometry(QtCore.QRect(130, 340, 91, 16))
        self.tierL_5.setObjectName("tierL_5")
      
        self.tier_5 = QtWidgets.QLabel(Widget)
        self.tier_5.setGeometry(QtCore.QRect(100, 340, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
       
        self.tier_5.setFont(font)
        self.tier_5.setObjectName("tier_5")
       
        self.workRank_5 = QtWidgets.QLabel(Widget)
        self.workRank_5.setGeometry(QtCore.QRect(100, 320, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_5.setFont(font)
        self.workRank_5.setObjectName("workRank_5")
       
        self.teamL_6 = QtWidgets.QLabel(Widget)
        self.teamL_6.setGeometry(QtCore.QRect(360, 300, 81, 16))
        self.teamL_6.setObjectName("teamL_6")
       
        self.teamlabel_6 = QtWidgets.QLabel(Widget)
        self.teamlabel_6.setGeometry(QtCore.QRect(320, 300, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_6.setFont(font)
        self.teamlabel_6.setObjectName("teamlabel_6")
       
        self.rank_6 = QtWidgets.QLabel(Widget)
        self.rank_6.setGeometry(QtCore.QRect(390, 320, 51, 16))
        self.rank_6.setObjectName("rank_6")
       
        self.tierL_6 = QtWidgets.QLabel(Widget)
        self.tierL_6.setGeometry(QtCore.QRect(350, 340, 91, 16))
        self.tierL_6.setObjectName("tierL_6")
      
        self.tier_6 = QtWidgets.QLabel(Widget)
        self.tier_6.setGeometry(QtCore.QRect(320, 340, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tier_6.setFont(font)
        self.tier_6.setObjectName("tier_6")
       
        self.workRank_6 = QtWidgets.QLabel(Widget)
        self.workRank_6.setGeometry(QtCore.QRect(320, 320, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_6.setFont(font)
        self.workRank_6.setObjectName("workRank_6")
       
        self.teamL_7 = QtWidgets.QLabel(Widget)
        self.teamL_7.setGeometry(QtCore.QRect(140, 380, 81, 16))
        self.teamL_7.setObjectName("teamL_7")
       
        self.teamlabel_7 = QtWidgets.QLabel(Widget)
        self.teamlabel_7.setGeometry(QtCore.QRect(100, 380, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_7.setFont(font)
        self.teamlabel_7.setObjectName("teamlabel_7")
        
        self.rank_7 = QtWidgets.QLabel(Widget)
        self.rank_7.setGeometry(QtCore.QRect(170, 400, 51, 16))
        self.rank_7.setObjectName("rank_7")
       
        self.tierL_7 = QtWidgets.QLabel(Widget)
        self.tierL_7.setGeometry(QtCore.QRect(130, 420, 91, 16))
        self.tierL_7.setObjectName("tierL_7")
      
        self.tier_7 = QtWidgets.QLabel(Widget)
        self.tier_7.setGeometry(QtCore.QRect(100, 420, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tier_7.setFont(font)
        self.tier_7.setObjectName("tier_7")
       
        self.workRank_7 = QtWidgets.QLabel(Widget)
        self.workRank_7.setGeometry(QtCore.QRect(100, 400, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_7.setFont(font)
        self.workRank_7.setObjectName("workRank_7")
       
        self.teamL_8 = QtWidgets.QLabel(Widget)
        self.teamL_8.setGeometry(QtCore.QRect(360, 380, 81, 16))
        self.teamL_8.setObjectName("teamL_8")
      
        self.teamlabel_8 = QtWidgets.QLabel(Widget)
        self.teamlabel_8.setGeometry(QtCore.QRect(320, 380, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.teamlabel_8.setFont(font)
        self.teamlabel_8.setObjectName("teamlabel_8")
       
        self.rank_8 = QtWidgets.QLabel(Widget)
        self.rank_8.setGeometry(QtCore.QRect(390, 400, 51, 16))
        self.rank_8.setObjectName("rank_8")
       
        self.tierL_8 = QtWidgets.QLabel(Widget)
        self.tierL_8.setGeometry(QtCore.QRect(350, 420, 91, 16))
        self.tierL_8.setObjectName("tierL_8")
       
        self.tier_8 = QtWidgets.QLabel(Widget)
        self.tier_8.setGeometry(QtCore.QRect(320, 420, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tier_8.setFont(font)
        self.tier_8.setObjectName("tier_8")
        
        self.workRank_8 = QtWidgets.QLabel(Widget)
        self.workRank_8.setGeometry(QtCore.QRect(320, 400, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.workRank_8.setFont(font)
        self.workRank_8.setObjectName("workRank_8")
        
        self.playerL_1 = QtWidgets.QLabel(Widget)
        self.playerL_1.setGeometry(QtCore.QRect(10, 160, 81, 16))
        self.playerL_1.setObjectName("playerL_1")
        
        self.playerL_2 = QtWidgets.QLabel(Widget)
        self.playerL_2.setGeometry(QtCore.QRect(160, 260, 81, 16))
        self.playerL_2.setObjectName("playerL_2")
        
        self.playerL_3 = QtWidgets.QLabel(Widget)
        self.playerL_3.setGeometry(QtCore.QRect(240, 160, 81, 16))
        self.playerL_3.setObjectName("playerL_3")
        
        self.playerL_4 = QtWidgets.QLabel(Widget)
        self.playerL_4.setGeometry(QtCore.QRect(10, 240, 81, 16))
        self.playerL_4.setObjectName("playerL_4")
        
        self.playerL_5 = QtWidgets.QLabel(Widget)
        self.playerL_5.setGeometry(QtCore.QRect(240, 240, 81, 16))
        self.playerL_5.setObjectName("playerL_5")
        
        self.playerL_6 = QtWidgets.QLabel(Widget)
        self.playerL_6.setGeometry(QtCore.QRect(10, 320, 81, 16))
        self.playerL_6.setObjectName("playerL_6")
        
        self.playerL_7 = QtWidgets.QLabel(Widget)
        self.playerL_7.setGeometry(QtCore.QRect(240, 320, 81, 16))
        self.playerL_7.setObjectName("playerL_7")
       
        self.playerL_8 = QtWidgets.QLabel(Widget)
        self.playerL_8.setGeometry(QtCore.QRect(10, 400, 81, 16))
        self.playerL_8.setObjectName("playerL_8")
        
        self.playerL_9 = QtWidgets.QLabel(Widget)
        self.playerL_9.setGeometry(QtCore.QRect(240, 400, 81, 16))
        self.playerL_9.setObjectName("playerL_9")
        
        ##VRML Parts
        self.teamVRML = QtWidgets.QLabel(Widget)
        self.teamVRML.setGeometry(QtCore.QRect(290, 510, 81, 16))
        self.teamVRML.setObjectName("teamVRML")
        self.rankVRML = QtWidgets.QLabel(Widget)
        self.rankVRML.setGeometry(QtCore.QRect(320, 540, 51, 16))
        self.rankVRML.setObjectName("rankVRML")
        self.tierVRML = QtWidgets.QLabel(Widget)
        self.tierVRML.setGeometry(QtCore.QRect(280, 570, 91, 16))
        self.tierVRML.setObjectName("tierVRML")



        self.foundTeamName = "..."
        self.foundRanking = "..."
        self.foundDivision = "..."
        self.VRMLextraStats = []

        self.players = ["", "", "", "", "", "", "", ""]
        self.teams = ["", "", "", "", "", "", "", ""]
        self.ranks = ["", "", "", "", "", "", "", ""]
        self.tiers = ["", "", "", "", "", "", "", ""]

        self.extraStats = [[],[],[],[],[],[],[],[]]

        ### More Info Buttons
        self.moreInfo1 = QtWidgets.QPushButton(Widget)
        self.moreInfo1.setGeometry(QtCore.QRect(10, 180, 60, 25))
        self.moreInfo1.clicked.connect(lambda: self.loadMoreInfo(self.players[0]))

        self.moreInfo2 = QtWidgets.QPushButton(Widget)
        self.moreInfo2.setGeometry(QtCore.QRect(10 + 225, 180, 60, 25))
        self.moreInfo2.clicked.connect(lambda: self.loadMoreInfo(self.players[1]))

        self.moreInfo3 = QtWidgets.QPushButton(Widget)
        self.moreInfo3.setGeometry(QtCore.QRect(10, 180 + 80, 60, 25))
        self.moreInfo3.clicked.connect(lambda: self.loadMoreInfo(self.players[2]))

        self.moreInfo4 = QtWidgets.QPushButton(Widget)
        self.moreInfo4.setGeometry(QtCore.QRect(10+225, 180 + 80, 60, 25))
        self.moreInfo4.clicked.connect(lambda: self.loadMoreInfo(self.players[3]))

        self.moreInfo5 = QtWidgets.QPushButton(Widget)
        self.moreInfo5.setGeometry(QtCore.QRect(10, 180 + 160, 60, 25))
        self.moreInfo5.clicked.connect(lambda: self.loadMoreInfo(self.players[4]))

        self.moreInfo6 = QtWidgets.QPushButton(Widget)
        self.moreInfo6.setGeometry(QtCore.QRect(10 + 225, 180 + 160, 60, 25))
        self.moreInfo6.clicked.connect(lambda: self.loadMoreInfo(self.players[5]))

        self.moreInfo7 = QtWidgets.QPushButton(Widget)
        self.moreInfo7.setGeometry(QtCore.QRect(10, 180 + 240, 60, 25))
        self.moreInfo7.clicked.connect(lambda: self.loadMoreInfo(self.players[6]))

        self.moreInfo8 = QtWidgets.QPushButton(Widget)
        self.moreInfo8.setGeometry(QtCore.QRect(10+225, 180 + 240, 60, 25))
        self.moreInfo8.clicked.connect(lambda: self.loadMoreInfo(self.players[7]))

        self.moreInfoButtons = [self.moreInfo1, self.moreInfo2, self.moreInfo3, self.moreInfo4, self.moreInfo5, self.moreInfo6, self.moreInfo7, self.moreInfo8]


        ### Update System
        self.updateButton = QtWidgets.QPushButton(Widget)
        self.updateButton.setGeometry(QtCore.QRect(320, 10, 125, 25))
        self.updateButton.clicked.connect(self.update)
        self.threadpool.start(self.checkForUpdate)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.PubTitle.setText(_translate("Widget", "Pub Player Search"))
        self.VRMLTitle.setText(_translate("Widget", "VRML Player Search"))
        self.pubSearchButton.setText(_translate("Widget", "Get Player Stats"))
        
        self.ipLabel.setText(_translate("Widget", "IP Address"))
        self.portLabel.setText(_translate("Widget", "Port Number"))
        self.ipLabel_2.setText(_translate("Widget", "(Leave blank if on PC)"))
        self.ipLabel_3.setText(_translate("Widget", "(Leave blank if on PC)"))
        
        self.playerTitle_1.setText(_translate("Widget", "Player"))
        self.playerTitle_2.setText(_translate("Widget", "Player"))
        self.playerTitle_3.setText(_translate("Widget", "Player"))
        self.playerTitle_4.setText(_translate("Widget", "Player"))
        self.playerTitle_5.setText(_translate("Widget", "Player"))
        self.playerTitle_6.setText(_translate("Widget", "Player"))
        self.playerTitle_7.setText(_translate("Widget", "Player"))
        self.playerTitle_8.setText(_translate("Widget", "Player"))
        
        self.teamlabel_1.setText(_translate("Widget", "Team: "))
        self.workRank_1.setText(_translate("Widget", "World Rank:"))
        self.tier_1.setText(_translate("Widget", "Tier:"))
        
        self.vrmlPlayerTitle.setText(_translate("Widget", "Player Name"))

        self.vrmlSearchButton.setText(_translate("Widget", "Search VRML\n" "Database"))
        
        self.vrmlRank.setText(_translate("Widget", "World Rank:"))
        self.vrmlTeam.setText(_translate("Widget", "Team: "))
        self.vrmlTier.setText(_translate("Widget", "Tier:"))
        
        self.teamL_1.setText(_translate("Widget", f"{self.teams[0]}"))
        self.rank_1.setText(_translate("Widget", f"{self.ranks[0]}"))
        self.tierL_1.setText(_translate("Widget", f"{self.tiers[0]}"))
        self.teamL_2.setText(_translate("Widget", f"{self.teams[1]}"))
        self.teamlabel_2.setText(_translate("Widget", "Team: "))
        self.rank_2.setText(_translate("Widget", f"{self.ranks[1]}"))
        self.tierL_2.setText(_translate("Widget", f"{self.tiers[1]}"))
        self.tier_2.setText(_translate("Widget", "Tier:"))
        self.workRank_2.setText(_translate("Widget", "World Rank:"))
        self.teamL_3.setText(_translate("Widget", f"{self.teams[2]}"))
        self.teamlabel_3.setText(_translate("Widget", "Team: "))
        self.rank_3.setText(_translate("Widget", f"{self.ranks[2]}"))
        self.tierL_3.setText(_translate("Widget", f"{self.tiers[2]}"))
        self.tier_3.setText(_translate("Widget", "Tier:"))
        self.workRank_3.setText(_translate("Widget", "World Rank:"))
        self.teamL_4.setText(_translate("Widget", f"{self.teams[3]}"))
        self.teamlabel_4.setText(_translate("Widget", "Team: "))
        self.rank_4.setText(_translate("Widget",f"{self.ranks[3]}"))
        self.tierL_4.setText(_translate("Widget", f"{self.tiers[3]}"))
        self.tier_4.setText(_translate("Widget", "Tier:"))
        self.workRank_4.setText(_translate("Widget", "World Rank:"))
        self.teamL_5.setText(_translate("Widget", f"{self.teams[4]}"))
        self.teamlabel_5.setText(_translate("Widget", "Team: "))
        self.rank_5.setText(_translate("Widget", f"{self.ranks[4]}"))
        self.tierL_5.setText(_translate("Widget", f"{self.tiers[4]}"))
        self.tier_5.setText(_translate("Widget", "Tier:"))
        self.workRank_5.setText(_translate("Widget", "World Rank:"))
        self.teamL_6.setText(_translate("Widget", f"{self.teams[5]}"))
        self.teamlabel_6.setText(_translate("Widget", "Team: "))
        self.rank_6.setText(_translate("Widget", f"{self.ranks[5]}"))
        self.tierL_6.setText(_translate("Widget", f"{self.tiers[5]}"))
        self.tier_6.setText(_translate("Widget", "Tier:"))
        self.workRank_6.setText(_translate("Widget", "World Rank:"))
        self.teamL_7.setText(_translate("Widget", f"{self.teams[6]}"))
        self.teamlabel_7.setText(_translate("Widget", "Team: "))
        self.rank_7.setText(_translate("Widget", f"{self.ranks[6]}"))
        self.tierL_7.setText(_translate("Widget", f"{self.tiers[6]}"))
        self.tier_7.setText(_translate("Widget", "Tier:"))
        self.workRank_7.setText(_translate("Widget", "World Rank:"))
        self.teamL_8.setText(_translate("Widget", f"{self.teams[7]}"))
        self.teamlabel_8.setText(_translate("Widget", "Team: "))
        self.rank_8.setText(_translate("Widget", f"{self.ranks[7]}"))
        self.tierL_8.setText(_translate("Widget", f"{self.tiers[7]}"))
        self.tier_8.setText(_translate("Widget", "Tier:"))
        self.workRank_8.setText(_translate("Widget", "World Rank:"))
        
        self.playerL_1.setText(_translate("Widget", f"{self.players[0]}"))
        self.playerL_2.setText(_translate("Widget", ""))
        self.playerL_3.setText(_translate("Widget", f"{self.players[1]}"))
        self.playerL_4.setText(_translate("Widget", f"{self.players[2]}"))
        self.playerL_5.setText(_translate("Widget", f"{self.players[3]}"))
        self.playerL_6.setText(_translate("Widget", f"{self.players[4]}"))
        self.playerL_7.setText(_translate("Widget", f"{self.players[5]}"))
        self.playerL_8.setText(_translate("Widget", f"{self.players[6]}"))
        self.playerL_9.setText(_translate("Widget", f"{self.players[7]}"))
        
        self.teamVRML.setText(_translate("Widget", f"{self.foundTeamName}"))
        self.rankVRML.setText(_translate("Widget", f"{self.foundRanking}"))
        self.tierVRML.setText(_translate("Widget", f"{self.foundDivision}"))

        self.moreInfo1.setText(_translate("Widget", "More Info"))
        self.moreInfo2.setText(_translate("Widget", "More Info"))
        self.moreInfo3.setText(_translate("Widget", "More Info"))
        self.moreInfo4.setText(_translate("Widget", "More Info"))
        self.moreInfo5.setText(_translate("Widget", "More Info"))
        self.moreInfo6.setText(_translate("Widget", "More Info"))
        self.moreInfo7.setText(_translate("Widget", "More Info"))
        self.moreInfo8.setText(_translate("Widget", "More Info"))

        self.moreInfoVRML.setText(_translate("Widget", "More Info"))

        # Hide more info buttons
        for index in range(0, len(self.moreInfoButtons)):
            if self.tiers[index] == "" or self.tiers[index] == None or self.tiers[index] == "..." or self.players[index] == "...":
                self.moreInfoButtons[index].hide()
            else:
                self.moreInfoButtons[index].show()
        
        if self.foundTeamName == "...":
            self.moreInfoVRML.hide()
        else:
            self.moreInfoVRML.show()
    
    def searchForVRMLPlayer(self):
        self.playerName = self.PlayerNameInput.toPlainText()
        if self.playerName == None or self.playerName == "": ##Filter missing names
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Please enter a player name")
            msgBox.setWindowTitle("No Player Entered")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else: 
            main = VRMLMain('https://api.vrmasterleague.com/', str(self.playerName))
            results = main.completeSearch()
            self.foundTeamName = results[0]
            self.foundRanking = str(results[1])
            self.foundDivision = str(results[2])
            self.VRMLextraStats = results[3]
            self.retranslateUi(Widget)

    def searchForPubPlayer(self):
        
        self.pubSearchButton.setDisabled(True)
        self.clearPubStats()

        #Get IP and Port
        self.ip = self.ipInput.toPlainText()
        self.port = self.portInput.toPlainText()


        #Check and fix ports
        if len(self.ip.split(".")) != 4: ##Invalid or missing IP Address
            self.ip = "127.0.0.1"
            print("Empty or Invalid IP, using default")
        if (self.port == None) or (self.port == ""):
            self.port = "6721"
            print("Empty or Invalid Port, using default")
        
        #Execute pub player finder scripts
        self.pubBackground()
        self.populatePubPlayers()
    
    def clearPubStats(self):
        ## CLEAR INFO TO PREVENT CROSS-OVER STATS
        for i in range(0, len(self.players)):
            self.players[i], self.teams[i], self.ranks[i], self.tiers[i] = "...", "...", "...", "..."
        
        self.retranslateUi(Widget)

    def clearVRMLStats(self):

        ## CLEAR INFO TO PREVENT CROSS-OVER STATS
        self.foundDivision = "..."
        self.foundRanking = "..."
        self.foundTeamName = "..."
        
        self.retranslateUi(Widget)

    def populatePubPlayers(self):
        for i in range(0, len(self.names)):
            self.players[i] = self.names[i]
        for i in range(0, len(self.players)):
            if self.players[i] == "":
                self.players[i] = "..."
        self.multithreadWorker = multithreadVRMLSearch(self.players)
        self.threadpool.start(self.multithreadWorker)
        self.retranslateUi(Widget)
        
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

    def loadMoreInfo(self, username):
        index = self.players.index(username)
        informationString = f"""
        Player Name: {self.players[index]}\n
        Team: {self.teams[index]}\n
        Region: {self.extraStats[index][7]}\n
        Division: {self.tiers[index]}\n
        Team Worldwide Rank: {self.ranks[index]}\n
        Team Region Rank: {self.extraStats[index][0]}\n
        Team MMR: {self.extraStats[index][6]}\n
        Team Games Played: {self.extraStats[index][1]}\n
        Team Wins: {self.extraStats[index][2]}\n
        Team Losses: {self.extraStats[index][4]}\n
        Team Ties: {self.extraStats[index][3]}\n
        Team Points: {self.extraStats[index][5]}\n
        Is This Team Recruiting: {self.extraStats[index][8]}\n
        """
        alert = QMessageBox()
        alert.setText(informationString)
        alert.setWindowTitle("Extra Information")
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec()

    def loadMoreInfoVRML(self):

        informationString = f"""
        Player Name: {self.playerName}\n
        Team: {self.foundTeamName}\n
        Region: {self.VRMLextraStats[7]}\n
        Division: {self.foundDivision}\n
        Team Worldwide Rank: {self.foundRanking}\n
        Team Region Rank: {self.VRMLextraStats[0]}\n
        Team MMR: {self.VRMLextraStats[6]}\n
        Team Games Played: {self.VRMLextraStats[1]}\n
        Team Wins: {self.VRMLextraStats[2]}\n
        Team Losses: {self.VRMLextraStats[4]}\n
        Team Ties: {self.VRMLextraStats[3]}\n
        Team Points: {self.VRMLextraStats[5]}\n
        Is This Team Recruiting: {self.VRMLextraStats[8]}\n
        """
        alert = QMessageBox()
        alert.setText(informationString)
        alert.setWindowTitle("Extra Information")
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec()

    def update(self):
        webbrowser.open("https://github.com/Slaymish/EchoStatsFinder/releases")
    
    def checkForUpdate(self):
        _translate = QtCore.QCoreApplication.translate
        self.updateButton.setDisabled(True)
        self.updateButton.setText(_translate("Widget", "Checking for update..."))

        try:
            r = requests.get("https://raw.githubusercontent.com/Slaymish/EchoStatsFinder/main/gui.py")

            remoteVersion = str(re.findall('__version__ = "(.*)"', r.text)[0])
            localVersion = __version__

            if __beta__:
                self.updateButton.setText(_translate("Widget", "Update Beta Version"))
                self.updateButton.setDisabled(False)
            else:
                if remoteVersion != localVersion:
                    self.updateButton.setDisabled(False)
                    self.updateButton.setText(_translate("Widget", "Update Available!"))
                else:
                    self.updateButton.setText(_translate("Widget", "No update available"))
        except Exception as e:
            print("Update search failed, aborting.")

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
        twoDimIndivStats = []

        for name in self.names:
            individualStat = []
            vrmlInfo.username = name
            res = vrmlInfo.completeSearch()
            for stat in res: ## Convert stats from dictionary to array
                individualStat.append(stat)
            self.stats.append(individualStat)
        for i in range(0, len(self.stats)):
            ui.teams[i] = self.stats[i][0]
            ui.ranks[i] = self.stats[i][1]
            ui.tiers[i] = self.stats[i][2]
            ui.extraStats[i] = self.stats[i][3]
        
        ui.pubSearchButton.setDisabled(False)
        ui.retranslateUi(Widget)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = MainWindow()

    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())