# Base64 Encoder/Decoder
A Python script that encodes and decodes text using base64.

# Installation
You can clone this repository or download the source code.
```
git clone https://github.com/brm0x/base64.git
cd base64
python main.py --help
```
# Encoding
To encode a text, use the -e or --encode flag followed by the text to encode.
```
python main.py -e "Hello, World!"
SGVsbG8sIFdvcmxkIQ==
```
# Decoding
To decode a base64 encoded text, use the -d or --decode flag followed by the encoded text.
```
python main.py -d "SGVsbG8sIFdvcmxkIQ=="
Hello, World
```
# Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
