from base64 import b64decode
from io import BytesIO

from nio.block.base import Block
from nio.properties import VersionProperty


class PILBase64Decode(Block):

    """ Convert a PIL image to a base64-encoded string """

    version = VersionProperty('0.1.0')

    def __init__(self):
        super().__init__()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            frame_buffer = BytesIO()
            signal.image.save(frame_buffer, format='JPEG')
            signal.image = b64decode(frame_buffer.getvalue())
        self.notify_signals(signals)
