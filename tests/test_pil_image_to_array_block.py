from unittest.mock import MagicMock, patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_image_to_array_block import PILImageToArray


class TestPILImageToArray(NIOBlockTestCase):

    @patch(PILImageToArray.__module__ + '.np')
    def test_notified_signals(self, mock_numpy):
        mock_array = mock_numpy.array.return_value = MagicMock()
        mock_image = MagicMock()
        blk = PILImageToArray()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': mock_image})])
        blk.stop()
        mock_numpy.array.assert_called_once_with(mock_image)
        self.assertEqual(self.last_notified[DEFAULT_TERMINAL][0].image,
                         mock_array)
        self.assert_num_signals_notified(1)
