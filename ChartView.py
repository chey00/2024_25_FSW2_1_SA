from PyQt6.QtCharts import QChartView, QChart, QDateTimeAxis, QValueAxis, QSplineSeries
from PyQt6.QtCore import Qt, QDateTime, pyqtSlot


class ChartView(QChartView):
    def __init__(self, parent=None):
        super(ChartView, self).__init__(parent)
