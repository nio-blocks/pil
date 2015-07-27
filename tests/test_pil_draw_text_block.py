from PIL import Image
from collections import defaultdict
from nio.common.signal.base import Signal
from nio.util.support.block_test_case import NIOBlockTestCase
from ..pil_draw_text_block import PILDrawText


class TestPILDrawText(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    def test_notified_signals(self):
        blk = PILDrawText()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': Image.new('1', (64, 48))})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'],
                         list(self.last_notified['default'][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified['default'][0].image))
        self.assertEqual((64, 48),
                         self.last_notified['default'][0].image.size)
        # TODO: figure out how to mock ImageDraw and check that it's called
        # TODO: figure out how to inspect that PIL Image was drawn to

    def test_signal_without_image_attr(self):
        ''' Signal passes through the block unmodified '''
        blk = PILDrawText()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual([],
                         list(self.last_notified['default'][0].to_dict().keys()))

    def test_signal_without_image_object(self):
        ''' Signal passes through the block unmodified '''
        blk = PILDrawText()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': 'not an Image object'})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'],
                         list(self.last_notified['default'][0].to_dict().keys()))
        self.assertEqual('not an Image object',
                         self.last_notified['default'][0].image)
