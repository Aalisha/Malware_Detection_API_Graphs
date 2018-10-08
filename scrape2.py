import requests
import re
from bs4 import BeautifulSoup
import zipfile
import StringIO
#import urllib
#import wget
import shutil
 
'''
URL of the archive web-page which provides link to
all video lectures. It would have been tiring to
download each video manually.
In this example, we first crawl the webpage to extract
all the links and then download videos.
'''
 
# specify the URL of the archive here
archive_url = "http://www.offensivecomputing.net/search.cgi?search=sha1"
archive_url2 = "http://www.offensivecomputing.net/"
 
def get_video_links():
     
    # create response object
    r = requests.get(archive_url)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')
     
    # find all links on web-page
    #links = soup.findAll('a')

    links=soup.findAll('a', href=re.compile('^/download'))
    print "Links:"
    #print links   
    

    video_links = [archive_url2 + link.get('href') for link in links if link.get('href').startswith('/download')]
    
    #video_links = [archive_url + link['href'] for link in links 
    print "Video links:"
    print video_links

    #video_links =soup.findAll('a', href=re.compile('^/download'))
    return video_links

def download_video_series(video_links):
 
    for link in video_links:
 

        # obtain filename by splitting url and getting 
        # last string
        #file_name = link.split('/')[-1]   
        file_name=link
        print "Downloading file:%s"%file_name
         
        
        print "%s downloaded!\n"%file_name

        zip_file_url=file_name
        r = requests.get(zip_file_url, stream=True)
        print StringIO.StringIO(r.content)
        z = zipfile.ZipFile(StringIO.StringIO(r.content))

        targetdir="D:\Sem7\SystemNetSec\Project\Extract";

        z.extractall(targetdir,pwd='infected')
        #Insert code for graph
 
    print "All videos downloaded!"
    return

if __name__ == "__main__":
 
    # getting all video links
    video_links = get_video_links()
    #print video_links
    # download all videos
    download_video_series(video_links)
    
#IDA from cmd prompt:
#"C:\Program Files (x86)\IDA Free\idag.exe" -B "D:\Sem7\SystemNetSec\ProjectExtarct\malware.exe"
    