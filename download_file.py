import threading
import time
from urllib.request import urlopen
from multiprocessing import Process
import asyncio
import aiohttp


counter = 0
lock = threading.Lock()

def download(url):
    global counter
    response = urlopen(url)
    file_name = 'data/'+url.replace('https://','').replace('.','_').replace('/','')+ '.jpg'
    with open(file_name, 'wb') as f:
        f.write(response.read())
    with lock:
            counter += time.time() - start_time
    print(f'dowloading: {url} in {time.time() - start_time:.2f} seconds')
    print(f'общее время выполнения скачивания: {counter:.2f}') 


def multiprocess():
    processes = []
    for url in list_url:
        prosess = Process(target= download, args=(url,))
        processes.append(prosess)
        prosess.start()

    for prosess in processes:
        prosess.join()   


start_time = time.time()  


def thread_():
    threads = []
    for url in list_url:
        thread = threading.Thread(target= download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  



async def dowload_asin(url):
    global counter
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img = await response.read()  


    filename = 'data/asyncio_'+ url.replace('https://','').replace('.','_').replace('/','')+ '.jpg'   
    with open(filename,'wb') as f:
        f.write(img)
        counter += time.time() - start_time
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds') 
    print(f'общее время выполнения скачивания: {counter:.2f}') 


async def main():
    tasks = []
    for url in list_url:
        task = asyncio.ensure_future(dowload_asin(url))
        tasks.append(task)
        await asyncio.gather(*tasks)




if __name__ == '__main__':
    choice_ = input('выберите как скачивать изображение, введите 1 если потоком, 2 если процесом, 3 если асинхронно: ')
    list_url = []
    while True:
        url = input('ведите url изображения, для завершения введите "stop": ')
        if url == 'stop':
            break
        list_url.append(url)
    if choice_ == '1':
        thread_()
    if choice_ == '2':
        multiprocess()    
    if choice_ == '3':
        loop = asyncio.get_event_loop()  
        loop.run_until_complete(main()) 

    