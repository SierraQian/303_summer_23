import wikipedia
import concurrent.futures
import time

def download_wiki_page(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        filename = f"{page.title}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page.content)
        print(f"File '{filename}' created for topic: {topic}")
        print()
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e:
        print(f"Error processing topic: {topic} - {e}")
    except IOError:
        print(f"Error creating file for topic: {topic}")

start_time = time.perf_counter()  # Record the start time

topics = wikipedia.search("generative artificial intelligence")
num_threads = len(topics)  # Number of concurrent threads

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(download_wiki_page, topics)

'''
max_workers: A parameter that specifies the maximum number of worker threads in the thread pool.
submit(fn, *args, **kwargs): Submits a callable function fn with optional arguments args and keyword arguments kwargs to the thread pool for execution. It returns a concurrent.futures.Future object representing the result of the task.
map(func, *iterables, timeout=None): A higher-level method that applies a function func to each item of one or more iterables and returns an iterator that yields the results in the order of completion.
shutdown(wait=True): Shuts down the thread pool. If wait is True (default), it waits for all submitted tasks to be completed before terminating the threads. If wait is False, it immediately stops the threads, even if tasks are still running.
'''

end_time = time.perf_counter()  # Record the end time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")