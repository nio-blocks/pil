from unittest.mock import MagicMock

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_save_image_block import PILSaveImage


class TestPILSaveImage(NIOBlockTestCase):

    def test_notified_signals(self):
        mock_image = MagicMock()
        file_name = 'foo.jpg'
        blk = PILSaveImage()
        self.configure_block(blk, {'file': file_name})
        blk.start()
        blk.process_signals([Signal({'image': mock_image})])
        blk.stop()
        mock_image.save.assert_called_once_with(file_name)
