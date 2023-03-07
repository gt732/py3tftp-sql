import os
from pathlib import Path
from .netascii import Netascii


def sanitize_fname(fname):
    """
    Ensures that fname is a path under the current working directory.
    """
    # Remove root (/) and parent (..) directory references.
    path = os.fsdecode(fname).lstrip("./")
    abs_path = Path.cwd() / path

    # Verify that the formed path is under the current working directory.
    try:
        abs_path.relative_to(Path.cwd())
    except ValueError:
        raise FileNotFoundError

    # Verify that we are not accesing a reserved file.
    if abs_path.is_reserved():
        raise FileNotFoundError

    return abs_path


class FileWriter(object):
    """
    Wrapper around a regular file that implements:
    - write_chunk - for closing the file when bytes written
      is less than chunk_size.
    When it goes out of scope, it ensures the file is closed.
    """

    def __init__(self, fname, chunk_size, mode=None):
        self._f = None
        self.fname = sanitize_fname(fname)
        self.chunk_size = chunk_size

        if mode == b"netascii":
            self._f = Netascii(self._f)

    def _flush(self):
        if self._f:
            self._f.flush()

    def write_chunk(self, data):
        bytes_written = self._f.write(data)

        if not data or len(data) < self.chunk_size:
            self._f.close()

        return bytes_written

    def __del__(self):
        if self._f and not self._f.closed:
            self._f.close()
