from PIL import Image

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_new_image_block import PILNewImage


class TestPILNewImage(NIOBlockTestCase):

    def test_defaults(self):
        """Create an image of default size 64x48"""
        blk = PILNewImage()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(
            ['image'],
            list(self.last_notified[DEFAULT_TERMINAL][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified[DEFAULT_TERMINAL][0].image))
        self.assertEqual((64, 48),
                         self.last_notified[DEFAULT_TERMINAL][0].image.size)
        self.assertEqual('RGB',
                         self.last_notified[DEFAULT_TERMINAL][0].image.mode)

    def test_size_prop(self):
        """Create a black and white image of configured size 1x48"""
        blk = PILNewImage()
        self.configure_block(blk, {'size': {'x': 1}, 'mode': 'BW'})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(
            ['image'],
            list(self.last_notified[DEFAULT_TERMINAL][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified[DEFAULT_TERMINAL][0].image))
        self.assertEqual((1, 48),
                         self.last_notified[DEFAULT_TERMINAL][0].image.size)
        self.assertEqual('L',
                         self.last_notified[DEFAULT_TERMINAL][0].image.mode)
