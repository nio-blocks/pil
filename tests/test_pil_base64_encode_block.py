from unittest.mock import MagicMock, patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_base64_encode_block import PILBase64Encode


class TestPILBase64Encode(NIOBlockTestCase):

    @patch(PILBase64Encode.__module__ + '.b64encode')
    def test_notified_signals(self, mock_b64encode):
        mock_image = MagicMock()
        mock_b64encode.return_value = 'foo'
        blk = PILBase64Encode()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'image': mock_image})])
        blk.stop()
        self.assertEqual(self.last_notified[DEFAULT_TERMINAL][0].image, 'foo')
