from PIL import Image
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import VersionProperty


@Discoverable(DiscoverableType.block)
class PILNewImage(Block):

    """ Use PIL to create a new Image and store the Image in a signal """

    version = VersionProperty('0.1.0')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            image = Image.new('1', (64, 48))
            signal.image = image
        self.notify_signals(signals, output_id='default')
