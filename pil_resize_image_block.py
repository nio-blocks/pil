from nio.block.base import Block
from nio.properties import IntProperty, VersionProperty


class PILResizeImage(Block):

    """ Resize a PIL image to the specified dimensions """

    version = VersionProperty('0.1.0')
    x = IntProperty(title='Width', default='{{ $image.width * 0.5 }}')
    y = IntProperty(title='Height', default='{{ $image.height * 0.5 }}')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            new_dims = (self.x(signal), self.y(signal))
            self.logger.debug('image size: {}'.format(signal.image.size))
            resized = signal.image.resize(new_dims)
            self.logger.debug('resized: {}'.format(resized.size))
            signal.image = resized
        self.notify_signals(signals)
