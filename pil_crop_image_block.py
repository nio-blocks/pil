from nio.block.base import Block
from nio.properties import IntProperty, VersionProperty


class PILCropImage(Block):

    """ Crop a PIL image to the specified region """

    version = VersionProperty('0.1.0')
    left = IntProperty(title='Left Edge', default=0)
    upper = IntProperty(title='Upper Edge', default=0)
    right = IntProperty(title='Right Edge',
                        default='{{ min($image.width, $image.height) }}')
    lower = IntProperty(title='Lower Edge',
                        default='{{ min($image.width, $image.height) }}')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            box = (self.left(signal),
                   self.upper(signal),
                   self.right(signal),
                   self.lower(signal))
            self.logger.debug('image size: {}'.format(signal.image.size))
            cropped = signal.image.crop(box)
            self.logger.debug('cropped: {}'.format(cropped.size))
            signal.image = cropped
        self.notify_signals(signals)
