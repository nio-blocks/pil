from enum import Enum
from PIL import Image

from nio.block.base import Block
from nio.properties import IntProperty, VersionProperty, \
        ObjectProperty, PropertyHolder, SelectProperty


class Mode(Enum):
    RGB = 'RGB'
    RGBA = 'RGBA'
    BW = 'L'


class Size(PropertyHolder):
    x = IntProperty(default='64', title="x")
    y = IntProperty(default='48', title="y")


class PILNewImage(Block):

    """ Use PIL to create a new Image and store the Image in a signal """

    version = VersionProperty('0.1.0')
    size = ObjectProperty(Size, default=Size(), title='Size')
    mode = SelectProperty(Mode, default=Mode.RGB, title='Image Mode')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            try:
                self._create_image(signal)
            except:
                self.logger.exception('Failed to create image')
        self.notify_signals(signals)

    def _create_image(self, signal):
        x, y = self._image_size(signal)
        image = Image.new(self.mode().value, (x, y))
        signal.image = image

    def _image_size(self, signal):
        try:
            x = int(self.size().x(signal))
            y = int(self.size().y(signal))
        except:
            raise Exception('Failed to evaluate block properties')
        return x, y
