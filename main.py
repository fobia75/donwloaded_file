"""Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте потоки."""

# import threading
# import time
# import requests

# urls = [
#     'https://vk.com/',
#     'https://www.youtube.com/',
#     'https://wireframe.cc',
#     'https://letsencrypt.org/',
#     'https://getbootstrap.com/',
#     'https://www.editor.ru/',
#     'https://pythontutor.com/'
# ]


# def download(url):
#     response = requests.get(url)
#     file_name = 'threading_'+url.replace('https://','').replace('.','_').replace('/','')+ '.html'
#     with open('ile_name','w',encoding='utf-8') as f:
#         f.write(response.text)
#     print(f'dowloading: {url} in {time.time() - start_time:.2f} seconds')    


# threads = [] 
# start_time = time.time()  

# for url in urls:
#     thread = threading.Thread(target= download, args=[url])
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()    

"""Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте процессы."""

# from multiprocessing import Process
# import time
# import requests


# urls = [
#     'https://vk.com/',
#     'https://www.youtube.com/',
#     'https://wireframe.cc',
#     'https://letsencrypt.org/',
#     'https://getbootstrap.com/',
#     'https://www.editor.ru/',
#     'https://pythontutor.com/'
# ]

# def download(url):
#     response = requests.get(url)
#     file_name = 'multiprocessing_'+url.replace('https://','').replace('.','_').replace('/','')+ '.html'
#     with open('ile_name','w',encoding='utf-8') as f:
#         f.write(response.text)
#     print(f'dowloading: {url} in {time.time() - start_time:.2f} seconds')  


# processes = []
# start_time = time.time()  

# if __name__ == '__main__':
#     for url in urls:
#         prosess = Process(target= download, args=(url,))
#         processes.append(prosess)
#         prosess.start()

#     for prosess in processes:
#         prosess.join()      


"""Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте асинхронный подход."""

# import time
# import requests
# import asyncio
# import aiohttp

# urls = [
#     'https://vk.com/',
#     'https://www.youtube.com/',
#     'https://wireframe.cc',
#     'https://letsencrypt.org/',
#     'https://getbootstrap.com/',
#     'https://www.editor.ru/',
#     'https://pythontutor.com/'
# ]

async def dowload(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()


    filename = 'data/asyncio_'+ url.replace('https://','').replace('.','_').replace('/','')+ '.html'   
    with open(filename,'w',encoding='utf-8') as f:
        f.write(text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')



# async def main():
#     tasks = []
#     for url in urls:
#         task = asyncio.ensure_future(dowload(url))
#         tasks.append(task)
#         await asyncio.gather(*tasks)


# start_time = time.time()

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()  
#     loop.run_until_complete(main())     


"""Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте потоки."""

# import threading
# import time
# import os

# PATH = 'data'
# count = 0
# def get_amount_worlds(filename: str)-> None:
#     global count
#     with open(filename, encoding='utf-8') as f:
#         count += len(f.read().split())


# if __name__ == '__main__':
#     threads = [] 
#     for root, dirs, files in os.walk(PATH):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)
#             thread = threading.Thread(target= get_amount_worlds, args= (file_path, ))
#             threads.append(thread)
#             thread.start() 

#     for thread in threads:
#         thread.join() 


#     for thread in threads:     
#         print(f'количество символов:{count}')        


"""Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте процессы.
"""

# from multiprocessing import Process
# import multiprocessing
# import time
# import os

# PATH = 'data'
# count = multiprocessing.Value('i', 0)


# def get_amount_worlds(count, file_name)-> None: 
#     with open(file_name, encoding='utf-8') as f:
#         with count.get_lock():    
#             count.value += len(f.read().split())



# start_time = time.time()  


# if __name__ == '__main__':
#     processes = [] 

#     for root, dirs, files in os.walk(PATH):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)
#             proses = Process(target= get_amount_worlds, args= (count, file_path, ))
#             processes.append(proses)
#             proses.start() 

#     for proses in processes:
#         proses.join() 
#         print(f'количество символов:{count.value}') 


"""Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте асинхронный подход.
"""


import asyncio
import os


PATH = 'data'
count = 0

async def get_amount_worlds(file_path)-> None: 
    global count
    with open(file_path, encoding='utf-8') as f:
        count += len(f.read().split())


async def main():  
    tasks = [] 
    for root, dirs, files in os.walk(PATH):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            tasks.append(asyncio.create_task(get_amount_worlds(file_path)))
    await asyncio.gather(*tasks)

        
if __name__ == '__main__':
    asyncio.run(main())
    print(f'количество символов: {count}')










