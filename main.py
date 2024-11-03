from base64 import b64decode,b64encode
import argparse

def encode(value):
    """
    Encode a given string into base64 format.

    Parameters:
    value (str): The string to be encoded. It should be a valid UTF-8 encoded string.

    Returns:
    str: The base64 encoded string.
    """

    return b64encode(value.encode()).decode()

def decode(value):
    """
    Decode a given encoded base64 string to plain text.

    Parameters:
    value (str): The base64 string to be decoded. It should be a valid UTF-8 encoded string.

    Returns:
    str: The decoded string.
    """

    try:
        decoded = b64decode(value.encode()).decode()
    except:
        decoded = "Invalid base64 input"
    return decoded

parser = argparse.ArgumentParser(description="Encode or decode text using base64")
parser.add_argument(
    '-e', '--encode',
    type=str,
    help="Text to encode",
    metavar=""
)
parser.add_argument(
    '-d', '--decode',
    type=str,
    help="Text to decode",
    metavar=""
)

args = parser.parse_args()

if args.encode:
    print(encode(args.encode))
elif args.decode:
    print(decode(args.decode))
else:
    parser.print_help()