import sys
import hashlib
import base64


def hash_of_contents(entry_points_path):
    """Calculate hash of file's contents."""
    with open(entry_points_path, 'r') as f:
        contents = f.read()
        if sys.version_info[0] > 2 and isinstance(contents, str):
            contents = contents.encode('utf-8', 'surrogateescape')
        hash = hashlib.sha256()
        hash.update(contents)
        digest = base64.urlsafe_b64encode(hash.digest())
        digest = b'sha256=' + digest.rstrip(b'=')
        digest = digest.decode('utf-8')
        print(digest)

contents = sys.argv[1]
hash_of_contents(contents)