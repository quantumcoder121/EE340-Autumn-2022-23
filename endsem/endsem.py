#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: endsem
# Author: oem
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
import pmt
from gnuradio import digital
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



from gnuradio import qtgui

class endsem(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "endsem", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("endsem")
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

        self.settings = Qt.QSettings("GNU Radio", "endsem")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=441,
                decimation=20000,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=50,
                taps=[1],
                fractional_bw=0)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                2000000,
                500000,
                50000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                2000000,
                500000,
                50000,
                window.WIN_HAMMING,
                6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_fff(4, 0.062831853, firdes.root_raised_cosine(32, 1280000, 10000, 0.4, 1408), 32, 16, 1.5, 1)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0, 0, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 18)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(-1)
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_ff(-0.5)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_ff(-0.5)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(-0.5)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(-0.5)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, 'rx.dat', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'received.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0_0_0 = blocks.delay(gr.sizeof_float*1, 200)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, 200)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 200)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 200)
        self.blocks_add_xx_0_0_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(2000000, analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(2000000, analog.GR_SIN_WAVE, 500000, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_add_xx_0_0_0, 1))
        self.connect((self.blocks_add_xx_0_0_0, 0), (self.blocks_add_xx_0_0_0_0, 1))
        self.connect((self.blocks_add_xx_0_0_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0_0_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_add_xx_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.blocks_add_xx_0_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_delay_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "endsem")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()




def main(top_block_cls=endsem, options=None):

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
