# Wikipedia Frequency Lookup

Simple script written in Python to get the 20 words and their frequency percentage with highest frequency in an English Wikipedia article.
You enter your string and using [Wikipedia Search API](https://www.mediawiki.org/wiki/API:Search), you get the top 20 words

Built this, so that I could implement my basic learning somewhere and play around with some libraries :books: . 

```python
  python main.py <your-string>
```

If you want to remove the stop words _(such as "and", "the", "a", "an", and similar words)_ from frequency table, simply add a **yes** after your string.

```python
  python main.py <your-string> yes
```

----

![screenshot](/screenshots/Screenshot%20from%202016-04-24%2001:42:18.png?raw=true)

![screenshot](/screenshots/Screenshot%20from%202016-04-24%2001:42:44.png?raw=true)
