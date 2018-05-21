from PIL import Image
import inspect
from os.path import join, dirname

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_resize_image_block import PILResizeImage


class TestPILResizeImage(NIOBlockTestCase):

    def test_notified_signals(self):
        blk = PILResizeImage()
        # Get the niologo.png file from the block directory
        file = join(dirname(inspect.getfile(PILResizeImage)), 'niologo.png')
        test_image = Image.open(file)
        self.configure_block(blk, {'x': 32, 'y': 24})
        blk.start()
        blk.process_signals([Signal({'image': test_image})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'], list(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified[DEFAULT_TERMINAL][0].image))
        self.assertEqual((32, 24), 
                         self.last_notified[DEFAULT_TERMINAL][0].image.size)
