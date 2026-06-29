def ft_filter(function, it):
    """Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true."""
    if function is None:
        return [item for item in it if item]
    return [item for item in it if function(item)]
