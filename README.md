PILBase64Decode
===============
Decode a base64-encoded string to a PIL.Image object

Properties
----------
None

Inputs
------
- **default**: Any list of signals
  - *image* (string) base64 representation of the image

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (object) PIL.Image object

Commands
--------
None

***

PILBase64Encode
===============
Convert a PIL image to a base64-encoded string

Properties
----------
None

Inputs
------
- **default**: Any list of signals
  - *image* (object) PIL.Image object

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (string) base64 representation of the image

Commands
--------
None

***

PILCropImage
============
Crop a PIL image to the specified region

Properties
----------
- **left**: Pixel offset from left edge of original image
- **lower**: Pixel offset from bottom edge of original image
- **right**: Pixel offset from right edge of original image
- **upper**: Pixel offset from top edge of original image

Inputs
------
- **default**: Any list of signals
  - *image* (object) PIL.Image object

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (object) PIL.Image object with size (`right - left`, `lower - upper`)

Commands
--------
None

***

PILDrawText
===========
Draw text to an existing Python Image Library (PIL) Image.

Properties
----------
- **coordinate**: X, Y coordinates to start text.
- **text**: Text to draw to image.

Inputs
------
- **default**: Any list of signals
  - *image* (object) PIL.Image object

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (object) original image with text added.

Commands
--------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)

***

PILNewImage
===========
Create a new Python Image Library (PIL) Image and store it in the *image* attribute of the input signal.

Properties
----------
- **size**: X, Y size of new image.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (object) PIL.Image object

Commands
--------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)

***

PILOpenFile
===========
Load an image file from disk and create a new Python Image Library (PIL) Image and store it in the *image* attribute of the input signal.

Properties
----------
- **file**: Location of image file to open

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (object) PIL.Image object

Commands
--------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)

***

PILResizeImage
==============
Resize a PIL image to the specified dimensions

Properties
----------
- **x**: Output image width, in pixels
- **y**: Output image height, in pixels

Inputs
------
- **default**: Any list of signals
  - *image* (object) PIL.Image object

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (object) PIL.Image object with size (`x`, `y`)

Commands
--------
None

***

PILSaveImage
============
Save a PIL image object to disk in the specified format

Properties
----------
- **file**: Path to save image file. The file extension specifies format.

Inputs
------
- **default**: Any list of signals
  - *image* (object) PIL.Image object

Outputs
-------
- **default**: Same list of signals as input.
  - *image* (object) PIL.Image object

Commands
--------
None

