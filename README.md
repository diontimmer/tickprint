# tickprint
 Prints variables at a set interval.
 Coming from the unreal engine world, I like having a quick and dirty way to constantly monitor values.
 ```python
 from tickprint import tickprint

tickprint(interval=1, object=object_with_attrs, attr=attribute_to_print)

# will print the attr associated with object every interval sec.

 ```
