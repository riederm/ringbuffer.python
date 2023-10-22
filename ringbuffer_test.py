from ringbuffer import Ringbuffer

def test_create_ringbuffer():
    rb = Ringbuffer(10)
    assert rb.get_number_of_elements() == 0

