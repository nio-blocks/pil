from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty, VersionProperty, \
        ObjectProperty, PropertyHolder
from nio.util.environment import NIOEnvironment


class Coordinate(PropertyHolder):
    x = ExpressionProperty(default='0')
    y = ExpressionProperty(default='0')


@Discoverable(DiscoverableType.block)
class PILDrawText(Block):

    """ Draw text to a PIL Image """

    version = VersionProperty('0.1.0')
    text = ExpressionProperty(title='Text', default='Hello, n.io!')
    coordinate = ObjectProperty(Coordinate, default=Coordinate())

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            try:
                self._draw_text(signal)
            except:
                self._logger.exception('Failed to draw text to image')
        self.notify_signals(signals, output_id='default')

    def _draw_text(self, signal):
        """ Edits the Image object in signal.image by drawing text to it """
        self._logger.debug('Create Draw object')
        image = self._get_image(signal)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        try:
            text = self.text(signal)
            x = int(self.coordinate.x(signal))
            y = int(self.coordinate.y(signal))
        except:
            raise Exception('Failed to evaluate block properties')
        self._logger.debug(
            'Draw text: {} at location: {}, {}'.format(text, x, y))
        draw.text((x, y), text, font=font, fill=255)
        self._logger.debug('Done drawing text: {}'.format(signal.image))

    def _get_image(self, signal):
        try:
            image = signal.image
        except:
            raise Exception('Signal does not containg attribute `image`')
        if type(image) == Image.Image:
            return image
        else:
            raise Exception('`image` needs to be a PIL Image')
