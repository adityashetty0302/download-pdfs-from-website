import os
import urllib.request
import urllib.request

if __name__ == '__main__':

    try:
        from bs4 import BeautifulSoup
    except Exception as e:
        print("Pls install BeautifulSoup 4")

    url = input('[+] Enter the url: ')

    try:

        i = 0
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html.read(), 'html.parser')
        for tag in soup.findAll('a', href=True):

            if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
                current = urllib.request.urlopen(tag['href'])

                print("\n[*] Downloading: %s" % (os.path.basename(tag['href'])))

                f = open(os.path.basename(tag['href']), "wb")
                f.write(current.read())
                f.close()
                i += 1

        print("\n[*] Downloaded %d files" % (i))
        input("[+] Press any key to exit...")

    except Exception as e:
        print(e)
