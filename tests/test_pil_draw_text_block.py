from PIL import Image
from PIL import ImageFont
from collections import defaultdict
from unittest.mock import MagicMock, patch
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..pil_draw_text_block import PILDrawText


class TestPILDrawText(NIOBlockTestCase):

    @patch(PILDrawText.__module__ + '.ImageDraw.Draw')
    def test_notified_signals(self, mock_draw):
        mock_draw_obj = MagicMock()
        mock_draw.return_value = mock_draw_obj
        blk = PILDrawText()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': Image.new('1', (64, 48))})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'], list(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict().keys()))
        self.assertEqual(Image.Image,
                         type(self.last_notified[DEFAULT_TERMINAL][0].image))
        self.assertEqual((64, 48),
                         self.last_notified[DEFAULT_TERMINAL][0].image.size)
        # Check that the Draw object was created
        self.assertEqual(1, mock_draw.call_count)
        self.assertTrue(isinstance(mock_draw.call_args[0][0], Image.Image))
        # Check that text was written to the Draw object
        self.assertEqual(1, mock_draw_obj.text.call_count)
        self.assertEqual(((0, 0), 'Hello, n.io!'),
                         mock_draw_obj.text.call_args[0])
        self.assertTrue(isinstance(mock_draw_obj.text.call_args[1]['font'],
                                   ImageFont.ImageFont))
        self.assertEqual(mock_draw_obj.text.call_args[1]['fill'], 255)

    @patch(PILDrawText.__module__ + '.ImageDraw.Draw')
    def test_invalid_text(self, mock_draw):
        ''' Test that text is converted to string before drawing it '''
        mock_draw_obj = MagicMock()
        mock_draw.return_value = mock_draw_obj
        blk = PILDrawText()
        self.configure_block(blk, {"text": "{{ 42 }}"})
        blk.start()
        blk.process_signals([Signal({'image': Image.new('1', (64, 48))})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(((0, 0), '42'),
                         mock_draw_obj.text.call_args[0])

    @patch(PILDrawText.__module__ + '.ImageDraw.Draw')
    def test_signal_without_image_attr(self, mock_draw):
        ''' Signal passes through the block unmodified '''
        blk = PILDrawText()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual([], list(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict().keys()))
        self.assertEqual(0, mock_draw.call_count)

    @patch(PILDrawText.__module__ + '.ImageDraw.Draw')
    def test_signal_without_image_object(self, mock_draw):
        ''' Signal passes through the block unmodified '''
        blk = PILDrawText()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': 'not an Image object'})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertEqual(['image'], list(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict().keys()))
        self.assertEqual('not an Image object',
                         self.last_notified[DEFAULT_TERMINAL][0].image)
        self.assertEqual(0, mock_draw.call_count)
