from unittest.mock import MagicMock, patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_base64_decode_block import PILBase64Decode


class TestPILBase64Decode(NIOBlockTestCase):

    @patch(PILBase64Decode.__module__ + '.b64decode')
    def test_notified_signals(self, mock_b64decode):
        mock_image = MagicMock()
        mock_b64decode.return_value = 'foo'
        blk = PILBase64Decode()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': mock_image})])
        blk.stop()
        self.assertEqual(self.last_notified[DEFAULT_TERMINAL][0].image, 'foo')
