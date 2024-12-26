# DSA and Visualizations in Python

Hey! I've made a variety of basic data structres in Python, alongside a few sorting algorithms. However, due to the sometimes difficult concepts surrounding some of them, mainly merge and quick sort, I've also made visualizations using matplotlib and numpy for each sorting algorithm. If you want to see a default sort, something like this:



Then just run the Vis program for the algorithm you want to see. If you want to use a custom list or change the number of values in the list, you can edit that by importing the visualization file, instantiating a new Vis() object, and changing the *lst* attribute that the algorithm sorts, or by feeding in an *amount* parameter into the object to change the size of the array. Then, call the sort like this:

```
my_vis = Vis(10)
my_vis.lst = np.flip(my_vis.lst) #  or whatever change you want to make to the unsorted array
merge_sort(my_vis)
```

The program should automatically create a matplotlib window and run the simulation. It will close out once completed.
Have fun!
