# Shuffling several apps

This code is updated for working with the recent (>3.0.8). 


to make it work, do 2 things:

1. Add `StartApp` at the beginning of `app_sequence` of the session config where you want 
to randomize apps (all following apps will be randomized, with an exception of `StartApp`)

2. in each `pages.py` instead of
```python
from ._builtin import  Page
```
insert 
```python
from StartApp.pages import Page
```

You can keep the old import statement and insert a new one **after** that:

```python
from ._builtin import Page, WaitPage
from StartApp.pages import Page
```


## Citation:
if use, please cite:
> Chapkovski, Philipp, Randomizing apps in oTree (February 15, 2021). Available at SSRN: https://ssrn.com/abstract=3786021

That's it, enjoy!

