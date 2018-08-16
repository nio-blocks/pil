from base64 import b64encode
from io import BytesIO

from nio.block.base import Block
from nio.properties import VersionProperty


class PILBase64Encode(Block):

    """ Convert a PIL image to a base64-encoded string """

    version = VersionProperty("0.1.0")

    def __init__(self):
        super().__init__()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            if signal.image.mode == 'RGBA':
                # JPEG cannot represent Alpha channel, convert it
                signal.image = signal.image.convert('RGB')
            frame_buffer = BytesIO()
            signal.image.save(frame_buffer, format='JPEG')
            signal.image = b64encode(frame_buffer.getvalue())
        self.notify_signals(signals)
