import os
import csv
import requests
import mimetypes
import concurrent.futures


class ImageScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
    }
    total_images = 0  # total images in given csv file
    downloaded = 0  # Total images downloaded with status 200

    def __init__(self, threads=10, path='images', input='urls.csv'):
        """
        Parameters:
        _threads: total number of threads to run parallel
        _path: directory to store downloaded image files
        _input: CSV file will contain two columns: name of image, url
        _urls: All urls set from CSV file (name, url)
        """
        self._threads = threads
        self._path = path
        self._input_csv = input

        self._urls = set(())

        # Read all urls and filename from given csv file
        with open(self._input_csv) as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                image_name = os.path.join(self._path, row[0])
                image_url = row[1]
                self._urls.add((image_name, image_url))

        ImageScraper.total_images = len(self._urls)

    def download_image(self, image_data):
        """Scrape image from given image_url"""
        image_name, image_url = image_data

        print(f'Downloading: {image_name}')

        res = requests.get(
            image_url,
            allow_redirects=True,
            headers=ImageScraper.headers
        )

        if res.status_code == 200:
            # Get image file extension
            content_type = res.headers['content-type']
            extension = mimetypes.guess_extension(content_type)
            open(image_name+extension, 'wb').write(res.content)

            # Increase downloaded images count
            ImageScraper.downloaded += 1
        elif res.status_code == 404:
            print(f'ERROR (404): {image_name!r} URL is not found!')
        else:
            print(
                f'ERROR ({res.status_code}): Unable to download '
                f'{image_name!r}.'
            )

    def start_scraper(self):
        """Start concurrent scraper"""
        with concurrent.futures.ThreadPoolExecutor(self._threads) as executor:
            executor.map(self.download_image, self._urls)

        print(
            f'{ImageScraper.downloaded} of '
            f'{ImageScraper.total_images} images are downloaded!'
        )


if __name__ == '__main__':
    cc = ImageScraper(threads=10, path='images', input='urls.csv')
    cc.start_scraper()
