import zipfile
import StringIO
import requests
zip_file_url="http://www.offensivecomputing.net/download.cgi?id=95727718&auth=33cb6d23cf1d9298412dd63c39bf6c6e4df29db5e52b3bd34a50a88720818763"
r = requests.get(zip_file_url, stream=True)
print StringIO.StringIO(r.content)
z = zipfile.ZipFile(StringIO.StringIO(r.content))
'''z.extractall()

from zipfile import ZipFile'''
targetdir="D:\Sem7\SystemNetSec\Project";
'''with ZipFile('D:\Sem7\SystemNetSec\Project\malware.zip') as zf:'''
z.extractall(targetdir,pwd='infected')