from PIL import Image
from collections import defaultdict
from nio.common.signal.base import Signal
from nio.util.support.block_test_case import NIOBlockTestCase
from ..pil_new_image_block import PILNewImage


class TestPILNewImage(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    def test_defaults(self):
        blk = PILNewImage()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'],
                         list(self.last_notified['default'][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified['default'][0].image))
        self.assertEqual((64, 48),
                         self.last_notified['default'][0].image.size)

    def test_size_prop(self):
        blk = PILNewImage()
        self.configure_block(blk, {'size': {'x': 1}})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'],
                         list(self.last_notified['default'][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified['default'][0].image))
        self.assertEqual((1, 48),
                         self.last_notified['default'][0].image.size)

    def test_invalid_size_prop(self):
        blk = PILNewImage()
        self.configure_block(blk, {'size': {'x': None}})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertTrue(
            'image' not in self.last_notified['default'][0].to_dict())
