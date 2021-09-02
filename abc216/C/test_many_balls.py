import many_balls



def test_many_balls_1():
    output_value = many_balls.many_balls(5)
    assert len(output_value) < 120

def test_many_balls_2():
    output_value = many_balls.many_balls(1000000000000000000)
    assert len(output_value) < 120

def test_many_balls_3():
    output_value = many_balls.many_balls(1)
    assert len(output_value) < 120