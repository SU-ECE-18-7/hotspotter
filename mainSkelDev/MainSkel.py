# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainSkel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainSkel(object):
    def setupUi(self, mainSkel):
        mainSkel.setObjectName(_fromUtf8("mainSkel"))
        mainSkel.setWindowModality(QtCore.Qt.NonModal)
        mainSkel.resize(780, 480)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 25, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        mainSkel.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/hsicon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainSkel.setWindowIcon(icon)
        mainSkel.setDocumentMode(False)
        mainSkel.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(mainSkel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TableTabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableTabWidget.sizePolicy().hasHeightForWidth())
        self.TableTabWidget.setSizePolicy(sizePolicy)
        self.TableTabWidget.setMaximumSize(QtCore.QSize(16777215, 1200))
        self.TableTabWidget.setTabsClosable(False)
        self.TableTabWidget.setObjectName(_fromUtf8("TableTabWidget"))
        self.imageTab = QtGui.QWidget()
        self.imageTab.setObjectName(_fromUtf8("imageTab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.imageTab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.imageView = QtGui.QVBoxLayout()
        self.imageView.setObjectName(_fromUtf8("imageView"))
        self.gxs_TBL = QtGui.QTableWidget(self.imageTab)
        self.gxs_TBL.setAutoFillBackground(True)
        self.gxs_TBL.setObjectName(_fromUtf8("gxs_TBL"))
        self.gxs_TBL.setColumnCount(0)
        self.gxs_TBL.setRowCount(0)
        self.gxs_TBL.horizontalHeader().setCascadingSectionResizes(True)
        self.gxs_TBL.horizontalHeader().setDefaultSectionSize(150)
        self.gxs_TBL.horizontalHeader().setStretchLastSection(True)
        self.gxs_TBL.verticalHeader().setCascadingSectionResizes(False)
        self.imageView.addWidget(self.gxs_TBL)
        self.verticalLayout_6.addLayout(self.imageView)
        self.horizontalGroupBox = QtGui.QGroupBox(self.imageTab)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(self.horizontalGroupBox)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.AutoChip = QtGui.QPushButton(self.horizontalGroupBox)
        self.AutoChip.setObjectName(_fromUtf8("AutoChip"))
        self.horizontalLayout_4.addWidget(self.AutoChip)
        self.verticalLayout_6.addWidget(self.horizontalGroupBox)
        self.TableTabWidget.addTab(self.imageTab, _fromUtf8(""))
        self.chipTab = QtGui.QWidget()
        self.chipTab.setObjectName(_fromUtf8("chipTab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.chipTab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.chipView = QtGui.QVBoxLayout()
        self.chipView.setObjectName(_fromUtf8("chipView"))
        self.cxs_TBL = QtGui.QTableWidget(self.chipTab)
        self.cxs_TBL.setObjectName(_fromUtf8("cxs_TBL"))
        self.cxs_TBL.setColumnCount(0)
        self.cxs_TBL.setRowCount(0)
        self.chipView.addWidget(self.cxs_TBL)
        self.verticalLayout_7.addLayout(self.chipView)
        self.horizontalGroupBox1 = QtGui.QGroupBox(self.chipTab)
        self.horizontalGroupBox1.setObjectName(_fromUtf8("horizontalGroupBox1"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalGroupBox1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.AutoQuery = QtGui.QPushButton(self.horizontalGroupBox1)
        self.AutoQuery.setObjectName(_fromUtf8("AutoQuery"))
        self.horizontalLayout_5.addWidget(self.AutoQuery)
        self.Cluster = QtGui.QPushButton(self.horizontalGroupBox1)
        self.Cluster.setObjectName(_fromUtf8("Cluster"))
        self.horizontalLayout_5.addWidget(self.Cluster)
        self.ShowMatrices = QtGui.QPushButton(self.horizontalGroupBox1)
        self.ShowMatrices.setObjectName(_fromUtf8("ShowMatrices"))
        self.horizontalLayout_5.addWidget(self.ShowMatrices)
        self.SortToFolders = QtGui.QPushButton(self.horizontalGroupBox1)
        self.SortToFolders.setObjectName(_fromUtf8("SortToFolders"))
        self.horizontalLayout_5.addWidget(self.SortToFolders)
        self.verticalLayout_7.addWidget(self.horizontalGroupBox1)
        self.TableTabWidget.addTab(self.chipTab, _fromUtf8(""))
        self.nameTab = QtGui.QWidget()
        self.nameTab.setObjectName(_fromUtf8("nameTab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.nameTab)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.nameView = QtGui.QVBoxLayout()
        self.nameView.setObjectName(_fromUtf8("nameView"))
        self.nxs_TBL = QtGui.QTableWidget(self.nameTab)
        self.nxs_TBL.setObjectName(_fromUtf8("nxs_TBL"))
        self.nxs_TBL.setColumnCount(0)
        self.nxs_TBL.setRowCount(0)
        self.nameView.addWidget(self.nxs_TBL)
        self.verticalLayout_8.addLayout(self.nameView)
        self.TableTabWidget.addTab(self.nameTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.TableTabWidget, 2, 0, 1, 1)
        self.logo_space = QtGui.QGroupBox(self.centralwidget)
        self.logo_space.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_space.sizePolicy().hasHeightForWidth())
        self.logo_space.setSizePolicy(sizePolicy)
        self.logo_space.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logo_space.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.logo_space.setAcceptDrops(False)
        self.logo_space.setAccessibleDescription(_fromUtf8(""))
        self.logo_space.setFlat(False)
        self.logo_space.setCheckable(False)
        self.logo_space.setObjectName(_fromUtf8("logo_space"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.logo_space)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.logo_space)
        self.label_2.setMaximumSize(QtCore.QSize(175, 60))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/SeattleUMain-red-background.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.logo_space)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(75, 75))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/hsicon.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.PantheraLogo = QtGui.QLabel(self.logo_space)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PantheraLogo.sizePolicy().hasHeightForWidth())
        self.PantheraLogo.setSizePolicy(sizePolicy)
        self.PantheraLogo.setMaximumSize(QtCore.QSize(150, 75))
        self.PantheraLogo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PantheraLogo.setText(_fromUtf8(""))
        self.PantheraLogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Logo_DarkBackgrounds.png")))
        self.PantheraLogo.setScaledContents(True)
        self.PantheraLogo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PantheraLogo.setWordWrap(False)
        self.PantheraLogo.setObjectName(_fromUtf8("PantheraLogo"))
        self.horizontalLayout.addWidget(self.PantheraLogo)
        self.gridLayout.addWidget(self.logo_space, 0, 0, 1, 1)
        mainSkel.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainSkel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        self.menuBatch = QtGui.QMenu(self.menubar)
        self.menuBatch.setObjectName(_fromUtf8("menuBatch"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        mainSkel.setMenuBar(self.menubar)
        self.actionNew_Database = QtGui.QAction(mainSkel)
        self.actionNew_Database.setObjectName(_fromUtf8("actionNew_Database"))
        self.actionOpen_Database = QtGui.QAction(mainSkel)
        self.actionOpen_Database.setObjectName(_fromUtf8("actionOpen_Database"))
        self.actionSave_Database = QtGui.QAction(mainSkel)
        self.actionSave_Database.setObjectName(_fromUtf8("actionSave_Database"))
        self.actionImport_Images_Select_file_s = QtGui.QAction(mainSkel)
        self.actionImport_Images_Select_file_s.setObjectName(_fromUtf8("actionImport_Images_Select_file_s"))
        self.actionImport_Images_Select_Directory = QtGui.QAction(mainSkel)
        self.actionImport_Images_Select_Directory.setObjectName(_fromUtf8("actionImport_Images_Select_Directory"))
        self.actionQuit = QtGui.QAction(mainSkel)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAdd_Chip = QtGui.QAction(mainSkel)
        self.actionAdd_Chip.setObjectName(_fromUtf8("actionAdd_Chip"))
        self.actionNew_Chip_Property = QtGui.QAction(mainSkel)
        self.actionNew_Chip_Property.setObjectName(_fromUtf8("actionNew_Chip_Property"))
        self.actionQuery = QtGui.QAction(mainSkel)
        self.actionQuery.setObjectName(_fromUtf8("actionQuery"))
        self.actionReselect_ROI = QtGui.QAction(mainSkel)
        self.actionReselect_ROI.setObjectName(_fromUtf8("actionReselect_ROI"))
        self.actionReselect_Orientation = QtGui.QAction(mainSkel)
        self.actionReselect_Orientation.setObjectName(_fromUtf8("actionReselect_Orientation"))
        self.actionSelect_Next = QtGui.QAction(mainSkel)
        self.actionSelect_Next.setObjectName(_fromUtf8("actionSelect_Next"))
        self.actionDelete_Chip = QtGui.QAction(mainSkel)
        self.actionDelete_Chip.setObjectName(_fromUtf8("actionDelete_Chip"))
        self.actionDelete_Image = QtGui.QAction(mainSkel)
        self.actionDelete_Image.setObjectName(_fromUtf8("actionDelete_Image"))
        self.actionPrecompute_Chips_Features = QtGui.QAction(mainSkel)
        self.actionPrecompute_Chips_Features.setObjectName(_fromUtf8("actionPrecompute_Chips_Features"))
        self.actionPrecompute_Queries = QtGui.QAction(mainSkel)
        self.actionPrecompute_Queries.setObjectName(_fromUtf8("actionPrecompute_Queries"))
        self.actionScale_All_ROIs = QtGui.QAction(mainSkel)
        self.actionScale_All_ROIs.setObjectName(_fromUtf8("actionScale_All_ROIs"))
        self.actionConvert_All_Images_into_Chips = QtGui.QAction(mainSkel)
        self.actionConvert_All_Images_into_Chips.setObjectName(_fromUtf8("actionConvert_All_Images_into_Chips"))
        self.actionLayout_Figures = QtGui.QAction(mainSkel)
        self.actionLayout_Figures.setObjectName(_fromUtf8("actionLayout_Figures"))
        self.actionAbout = QtGui.QAction(mainSkel)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionView_Documentation = QtGui.QAction(mainSkel)
        self.actionView_Documentation.setObjectName(_fromUtf8("actionView_Documentation"))
        self.actionView_Database_Dir = QtGui.QAction(mainSkel)
        self.actionView_Database_Dir.setObjectName(_fromUtf8("actionView_Database_Dir"))
        self.actionView_Computed_Dir = QtGui.QAction(mainSkel)
        self.actionView_Computed_Dir.setObjectName(_fromUtf8("actionView_Computed_Dir"))
        self.actionView_Global_Dir = QtGui.QAction(mainSkel)
        self.actionView_Global_Dir.setObjectName(_fromUtf8("actionView_Global_Dir"))
        self.actionWrite_Logs = QtGui.QAction(mainSkel)
        self.actionWrite_Logs.setObjectName(_fromUtf8("actionWrite_Logs"))
        self.actionDelete_Cached_Query_Results = QtGui.QAction(mainSkel)
        self.actionDelete_Cached_Query_Results.setObjectName(_fromUtf8("actionDelete_Cached_Query_Results"))
        self.actionDelete_Computed_Directory = QtGui.QAction(mainSkel)
        self.actionDelete_Computed_Directory.setObjectName(_fromUtf8("actionDelete_Computed_Directory"))
        self.actionDelete_Global_Preferences = QtGui.QAction(mainSkel)
        self.actionDelete_Global_Preferences.setObjectName(_fromUtf8("actionDelete_Global_Preferences"))
        self.actionDeveloper_Mode_IPython = QtGui.QAction(mainSkel)
        self.actionDeveloper_Mode_IPython.setObjectName(_fromUtf8("actionDeveloper_Mode_IPython"))
        self.actionDeveloper_Reload = QtGui.QAction(mainSkel)
        self.actionDeveloper_Reload.setObjectName(_fromUtf8("actionDeveloper_Reload"))
        self.menuFile.addAction(self.actionNew_Database)
        self.menuFile.addAction(self.actionOpen_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Images_Select_file_s)
        self.menuFile.addAction(self.actionImport_Images_Select_Directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuActions.addAction(self.actionAdd_Chip)
        self.menuActions.addAction(self.actionNew_Chip_Property)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionQuery)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionReselect_ROI)
        self.menuActions.addAction(self.actionReselect_Orientation)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionSelect_Next)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionDelete_Chip)
        self.menuActions.addAction(self.actionDelete_Image)
        self.menuBatch.addAction(self.actionPrecompute_Chips_Features)
        self.menuBatch.addAction(self.actionPrecompute_Queries)
        self.menuBatch.addSeparator()
        self.menuBatch.addAction(self.actionScale_All_ROIs)
        self.menuBatch.addSeparator()
        self.menuBatch.addAction(self.actionConvert_All_Images_into_Chips)
        self.menuOptions.addAction(self.actionLayout_Figures)
        self.menuOptions.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionView_Documentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionView_Database_Dir)
        self.menuHelp.addAction(self.actionView_Computed_Dir)
        self.menuHelp.addAction(self.actionView_Global_Dir)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionWrite_Logs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDelete_Cached_Query_Results)
        self.menuHelp.addAction(self.actionDelete_Computed_Directory)
        self.menuHelp.addAction(self.actionDelete_Global_Preferences)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDeveloper_Mode_IPython)
        self.menuHelp.addAction(self.actionDeveloper_Reload)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuBatch.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainSkel)
        self.TableTabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mainSkel)

    def retranslateUi(self, mainSkel):
        mainSkel.setWindowTitle(_translate("mainSkel", "HotSpotter", None))
        self.pushButton.setText(_translate("mainSkel", "Import Image(s)", None))
        self.AutoChip.setText(_translate("mainSkel", "AutoChip", None))
        self.TableTabWidget.setTabText(self.TableTabWidget.indexOf(self.imageTab), _translate("mainSkel", "Image Table", None))
        self.AutoQuery.setText(_translate("mainSkel", "AutoQuery", None))
        self.Cluster.setText(_translate("mainSkel", "Cluster", None))
        self.ShowMatrices.setText(_translate("mainSkel", "Show Matrices", None))
        self.SortToFolders.setText(_translate("mainSkel", "Sort to Folders", None))
        self.TableTabWidget.setTabText(self.TableTabWidget.indexOf(self.chipTab), _translate("mainSkel", "Chip Table", None))
        self.TableTabWidget.setTabText(self.TableTabWidget.indexOf(self.nameTab), _translate("mainSkel", "Name View", None))
        self.menuFile.setTitle(_translate("mainSkel", "File", None))
        self.menuActions.setTitle(_translate("mainSkel", "Actions", None))
        self.menuBatch.setTitle(_translate("mainSkel", "Batch", None))
        self.menuOptions.setTitle(_translate("mainSkel", "Options", None))
        self.menuHelp.setTitle(_translate("mainSkel", "Help", None))
        self.actionNew_Database.setText(_translate("mainSkel", "New Database", None))
        self.actionOpen_Database.setText(_translate("mainSkel", "Open Database", None))
        self.actionSave_Database.setText(_translate("mainSkel", "Save Database", None))
        self.actionImport_Images_Select_file_s.setText(_translate("mainSkel", "Import Images (Select file(s))", None))
        self.actionImport_Images_Select_Directory.setText(_translate("mainSkel", "Import Images (Select Directory)", None))
        self.actionQuit.setText(_translate("mainSkel", "Quit", None))
        self.actionAdd_Chip.setText(_translate("mainSkel", "Add Chip", None))
        self.actionNew_Chip_Property.setText(_translate("mainSkel", "New Chip Property", None))
        self.actionQuery.setText(_translate("mainSkel", "Query", None))
        self.actionReselect_ROI.setText(_translate("mainSkel", "Reselect ROI", None))
        self.actionReselect_Orientation.setText(_translate("mainSkel", "Reselect Orientation", None))
        self.actionSelect_Next.setText(_translate("mainSkel", "Select Next", None))
        self.actionDelete_Chip.setText(_translate("mainSkel", "Delete Chip", None))
        self.actionDelete_Image.setText(_translate("mainSkel", "Delete Image", None))
        self.actionPrecompute_Chips_Features.setText(_translate("mainSkel", "Precompute Chips/Features", None))
        self.actionPrecompute_Queries.setText(_translate("mainSkel", "Precompute Queries", None))
        self.actionScale_All_ROIs.setText(_translate("mainSkel", "Scale All ROIs", None))
        self.actionConvert_All_Images_into_Chips.setText(_translate("mainSkel", "Convert All Images into Chips", None))
        self.actionLayout_Figures.setText(_translate("mainSkel", "Layout Figures", None))
        self.actionAbout.setText(_translate("mainSkel", "About", None))
        self.actionView_Documentation.setText(_translate("mainSkel", "View Documentation", None))
        self.actionView_Database_Dir.setText(_translate("mainSkel", "View Database Dir", None))
        self.actionView_Computed_Dir.setText(_translate("mainSkel", "View Computed Dir", None))
        self.actionView_Global_Dir.setText(_translate("mainSkel", "View Global Dir", None))
        self.actionWrite_Logs.setText(_translate("mainSkel", "Write Logs", None))
        self.actionDelete_Cached_Query_Results.setText(_translate("mainSkel", "Delete Cached Query Results", None))
        self.actionDelete_Computed_Directory.setText(_translate("mainSkel", "Delete Computed Directory", None))
        self.actionDelete_Global_Preferences.setText(_translate("mainSkel", "Delete Global Preferences", None))
        self.actionDeveloper_Mode_IPython.setText(_translate("mainSkel", "Developer Mode (IPython)", None))
        self.actionDeveloper_Reload.setText(_translate("mainSkel", "Developer Reload", None))

import resources_MainSkel_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainSkel = QtGui.QMainWindow()
    ui = Ui_mainSkel()
    ui.setupUi(mainSkel)
    mainSkel.show()
    sys.exit(app.exec_())

