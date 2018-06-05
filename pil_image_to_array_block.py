import numpy as np

from nio.block.base import Block
from nio.properties import VersionProperty


class PILImageToArray(Block):

    """ Convert a PIL Image to a numpy array """

    version = VersionProperty("0.1.0")

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            signal.image = np.array(signal.image)
        self.notify_signals(signals)
