from PIL import Image
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty, VersionProperty, \
        ObjectProperty, PropertyHolder


class Size(PropertyHolder):
    x = ExpressionProperty(default='64')
    y = ExpressionProperty(default='48')


@Discoverable(DiscoverableType.block)
class PILNewImage(Block):

    """ Use PIL to create a new Image and store the Image in a signal """

    version = VersionProperty('0.1.0')
    size = ObjectProperty(Size, default=Size())

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            try:
                self._create_image(signal)
            except:
                self._logger.exception('Failed to create image')
        self.notify_signals(signals, output_id='default')

    def _create_image(self, signal):
        x, y = self._image_size(signal)
        image = Image.new('1', (x, y))
        signal.image = image

    def _image_size(self, signal):
        try:
            x = int(self.size.x(signal))
            y = int(self.size.y(signal))
        except:
            raise Exception('Failed to evaluate block properties')
        return x, y
