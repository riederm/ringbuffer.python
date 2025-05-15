from ringbuffer import Ringbuffer

def test_create_ringbuffer():
    # GIVEN an empty ringbuffer
    rb = Ringbuffer(10)
    # THEN the buffer should have 0 elements
    assert rb.get_number_of_elements() == 0

def test_add_one_element():
    # GIVEN an empty ringbuffer
    rb = Ringbuffer(5)
    # WHEN I add an element
    rb.add("a")
    # THEN the buffer should have 1 element
    assert rb.get_number_of_elements() == 1

def test_add_and_remove_element():
    # GIVEN an empty ringbuffer
    rb = Ringbuffer(5)
    rb.add("x")
    # WHEN I remove an element
    removed = rb.remove()
    # THEN the removed element should be the one added and buffer should be empty
    assert removed == "x"
    assert rb.get_number_of_elements() == 0

def test_overwrite_when_full():
    # GIVEN a full ringbuffer
    rb = Ringbuffer(2)
    rb.add("first")
    rb.add("second")
    # WHEN I add another element
    rb.add("third")
    # THEN the oldest element ("first") should be overwritten
    assert rb.get_number_of_elements() == 2
    assert rb.remove() == "second"
    assert rb.remove() == "third"

def test_fifo_order():
    # GIVEN a ringbuffer
    rb = Ringbuffer(3)
    rb.add(1)
    rb.add(2)
    rb.add(3)
    # WHEN I remove elements
    # THEN they should come out in FIFO order
    assert rb.remove() == 1
    assert rb.remove() == 2
    assert rb.remove() == 3
