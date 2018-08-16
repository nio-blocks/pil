from base64 import b64decode
from io import BytesIO
from PIL import Image

from nio.block.base import Block
from nio.properties import VersionProperty


class PILBase64Decode(Block):

    """ Convert a base64-encoded string to a PIL Image """

    version = VersionProperty("0.1.0")

    def __init__(self):
        super().__init__()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            decoded = b64decode(signal.image)
            buffer = BytesIO(decoded)
            signal.image = Image.open(buffer)
        self.notify_signals(signals)
