#!/usr/bin/env python
__author__ = 'historypeats'
import requests
import sys

data = 'About that fox...'
testFile = 'someTestFile.txt'
proxies = {}


def main():
    """

    Main
    """

    if len(sys.argv) < 2:
        sys.exit("Need urls file.")

    if len(sys.argv) == 3:
        proxies = {'http': sys.argv[2]}
    try:
        urlFile = open(sys.argv[1], 'r')
    except IOError:
        sys.exit('Unable to open file: ' + sys.argv[1])

    for url in urlFile:
        puturl = url.strip() + testFile

        try:
            response = requests.put(puturl, data=data, proxies=proxies)
            if response.status_code == 200:
                print "[VULNERABLE!] - " + puturl
            else:
                print "[" + str(response.status_code) + "] - " + puturl
        except requests.ConnectionError:
            print 'Connection failed: ' + url
        except requests.Timeout:
            print 'Connection timed out: ' + url
        except requests.HTTPError:
            print 'Invalid HTTP Response: ' + url
        except Exception:
            print 'Unknown error: ' + url

if __name__ == '__main__':
    main()
    '''
    key{whatDidtheF0xSay?}
    '''