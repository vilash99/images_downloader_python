# Multi-Threaded Image Downloader in Python

Retrieve image names and URLs from a CSV file, then employ the requests library with multithreading to download the corresponding images in Python.

## Parameters
* <em>threads<em>: total number of threads to run parallel
* <em>path<em>: directory to store downloaded image files (here images/)
* <em>input<em>: CSV file will contain two columns: name of image, url (here urls.csv)

## Installation
1. Clone the repo

```bash
git clone https://github.com/vilash99/images_downloader_python.git
```
2. Setup virtual environment & Install Requirements

```bash
python -m venv .venv
.venv/Scripts/activate
pip install requests
```

3. Run the script
Pass required values in function e.g. threads, path to save images, and input CSV file. Then run the script with the given command.
```bash
python image_downloader.py
```
## Contribution
Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Your contributions are highly appreciated.

## License
This project is licensed under the MIT License.

## Contact me
If you need a script similar to this or have new requirements. You can contact me at vilashdd[at]gmail[com].

My website: https://vilashdaate.com/

My blog: https://www.kushalstudy.com/
