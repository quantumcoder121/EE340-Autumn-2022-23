#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: lab1c
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class lab1c(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "lab1c", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("lab1c")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "lab1c")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.range4 = range4 = 0.5
        self.range3 = range3 = 0.5
        self.range2 = range2 = 0.5
        self.range1 = range1 = 0.5
        self.range0 = range0 = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._range4_range = Range(0.1, 1, 0.01, 0.5, 200)
        self._range4_win = RangeWidget(self._range4_range, self.set_range4, "r4", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._range4_win)
        self._range3_range = Range(0.1, 1, 0.01, 0.5, 200)
        self._range3_win = RangeWidget(self._range3_range, self.set_range3, "r3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._range3_win)
        self._range2_range = Range(0.1, 1, 0.01, 0.5, 200)
        self._range2_win = RangeWidget(self._range2_range, self.set_range2, "r2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._range2_win)
        self._range1_range = Range(0.1, 1, 0.01, 0.5, 200)
        self._range1_win = RangeWidget(self._range1_range, self.set_range1, "r1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._range1_win)
        self._range0_range = Range(0.1, 1, 0.01, 0.5, 200)
        self._range0_win = RangeWidget(self._range0_range, self.set_range0, "r0", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._range0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('Bach.wav', True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_3 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                range3,
                samp_rate,
                6000,
                9000,
                1,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_2 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                range1,
                samp_rate,
                500,
                3000,
                1,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_1 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                range2,
                samp_rate,
                3000,
                6000,
                1,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                range4,
                samp_rate,
                9000,
                15000,
                1,
                window.WIN_RECTANGULAR,
                6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                range0,
                samp_rate,
                20,
                500,
                1,
                window.WIN_RECTANGULAR,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0_3, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_2, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab1c")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.range0, self.samp_rate, 20, 500, 1, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.range4, self.samp_rate, 9000, 15000, 1, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.range2, self.samp_rate, 3000, 6000, 1, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.range1, self.samp_rate, 500, 3000, 1, window.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.range3, self.samp_rate, 6000, 9000, 1, window.WIN_RECTANGULAR, 6.76))

    def get_range4(self):
        return self.range4

    def set_range4(self, range4):
        self.range4 = range4
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.range4, self.samp_rate, 9000, 15000, 1, window.WIN_RECTANGULAR, 6.76))

    def get_range3(self):
        return self.range3

    def set_range3(self, range3):
        self.range3 = range3
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.range3, self.samp_rate, 6000, 9000, 1, window.WIN_RECTANGULAR, 6.76))

    def get_range2(self):
        return self.range2

    def set_range2(self, range2):
        self.range2 = range2
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.range2, self.samp_rate, 3000, 6000, 1, window.WIN_RECTANGULAR, 6.76))

    def get_range1(self):
        return self.range1

    def set_range1(self, range1):
        self.range1 = range1
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.range1, self.samp_rate, 500, 3000, 1, window.WIN_RECTANGULAR, 6.76))

    def get_range0(self):
        return self.range0

    def set_range0(self, range0):
        self.range0 = range0
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.range0, self.samp_rate, 20, 500, 1, window.WIN_RECTANGULAR, 6.76))




def main(top_block_cls=lab1c, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
