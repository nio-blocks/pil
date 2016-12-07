from PIL import Image
from collections import defaultdict
import inspect
from os.path import join, dirname
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..pil_open_file_block import PILOpenFile


class TestPILOpenFile(NIOBlockTestCase):

    def test_notified_signals(self):
        blk = PILOpenFile()
        # Get the niologo.png file from the block directory
        file = join(dirname(inspect.getfile(PILOpenFile)), blk.file().value)
        self.configure_block(blk, {"file": file})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'], list(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified[DEFAULT_TERMINAL][0].image))
        self.assertEqual((64, 48),
                         self.last_notified[DEFAULT_TERMINAL][0].image.size)
