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
        mainSkel.resize(922, 558)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
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
        self.centralwidget = QtGui.QWidget(mainSkel)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.horizontalGroupBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox.setSizePolicy(sizePolicy)
        self.horizontalGroupBox.setMaximumSize(QtCore.QSize(1200, 90))
        self.horizontalGroupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.horizontalGroupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 100, 0)
        self.horizontalLayout.setSpacing(150)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.PantheraLogo = QtGui.QLabel(self.horizontalGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PantheraLogo.sizePolicy().hasHeightForWidth())
        self.PantheraLogo.setSizePolicy(sizePolicy)
        self.PantheraLogo.setMaximumSize(QtCore.QSize(150, 75))
        self.PantheraLogo.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.PantheraLogo.setText(_fromUtf8(""))
        self.PantheraLogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Logo_DarkBackgrounds.png")))
        #self.PantheraLogo.setPixmap(QtGui.QPixmap(_fromUtf8("~/code/hotspotter/hsgui/_frontend/Logo_DarkBackgrounds.png")))
        self.PantheraLogo.setScaledContents(True)
        self.PantheraLogo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PantheraLogo.setWordWrap(False)
        self.PantheraLogo.setObjectName(_fromUtf8("PantheraLogo"))
        self.horizontalLayout.addWidget(self.PantheraLogo)
        self.label = QtGui.QLabel(self.horizontalGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(75, 75))
        #self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/hsicon.png")))
        #self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../code/hsgui/_frontend/hsicon.png")))
       # self.label.setPixmap(QtGui.QPixmap(_fromUtf8("~/code/hotspotter/hsgui/_frontend/hsicon.ico")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalGroupBox)
        self.label_2.setMaximumSize(QtCore.QSize(175, 60))
       # self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/SeattleUMain-red-background.png")))
       # self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../code/hsgui/_frontend/SeattleUMain-red-background.png")))
        #self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("~code/hotspotter/hsgui/_frontend/SeattleUMain-red-background.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox)
        self.tablesTabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablesTabWidget.sizePolicy().hasHeightForWidth())
        self.tablesTabWidget.setSizePolicy(sizePolicy)
        self.tablesTabWidget.setMaximumSize(QtCore.QSize(16777215, 1200))
        self.tablesTabWidget.setTabsClosable(False)
        self.tablesTabWidget.setObjectName(_fromUtf8("tablesTabWidget"))
        self.imageTab = QtGui.QWidget()
        self.imageTab.setObjectName(_fromUtf8("imageTab"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.imageTab)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.imageView = QtGui.QVBoxLayout()
        self.imageView.setObjectName(_fromUtf8("imageView"))
        #self.gxs_TBL = QtGui.QListWidget(self.imageTab)
        self.gxs_TBL = QtGui.QTableWidget(self.imageTab)
        self.gxs_TBL.setAutoFillBackground(True)
        self.gxs_TBL.setObjectName(_fromUtf8("gxs_TBL"))
        self.gxs_TBL.setColumnCount(0)
        self.gxs_TBL.setRowCount(0)
        self.gxs_TBL.horizontalHeader().setCascadingSectionResizes(False)
        self.gxs_TBL.horizontalHeader().setStretchLastSection(True)
        self.gxs_TBL.horizontalHeader().setDefaultSectionSize(250)
	#self.gxs_TBL.setVisible(False)
	#self.gxs_TBL.resizeColumnsToContents()
	#self.gxs_TBL.setVisible(True)
	#self.gxs_TBL.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.imageView.addWidget(self.gxs_TBL)
        self.verticalLayout_6.addLayout(self.imageView)

        self.horizontalGroupBox1 = QtGui.QGroupBox(self.imageTab)
        self.horizontalGroupBox1.setObjectName(_fromUtf8("horizontalGroupBox1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalGroupBox1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(self.horizontalGroupBox1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)

        self.AutoChip = QtGui.QPushButton(self.horizontalGroupBox1)
        self.AutoChip.setObjectName(_fromUtf8("AutoChip"))
        self.horizontalLayout_4.addWidget(self.AutoChip)
        self.verticalLayout_6.addWidget(self.horizontalGroupBox1)
        self.tablesTabWidget.addTab(self.imageTab, _fromUtf8(""))
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
        self.cxs_TBL.horizontalHeader().setStretchLastSection(True)
        self.cxs_TBL.horizontalHeader().setDefaultSectionSize(250)
        self.chipView.addWidget(self.cxs_TBL)
        self.verticalLayout_7.addLayout(self.chipView)

        self.horizontalGroupBox2 = QtGui.QGroupBox(self.chipTab)
        self.horizontalGroupBox2.setObjectName(_fromUtf8("horizontalGroupBox2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalGroupBox2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))

        self.AutoQuery = QtGui.QPushButton(self.horizontalGroupBox2)
        self.AutoQuery.setObjectName(_fromUtf8("AutoQuery"))
        self.horizontalLayout_5.addWidget(self.AutoQuery)
        self.Cluster = QtGui.QPushButton(self.horizontalGroupBox2)
        self.Cluster.setObjectName(_fromUtf8("Cluster"))
        self.horizontalLayout_5.addWidget(self.Cluster)

        ''' Added by Tim Nguyen 1/28/18 '''
        self.ShowMatrices = QtGui.QPushButton(self.horizontalGroupBox2)
        self.ShowMatrices.setObjectName(_fromUtf8("Show Matrices"))
        self.horizontalLayout_5.addWidget(self.ShowMatrices)

        ''' Added by Tim Nguyen 2/12/18 '''
        self.SortToFolders = QtGui.QPushButton(self.horizontalGroupBox2)
        self.SortToFolders.setObjectName(_fromUtf8("Sort to Folders"))
        self.horizontalLayout_5.addWidget(self.SortToFolders)

        self.verticalLayout_7.addWidget(self.horizontalGroupBox2)
        self.tablesTabWidget.addTab(self.chipTab, _fromUtf8(""))
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
        self.nxs_TBL.horizontalHeader().setStretchLastSection(True)
        self.nxs_TBL.horizontalHeader().setDefaultSectionSize(150)

        self.nameView.addWidget(self.nxs_TBL)
        self.verticalLayout_8.addLayout(self.nameView)
        self.tablesTabWidget.addTab(self.nameTab, _fromUtf8(""))
        # Query Results Table
        '''
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_6)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.queryView = QtGui.QVBoxLayout()
        self.queryView.setObjectName(_fromUtf8("queryView"))
        self.res_TBL = QtGui.QTableWidget(self.tab_6)
        self.res_TBL.setObjectName(_fromUtf8("res_TBL"))
        self.res_TBL.setColumnCount(0)
        self.res_TBL.setRowCount(0)
        self.queryView.addWidget(self.res_TBL)
        self.verticalLayout_9.addLayout(self.queryView)
        self.tablesTabWidget.addTab(self.tab_6, _fromUtf8(""))
        '''
        self.verticalLayout_2.addWidget(self.tablesTabWidget)
        self.outputEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputEdit.sizePolicy().hasHeightForWidth())
        self.outputEdit.setSizePolicy(sizePolicy)
        self.outputEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        self.verticalLayout_2.addWidget(self.outputEdit)
        self.tablesTabWidget.raise_()
        self.outputEdit.raise_()
        self.horizontalGroupBox.raise_() #horizontalGroupBox
        mainSkel.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainSkel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 25))
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
        self.actionNew_Database.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNew_Database.setObjectName(_fromUtf8("actionNew_Database"))
        self.actionImport_Img_dir = QtGui.QAction(mainSkel)
        self.actionImport_Img_dir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionImport_Img_dir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionImport_Img_dir.setObjectName(_fromUtf8("actionImport_Img_dir")) #added this just so it'll compile
        self.actionOpen_Database = QtGui.QAction(mainSkel)
        self.actionOpen_Database.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen_Database.setObjectName(_fromUtf8("actionOpen_Database"))
        self.actionSave_Database = QtGui.QAction(mainSkel)
        self.actionSave_Database.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave_Database.setObjectName(_fromUtf8("actionSave_Database"))
        self.actionImport_Images_Select_file_s = QtGui.QAction(mainSkel)
        self.actionImport_Images_Select_file_s.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionImport_Images_Select_file_s.setObjectName(_fromUtf8("actionImport_Images_Select_file_s"))
        self.actionImport_Img_file = QtGui.QAction(mainSkel)
        self.actionImport_Img_file.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionImport_Img_file.setObjectName(_fromUtf8("actionImport_Img_file")) #also added this so itll compilex
        self.actionImport_Images_Select_Directory = QtGui.QAction(mainSkel)
        self.actionImport_Images_Select_Directory.setObjectName(_fromUtf8("actionImport_Images_Select_Directory"))
        self.actionQuit = QtGui.QAction(mainSkel)
        self.actionQuit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAdd_Chip = QtGui.QAction(mainSkel)
        self.actionAdd_Chip.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAdd_Chip.setObjectName(_fromUtf8("actionAdd_Chip"))
        self.actionNew_Chip_Property = QtGui.QAction(mainSkel)
        self.actionNew_Chip_Property.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNew_Chip_Property.setObjectName(_fromUtf8("actionNew_Chip_Property"))
        self.actionQuery = QtGui.QAction(mainSkel)
        self.actionQuery.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionQuery.setObjectName(_fromUtf8("actionQuery"))
        self.actionReselect_ROI = QtGui.QAction(mainSkel)
        self.actionReselect_ROI.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionReselect_ROI.setObjectName(_fromUtf8("actionReselect_ROI"))
        self.actionBatch_Change_Name = QtGui.QAction(mainSkel)
        self.actionBatch_Change_Name.setObjectName(_fromUtf8("actionBatch_Change_Name"))
        self.actionReselect_Ori = QtGui.QAction(mainSkel)
        self.actionReselect_Ori.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionReselect_Ori.setObjectName(_fromUtf8("actionReselect_Ori"))
        self.actionSelect_Next = QtGui.QAction(mainSkel) #was action.Select_Next
        self.actionSelect_Next.setObjectName(_fromUtf8("actionSelect_Next"))
        self.actionDelete_Chip = QtGui.QAction(mainSkel)
        self.actionDelete_Chip.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete_Chip.setObjectName(_fromUtf8("actionDelete_Chip"))
        self.actionDelete_Image = QtGui.QAction(mainSkel)
        self.actionDelete_Image.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete_Image.setObjectName(_fromUtf8("actionDelete_Image"))
        self.actionPrecompute_Chips_Features = QtGui.QAction(mainSkel)
        self.actionPrecompute_Chips_Features.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionPrecompute_Chips_Features.setObjectName(_fromUtf8("actionPrecompute_Chips_Features"))
        self.actionPrecomputeChipsFeatures = QtGui.QAction(mainSkel)
        self.actionPrecomputeChipsFeatures.setObjectName(_fromUtf8("actionPrecomputeChipsFeatures")) #please compile
        self.actionPrecompute_Queries = QtGui.QAction(mainSkel)
        self.actionPrecompute_Queries.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionPrecompute_Queries.setObjectName(_fromUtf8("actionPrecompute_Queries"))
        self.actionScale_all_ROIS = QtGui.QAction(mainSkel)
        self.actionScale_all_ROIS.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionScale_all_ROIS.setObjectName(_fromUtf8("actionScale_all_ROIS"))
        self.actionConvert_all_images_into_chips = QtGui.QAction(mainSkel)
        self.actionConvert_all_images_into_chips.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionConvert_all_images_into_chips.setObjectName(_fromUtf8("actionConvert_all_images_into_chips"))
        self.actionLayout_Figures = QtGui.QAction(mainSkel)
        self.actionLayout_Figures.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionLayout_Figures.setObjectName(_fromUtf8("actionLayout_Figures"))
        self.actionAbout = QtGui.QAction(mainSkel)
        self.actionAbout.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionView_Docs = QtGui.QAction(mainSkel) #actionView_Documentation
        self.actionView_Docs.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_Docs.setObjectName(_fromUtf8("actionView_Docs"))
        self.actionView_DBDir = QtGui.QAction(mainSkel) #was actionView_Database_Dir
        self.actionView_DBDir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_DBDir.setObjectName(_fromUtf8("actionView_DBDir"))
        self.actionView_Computed_Dir = QtGui.QAction(mainSkel)
        self.actionView_Computed_Dir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_Computed_Dir.setObjectName(_fromUtf8("actionView_Computed_Dir"))
        self.actionView_Global_Dir = QtGui.QAction(mainSkel)
        self.actionView_Global_Dir.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionView_Global_Dir.setObjectName(_fromUtf8("actionView_Global_Dir"))
        self.actionWriteLogs = QtGui.QAction(mainSkel)
        self.actionWriteLogs.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionWriteLogs.setObjectName(_fromUtf8("actionWriteLogs"))
        self.actionDelete_Precomputed_Results = QtGui.QAction(mainSkel) #actionDelete_Cached_Query_Results
        self.actionDelete_Precomputed_Results.setObjectName(_fromUtf8("actionDelete_Precomputed_Results"))
        self.actionDelete_computed_directory = QtGui.QAction(mainSkel) #actionDelete_Computed_Directory
        self.actionDelete_computed_directory.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete_computed_directory.setObjectName(_fromUtf8("actionDelete_computed_directory"))
        self.actionDelete_global_preferences = QtGui.QAction(mainSkel) #actionDelete_Global_Preferences
        self.actionDelete_global_preferences.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete_global_preferences.setObjectName(_fromUtf8("actionDelete_global_preferences"))
        self.actionDev_Mode_IPython = QtGui.QAction(mainSkel) #actionDev_Mode_IPython
        self.actionDev_Mode_IPython.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDev_Mode_IPython.setObjectName(_fromUtf8("actionDev_Mode_IPython"))
        self.actionDeveloper_Reload = QtGui.QAction(mainSkel)
        self.actionDeveloper_Reload.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDeveloper_Reload.setObjectName(_fromUtf8("actionDeveloper_Reload"))
        self.actionNext = QtGui.QAction(mainSkel)
        self.actionNext.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNext.setObjectName(_fromUtf8("actionNext")) #so it'll compile
        self.actionPreferences = QtGui.QAction(mainSkel)
        self.actionPreferences.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.menuFile.addAction(self.actionNew_Database)
        self.menuFile.addAction(self.actionOpen_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Database)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_Img_file)
        self.menuFile.addAction(self.actionImport_Img_dir)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuActions.addAction(self.actionAdd_Chip)
        self.menuActions.addAction(self.actionNew_Chip_Property)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionQuery)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionReselect_ROI)
        self.menuActions.addAction(self.actionReselect_Ori)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionNext)
        self.menuActions.addAction(self.actionSelect_Next)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionDelete_Chip)
        self.menuActions.addAction(self.actionDelete_Image)
        self.menuBatch.addAction(self.actionPrecompute_Chips_Features)
        self.menuBatch.addAction(self.actionPrecomputeChipsFeatures) #please compile
        self.menuBatch.addAction(self.actionPrecompute_Queries)
        self.menuBatch.addSeparator()
        self.menuBatch.addAction(self.actionScale_all_ROIS)
        self.menuBatch.addSeparator()
        self.menuBatch.addAction(self.actionConvert_all_images_into_chips)
        self.menuOptions.addAction(self.actionLayout_Figures)
        self.menuOptions.addAction(self.actionPreferences) #added
        self.menuOptions.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionView_Docs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionView_DBDir) #action_View_Database_Dir
        self.menuHelp.addAction(self.actionView_Computed_Dir)
        self.menuHelp.addAction(self.actionView_Global_Dir)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionWriteLogs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDelete_Precomputed_Results)
        self.menuHelp.addAction(self.actionDelete_computed_directory)
        self.menuHelp.addAction(self.actionDelete_global_preferences)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDev_Mode_IPython)
        self.menuHelp.addAction(self.actionDeveloper_Reload)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuBatch.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainSkel)
        self.tablesTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainSkel)

    def retranslateUi(self, mainSkel):
        mainSkel.setWindowTitle(_translate("mainSkel", "HotSpotter", None))
        self.pushButton.setText(_translate("mainSkel", "Import Image(s)", None))
        self.AutoChip.setText(_translate("mainSkel", "AutoChip", None))
        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.imageTab), _translate("mainSkel", "Image Table", None))
        self.AutoQuery.setText(_translate("mainSkel", "AutoQuery", None))
        self.Cluster.setText(_translate("mainSkel", "Cluster", None))
        self.ShowMatrices.setText(_translate("mainSkel", "Show Matrices", None)) # added by TN 1/28/18
        self.SortToFolders.setText(_translate("mainSkel", "Sort to Folders", None)) # added by TN 2/12/18

        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.chipTab), _translate("mainSkel", "Chip Table", None))
        self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.nameTab), _translate("mainSkel", "Name View", None))
        # Deleted to hide Query Results Table (unused by 17.7)
        #self.tablesTabWidget.setTabText(self.tablesTabWidget.indexOf(self.tab_6), _translate("mainSkel", "Query Results Table", None))
        self.menuFile.setTitle(_translate("mainSkel", "File", None))
        self.menuActions.setTitle(_translate("mainSkel", "Actions", None))
        self.menuBatch.setTitle(_translate("mainSkel", "Batch", None))
        self.menuOptions.setTitle(_translate("mainSkel", "Options", None))
        self.menuHelp.setTitle(_translate("mainSkel", "Help", None))
        self.actionNew_Database.setText(_translate("mainSkel", "New Database", None))
        self.actionNew_Database.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Database.setText(_translate("mainSkel", "Open Database", None))
        self.actionOpen_Database.setToolTip(QtGui.QApplication.translate("mainSkel", "Opens a different database directory.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Database.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Database.setText(_translate("mainSkel", "Save Database", None))
        self.actionSave_Database.setIconText(QtGui.QApplication.translate("mainSkel", "Save Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Database.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Img_file.setText(_translate("mainSkel", "Import Images (Select file(s))", None))
        self.actionImport_Img_file.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Img_dir.setText(_translate("mainSkel", "Import Images (Select Directory)", None))

        self.actionQuit.setText(_translate("mainSkel", "Quit", None))
        self.actionAdd_Chip.setText(_translate("mainSkel", "Add Chip", None))
        self.actionAdd_Chip.setShortcut(QtGui.QApplication.translate("mainSkel", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Chip_Property.setText(_translate("mainSkel", "New Chip Property", None))
        self.actionQuery.setText(_translate("mainSkel", "Query", None))
        self.actionQuery.setShortcut(QtGui.QApplication.translate("mainSkel", "Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReselect_ROI.setText(_translate("mainSkel", "Reselect ROI", None))
        self.actionReselect_ROI.setShortcut(QtGui.QApplication.translate("mainSkel", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBatch_Change_Name.setText(QtGui.QApplication.translate("mainSkel", "Batch Change Name", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReselect_Ori.setText(_translate("mainSkel", "Reselect Orientation", None))
        self.actionReselect_Ori.setShortcut(QtGui.QApplication.translate("mainSkel", "O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Next.setText(_translate("mainSkel", "Select Next", None))
        self.actionSelect_Next.setShortcut(QtGui.QApplication.translate("mainSkel", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Chip.setText(_translate("mainSkel", "Delete Chip", None))
        self.actionDelete_Chip.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Image.setText(_translate("mainSkel", "Delete Image", None))

        self.actionPrecompute_Chips_Features.setText(_translate("mainSkel", "Precompute Chips/Features", None))
        self.actionPrecomputeChipsFeatures.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+Return", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrecompute_Queries.setText(_translate("mainSkel", "Precompute Queries", None))
        self.actionScale_all_ROIS.setText(_translate("mainSkel", "Scale All ROIs", None))
        self.actionConvert_all_images_into_chips.setText(_translate("mainSkel", "Convert All Images into Chips", None))
        self.actionLayout_Figures.setText(_translate("mainSkel", "Layout Figures", None))
        self.actionLayout_Figures.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(_translate("mainSkel", "About", None))
        self.actionView_Docs.setText(_translate("mainSkel", "View Documentation", None))
        self.actionView_DBDir.setText(_translate("mainSkel", "View Database Dir", None)) #actionView_Database_Dir
        self.actionView_Computed_Dir.setText(_translate("mainSkel", "View Computed Dir", None))
        self.actionView_Global_Dir.setText(_translate("mainSkel", "View Global Dir", None))
        self.actionWriteLogs.setText(_translate("mainSkel", "Write Logs", None))
        self.actionDelete_Precomputed_Results.setText(_translate("mainSkel", "Delete Cached Query Results", None))
        self.actionDelete_computed_directory.setText(_translate("mainSkel", "Delete Computed Directory", None))
        self.actionDelete_global_preferences.setText(_translate("mainSkel", "Delete Global Preferences", None))
        self.actionDev_Mode_IPython.setText(_translate("mainSkel", "Developer Mode (IPython)", None))
        self.actionDev_Mode_IPython.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+Alt+Shift+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeveloper_Reload.setText(_translate("mainSkel", "Developer Reload", None))
        self.actionDeveloper_Reload.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("mainSkel", "Edit Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setToolTip(QtGui.QApplication.translate("mainSkel", "Changes algorithm parameters and program behavior.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("mainSkel", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))

import resources_MainSkel_rc
