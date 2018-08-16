from unittest.mock import MagicMock, patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_base64_decode_block import PILBase64Decode


class TestPILBase64Decode(NIOBlockTestCase):

    @patch(PILBase64Decode.__module__ + '.b64decode')
    @patch(PILBase64Decode.__module__ + '.Image')
    @patch(PILBase64Decode.__module__ + '.BytesIO')
    def test_notified_signals(self, mock_buffer, mock_Image, mock_b64decode):
        image_string = 'base64stringgoeshere'
        mock_bytes = mock_b64decode.return_value = MagicMock()
        mock_buffer_obj = mock_buffer.return_value = MagicMock()
        mock_image_obj = mock_Image.open.return_value = MagicMock()
        blk = PILBase64Decode()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': image_string})])
        blk.stop()
        mock_b64decode.assert_called_once_with(image_string)
        mock_buffer.assert_called_once_with(mock_bytes)
        mock_Image.open.assert_called_once_with(mock_buffer_obj)
        self.assertEqual(self.last_notified[DEFAULT_TERMINAL][0].image,
                         mock_image_obj)
