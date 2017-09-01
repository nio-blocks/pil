from PIL import Image, ImageDraw, ImageFont

from nio.block.base import Block
from nio.properties import Property, IntProperty, VersionProperty, \
        ObjectProperty, PropertyHolder


class Coordinate(PropertyHolder):
    x = IntProperty(default='0', title="x")
    y = IntProperty(default='0', title="y")


class PILDrawText(Block):

    """ Draw text to a PIL Image """

    version = VersionProperty("0.1.0")
    text = Property(title='Text', default='Hello, n.io!')
    coordinate = ObjectProperty(
        Coordinate, default=Coordinate(), title='Coordinate')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            try:
                self._draw_text(signal)
            except:
                self.logger.exception('Failed to draw text to image')
        self.notify_signals(signals)

    def _draw_text(self, signal):
        """ Edits the Image object in signal.image by drawing text to it """
        self.logger.debug('Create Draw object')
        image = self._get_image(signal)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        try:
            text = str(self.text(signal))
            x = int(self.coordinate().x(signal))
            y = int(self.coordinate().y(signal))
        except:
            raise Exception('Failed to evaluate block properties')
        self.logger.debug(
            'Draw text: {} at location: {}, {}'.format(text, x, y))
        draw.text((x, y), text, font=font, fill=255)
        self.logger.debug('Done drawing text: {}'.format(signal.image))

    def _get_image(self, signal):
        if not hasattr(signal, 'image'):
            raise Exception('Signal does not containg attribute `image`')
        elif not isinstance(signal.image, Image.Image):
            raise Exception('`image` needs to be a PIL Image')
        else:
            return signal.image
