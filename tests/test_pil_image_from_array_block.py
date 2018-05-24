from unittest.mock import MagicMock, patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_image_from_array_block import PILImageFromArray


class TestPILImageFromArray(NIOBlockTestCase):

    @patch(PILImageFromArray.__module__ + '.Image')
    def test_notified_signals(self, mock_Image):
        mock_image_obj = mock_Image.fromarray.return_value = MagicMock()
        mock_array = MagicMock()
        blk = PILImageFromArray()
        self.configure_block(blk, {'input_array': '{{ $foo }}'})
        blk.start()
        blk.process_signals([Signal({'foo': mock_array})])
        blk.stop()
        mock_Image.fromarray.assert_called_once_with(mock_array)
        self.assertEqual(self.last_notified[DEFAULT_TERMINAL][0].image,
                         mock_image_obj)
        self.assert_num_signals_notified(1)
