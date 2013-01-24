# this is an implementation of the 'series' functionality using a module.

n = 0

def add_one():
    global n
    n = n + 1
    return n

# additional questions to address:
#  - what does 'global' do, above?
#  Makes it global accessable. 

#  - what naming limitations are there on series.py? Could we name it
#  no global constant symble. Can't start with numbers. 

#        series_mod.py or series-mod.py, and still have it work as a module?
