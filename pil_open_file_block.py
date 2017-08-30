from PIL import Image

from nio.block.base import Block
from nio.properties import FileProperty, VersionProperty


class PILOpenFile(Block):

    """ Use PIL to open a file and store the Image in a signal """

    version = VersionProperty('0.1.0')
    file = FileProperty(title='Image File', default='niologo.png')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            image = self._load_image_file(signal)
            if True:
                # TODO: resize image if configured to do so
                image = image.resize((64, 48), Image.ANTIALIAS)
            signal.image = image
        self.notify_signals(signals)

    def _load_image_file(self, signal):
        try:
            return Image.open(self.file(signal).file).convert('1')
        except:
            self.logger.exception('Failed to get file from signal')
