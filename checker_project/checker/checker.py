from http.client import HTTPConnection
from urllib.parse import urlparse
import asyncio
import aiohttp
from defer import return_value



def site_checker(url):
    """
    Check if a site is up and running
    """
    try:
        url = urlparse(url)
        conn = HTTPConnection(url.netloc)
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        if res.status == 200:
            return True
        else:
            return False
    except:
        return False

        
def site_is_online(url, timeout=2):
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        conn = HTTPConnection(host, port=port, timeout=timeout)
        try:            
            conn.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            conn.close()
    raise error

async def site_is_online_async(url, timeout=2):
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for schema in ("http", "https"):
        target_url = f"{schema}://{host}"
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(target_url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as e:
                error = e
    raise error