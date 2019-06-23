from PIL import ImageFilter
from nio.block.base import Block
from nio.properties import IntProperty, VersionProperty


class PILBlurRegion(Block):

    blur = IntProperty(title='Blur Radius', default=2, order=0)
    left = IntProperty(title='Left Edge', default=0, order=1)
    upper = IntProperty(title='Upper Edge', default=0, order=2)
    right = IntProperty(title='Right Edge', default=0, order=3)
    lower = IntProperty(title='Lower Edge', default=0, order=4)

    version = VersionProperty('0.1.0')

    def process_signal(self, signal):
        blur = self.blur(signal)
        box = (self.left(signal),
               self.upper(signal),
               self.right(signal),
               self.lower(signal))
        self.logger.debug('blur: {}, region: {}'.format(blur, (box)))
        cropped = signal.image.crop(box)
        blurred = cropped.filter(ImageFilter.GaussianBlur(blur))
        signal.image.paste(blurred, box)
        return signal
