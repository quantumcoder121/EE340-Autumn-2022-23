#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: lab106
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
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb



from gnuradio import qtgui

class lab106(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "lab106", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("lab106")
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

        self.settings = Qt.QSettings("GNU Radio", "lab106")

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
        self.udp_port = udp_port = 4091
        self.sps = sps = 4
        self.sample_rate = sample_rate = 320000
        self.f_off = f_off = 5000
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            sample_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            sps,
            taps=firdes.root_raised_cosine(1, sample_rate, sample_rate/sps, alpha, 11*sps),
            flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.iir_filter_xxx_0_0 = filter.iir_filter_ffd([1.0001, -1], [-1, 1], True)
        self.iir_filter_xxx_0 = filter.iir_filter_ffd([0.01], [-1, 0.99], True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 0.062831853, firdes.root_raised_cosine(100, 32*sample_rate, sample_rate/sps, alpha, 11*sps), 32, 16, 1.5, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((1.4142, 1+1j, 1.4142j, -1+1j, -1.4142, -1-1j, -1.4142j, 1-1j), 1)
        self.blocks_vco_c_0 = blocks.vco_c(sample_rate, -320000, 1)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_float*1, '127.0.0.1', udp_port, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_float*1, '127.0.0.1', udp_port, 1472, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, sample_rate,True)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.125)
        self.blocks_exponentiate_const_cci_0 = blocks.exponentiate_const_cci(8, 1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 10)
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(sample_rate, analog.GR_SIN_WAVE, f_off, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 8, 1000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_exponentiate_const_cci_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_exponentiate_const_cci_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.iir_filter_xxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_exponentiate_const_cci_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.iir_filter_xxx_0_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab106")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_udp_port(self):
        return self.udp_port

    def set_udp_port(self, udp_port):
        self.udp_port = udp_port

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(100, 32*self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(1, self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.sample_rate)
        self.blocks_throttle_0.set_sample_rate(self.sample_rate)
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(100, 32*self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(1, self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))
        self.qtgui_sink_x_0.set_frequency_range(0, self.sample_rate)

    def get_f_off(self):
        return self.f_off

    def set_f_off(self, f_off):
        self.f_off = f_off
        self.analog_sig_source_x_0.set_frequency(self.f_off)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(100, 32*self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(1, self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))




def main(top_block_cls=lab106, options=None):

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
