#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: lab83
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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class lab83(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "lab83", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("lab83")
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

        self.settings = Qt.QSettings("GNU Radio", "lab83")

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
        self.sym_rate = sym_rate = 32000
        self.sps = sps = 8
        self.amp = amp = 0
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################
        self._sym_rate_range = Range(1600, 160000, 1, 32000, 200)
        self._sym_rate_win = RangeWidget(self._sym_rate_range, self.set_sym_rate, "sym_rate", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._sym_rate_win)
        self._sps_range = Range(0, 16, 1, 8, 200)
        self._sps_win = RangeWidget(self._sps_range, self.set_sps, "sps", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._sps_win)
        self._amp_range = Range(0, 1, 0.001, 0, 200)
        self._amp_win = RangeWidget(self._amp_range, self.set_amp, "amp", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amp_win)
        self._alpha_range = Range(0, 1, 0.001, 1, 200)
        self._alpha_win = RangeWidget(self._alpha_range, self.set_alpha, "alpha", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                1,
                sym_rate*sps,
                sym_rate,
                alpha,
                11*sps))
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                1,
                sym_rate*sps,
                sym_rate,
                alpha,
                11*sps))
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=16,
                decimation=125,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=125,
                decimation=16,
                taps=[],
                fractional_bw=0)
        self.qtgui_sink_x_0_0_1_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            2000000, #bw
            'Demodulated', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_0_win)
        self.qtgui_sink_x_0_0_1 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            2000000, #bw
            'Demodulated', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_0_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_1.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_1_win)
        self.qtgui_sink_x_0_0_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            2000000, #bw
            'bits', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_0_0_win)
        self.qtgui_sink_x_0_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            2000000, #bw
            'Filtered and Thresholded', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_0_win)
        self.qtgui_sink_x_0_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            2000000, #bw
            'Input to Receiver', #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                2000000,
                100000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(sps, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((-0.5, 0.5), 1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0_0_1_0 = blocks.throttle(gr.sizeof_float*1, 2000000,True)
        self.blocks_throttle_0_0_1 = blocks.throttle(gr.sizeof_float*1, 2000000,True)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, 2000000,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_float*1, 2000000,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, 2000000,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0, 0, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 19)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'message.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'received.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(2000000, analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(2000000, analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.qtgui_sink_x_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_1, 0), (self.qtgui_sink_x_0_0_1, 0))
        self.connect((self.blocks_throttle_0_0_1_0, 0), (self.qtgui_sink_x_0_0_1_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0_0_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_throttle_0_0_1_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab83")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.sym_rate*self.sps, self.sym_rate, self.alpha, 11*self.sps))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.sym_rate*self.sps, self.sym_rate, self.alpha, 11*self.sps))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.sym_rate*self.sps, self.sym_rate, self.alpha, 11*self.sps))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.sym_rate*self.sps, self.sym_rate, self.alpha, 11*self.sps))

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp
        self.analog_noise_source_x_0.set_amplitude(self.amp)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.sym_rate*self.sps, self.sym_rate, self.alpha, 11*self.sps))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.sym_rate*self.sps, self.sym_rate, self.alpha, 11*self.sps))




def main(top_block_cls=lab83, options=None):

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
