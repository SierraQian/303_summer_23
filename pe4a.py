# In this program, I searched 10 topics and get error with 3 of them when using page function
# I checked the first topic "generative artificial intelligence"
# When I using ""generative artificial intelligence - Wikipedia" as the parameter to the wikipedia.page(), that works
# In order to solve this bug, I used try, expect, and continue to raise expection of the error ones and jump them to the next iteration
# However, when I change the auto_suggest as False in the wikipedia.page(), the page could be found.

import wikipedia
import time

start_time = time.perf_counter()

related_pages = wikipedia.search("generative artificial intelligence") # default get 10 related topics
print(related_pages)

''''
wikipedia.search() accepts the following parameters:
query: This is the term that you want to search.
results: This is an optional parameter that specifies how many results you want for the query. It accepts an integer value. The default value of this parameter is 10.
suggestion: This is also an optional parameter that accepts boolean values. If True, it will return suggestions based on your query. The default value of this parameter is False.
'''

# filelist = []
for topic in related_pages:
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        filename = f"{page.title}.txt"
        # filelist.append(filename)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page.content)
        print(f"File '{filename}' created.")
    except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e:
        print(f"Error processing topic: {topic} - {e}")
        continue
    except IOError:
        print(f"Error creating file for topic: {topic}")
        continue

# print(filelist)

end_time = time.perf_counter()  # Record the end time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

