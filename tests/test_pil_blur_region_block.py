from unittest.mock import Mock, patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..pil_blur_region_block import PILBlurRegion


class TestPILCropImage(NIOBlockTestCase):

    @patch(PILBlurRegion.__module__ + '.ImageFilter')
    def test_blur(self, mock_filter):
        dummy_image = Mock()
        mock_filter.GaussianBlur.return_value = Mock()
        blk = PILBlurRegion()
        self.configure_block(blk, {
            'blur': 42,
            'left': 0,
            'upper': 1,
            'right': 2,
            'lower': 3})
        blk.start()
        blk.process_signals([
            Signal({'image': dummy_image}),
        ])
        blk.stop()
        self.assert_num_signals_notified(1)
        dummy_image.crop.assert_called_once_with((0, 1, 2, 3))
        mock_filter.GaussianBlur.assert_called_once_with(42)
        dummy_image.crop.return_value.filter.assert_called_once_with(
            mock_filter.GaussianBlur.return_value)
        dummy_image.paste.assert_called_once_with(
            dummy_image.crop.return_value.filter.return_value, (0, 1, 2, 3))
