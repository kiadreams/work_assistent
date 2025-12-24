# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_services_report_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_ServiceReportsWidget(object):
    def setupUi(self, ServiceReportsWidget):
        if not ServiceReportsWidget.objectName():
            ServiceReportsWidget.setObjectName("ServiceReportsWidget")
        ServiceReportsWidget.resize(1058, 660)
        self.verticalLayout_4 = QVBoxLayout(ServiceReportsWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sirvice_list_title = QLabel(ServiceReportsWidget)
        self.label_sirvice_list_title.setObjectName("label_sirvice_list_title")

        self.verticalLayout.addWidget(self.label_sirvice_list_title)

        self.comboBox_service_list = QComboBox(ServiceReportsWidget)
        self.comboBox_service_list.setObjectName("comboBox_service_list")

        self.verticalLayout.addWidget(self.comboBox_service_list)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_edit_service = QPushButton(ServiceReportsWidget)
        self.pushButton_edit_service.setObjectName("pushButton_edit_service")

        self.horizontalLayout.addWidget(self.pushButton_edit_service)

        self.pushButton_add_service = QPushButton(ServiceReportsWidget)
        self.pushButton_add_service.setObjectName("pushButton_add_service")

        self.horizontalLayout.addWidget(self.pushButton_add_service)

        self.pushButton_remove_service = QPushButton(ServiceReportsWidget)
        self.pushButton_remove_service.setObjectName("pushButton_remove_service")

        self.horizontalLayout.addWidget(self.pushButton_remove_service)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_show_all_services = QPushButton(ServiceReportsWidget)
        self.pushButton_show_all_services.setObjectName("pushButton_show_all_services")

        self.verticalLayout.addWidget(self.pushButton_show_all_services)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_group_list_title = QLabel(ServiceReportsWidget)
        self.label_group_list_title.setObjectName("label_group_list_title")

        self.verticalLayout_2.addWidget(self.label_group_list_title)

        self.comboBox_group_list = QComboBox(ServiceReportsWidget)
        self.comboBox_group_list.setObjectName("comboBox_group_list")

        self.verticalLayout_2.addWidget(self.comboBox_group_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_edit_group = QPushButton(ServiceReportsWidget)
        self.pushButton_edit_group.setObjectName("pushButton_edit_group")

        self.horizontalLayout_2.addWidget(self.pushButton_edit_group)

        self.pushButton_add_group = QPushButton(ServiceReportsWidget)
        self.pushButton_add_group.setObjectName("pushButton_add_group")

        self.horizontalLayout_2.addWidget(self.pushButton_add_group)

        self.pushButton_remove_group = QPushButton(ServiceReportsWidget)
        self.pushButton_remove_group.setObjectName("pushButton_remove_group")

        self.horizontalLayout_2.addWidget(self.pushButton_remove_group)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pushButton_show_all_groups = QPushButton(ServiceReportsWidget)
        self.pushButton_show_all_groups.setObjectName("pushButton_show_all_groups")

        self.verticalLayout_2.addWidget(self.pushButton_show_all_groups)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableWidget_service_data_table = QTableWidget(ServiceReportsWidget)
        self.tableWidget_service_data_table.setObjectName("tableWidget_service_data_table")

        self.verticalLayout_3.addWidget(self.tableWidget_service_data_table)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(ServiceReportsWidget)

        QMetaObject.connectSlotsByName(ServiceReportsWidget)

    # setupUi

    def retranslateUi(self, ServiceReportsWidget):
        ServiceReportsWidget.setWindowTitle(
            QCoreApplication.translate("ServiceReportsWidget", "Form", None)
        )
        self.label_sirvice_list_title.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043b\u0443\u0436\u0431\u044b",
                None,
            )
        )
        self.pushButton_edit_service.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                " \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443",
                None,
            )
        )
        self.pushButton_add_service.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443",
                None,
            )
        )
        self.pushButton_remove_service.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043b\u0443\u0436\u0431\u0443",
                None,
            )
        )
        self.pushButton_show_all_services.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432\u0441\u0435\u0445 \u0441\u043b\u0443\u0436\u0431",
                None,
            )
        )
        self.label_group_list_title.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u0440\u0443\u043f\u043f\u044b",
                None,
            )
        )
        self.pushButton_edit_group.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                " \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                None,
            )
        )
        self.pushButton_add_group.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                None,
            )
        )
        self.pushButton_remove_group.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u0443",
                None,
            )
        )
        self.pushButton_show_all_groups.setText(
            QCoreApplication.translate(
                "ServiceReportsWidget",
                "\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0443\u043f\u043f\u044b \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u0441\u043b\u0443\u0436\u0431\u044b",
                None,
            )
        )

    # retranslateUi
