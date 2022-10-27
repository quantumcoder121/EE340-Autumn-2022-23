#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: lab108
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

from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb



from gnuradio import qtgui

class lab108(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "lab108", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("lab108")
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

        self.settings = Qt.QSettings("GNU Radio", "lab108")

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
        self.sps = sps = 4
        self.sample_rate = sample_rate = 320000
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            sps,
            taps=firdes.root_raised_cosine(1, sample_rate, sample_rate/sps, alpha, 11*sps),
            flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 0.062831853, firdes.root_raised_cosine(100, 32*sample_rate, sample_rate/sps, alpha, 11*sps), 32, 16, 1.5, 1)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((-0.5, 0.5), 1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0, 0, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 18)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'message.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'received_diff_bpsk.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lab108")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

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
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(100, 32*self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(1, self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(100, 32*self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(1, self.sample_rate, self.sample_rate/self.sps, self.alpha, 11*self.sps))




def main(top_block_cls=lab108, options=None):

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
