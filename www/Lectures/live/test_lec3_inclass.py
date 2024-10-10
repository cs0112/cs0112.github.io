from lecture03 import count_words

def test_dashes_inclass():
    input = "live-code Smith-Buonanno - -17 Smith-Buonanno Smith"
    output = {'live-code': 1,
              'Smith-Buonanno': 2,
              '-': 1, 
              '-17': 1,
              'Smith': 1}
    assert count_words(input) == output 

def test_caps_inclass():
    input = "Brown University built a brown building"
    output = {'Brown': 1,
              'University': 1,
              'built': 1,
              'a': 1,
              'brown': 1,
              'building': 2}
    assert count_words(input) == output 

def add(x, y):
    return x + y

def test_example():
    input1 = 5
    input2 = -6
    output = -1 


# if __name__ == '__main__':
#     test_dashes_inclass()
#     test_caps_inclass()


#"Barusand Holley adn Barus Holley and adn"
#{}