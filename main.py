import requests, zipfile, io
from bs4 import BeautifulSoup

def extract_zip(url, domain, desired_address, destination):
    """
        Finds, downloads, and extracts zip files contained in hyperlinks on a webpage to specified destination.
        Packages utilized: requests, zipfile, io, and bs4/BeautifulSoup

        Parameters
        ----------
        url
            TYPE String
            DESCRIPTION URL address of webpage containing desired zip files
        domain
            TYPE String
            DESCRIPTION Domain name and extension of site
        desired_address
            TYPE String
            DESCRIPTION Directory address containing desired zip files
        destination
            TYPE String
            DESCRIPTION Directory address for destination of extracted zip files

        Returns
        -------
        None.

    """
    # TODO: 
    # - reduce parameter count and implment extraction of domain from url
    # - implment error handling
    ##
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
    }

    # retrieves html content from url
    r = requests.get(url, headers=headers)
    html_contents = r.text

    # prepares html contents for parsing
    html_soup = BeautifulSoup(html_contents, 'html.parser')

    # retrieves all hyperlinks in html contents of URL
    hyperlinks = html_soup.find_all('a')

    addresses = list()

    # appends to addresses list all hyperlink addresses containing desired directory address
    for hyperlink in hyperlinks:

        # gets link address
        address = hyperlink.get('href')

        # checking for string to avoid type error
        if not isinstance(address, str):
            continue

        # appends address containing desired address
        if not address.find(desired_address) == -1:
            addresses.append('https://www.' + domain + address)

    # downloads zip file from every address in addresses
    for address in addresses:

        # creates url address of zip file
        url = address

        # downloads zip file
        r = requests.get(url, headers=headers)
        z = zipfile.ZipFile(io.BytesIO(r.content))

        # extracts zip file
        z.extractall(destination)

        # prints extracted zip file
        print(address)
