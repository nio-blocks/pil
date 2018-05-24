from PIL import Image

from nio.block.base import Block
from nio.properties import Property, VersionProperty


class PILImageFromArray(Block):

    """ Convert an array to a PIL Image """

    version = VersionProperty('0.1.0')
    input_array = Property(title='Array to Convert', default='{{ $image }}')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            input = self.input_array(signal)
            converted_image = Image.fromarray(input)
            signal.image = converted_image
        self.notify_signals(signals)
