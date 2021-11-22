# https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%ED%86%A0%ED%83%80%EC%9E%85_%ED%8C%A8%ED%84%B4#Python

from copy import copy, deepcopy

# create another instance, w/state, of an existing instance of unknown class/state
class Graphic:
    will_be_copied = 1
    only_copied_at_deep = []
    def clone(self):
        return copy(self)

def main():
    g = Graphic() # non-cooperative form
    g.only_copied_at_deep = [1]

    shallow_copy_of_g = copy(g)
    shallow_copy_of_g.will_be_copied = 2
    shallow_copy_of_g.only_copied_at_deep.append(2)
    
    deep_copy_of_g = deepcopy(g)
    deep_copy_of_g.will_be_copied = 3
    deep_copy_of_g.only_copied_at_deep.append(3)

    print(g.will_be_copied, shallow_copy_of_g.will_be_copied, deep_copy_of_g.will_be_copied) # 1 2 3
    print(g.only_copied_at_deep, shallow_copy_of_g.only_copied_at_deep, deep_copy_of_g.only_copied_at_deep) # [1, 2] [1, 2] [1, 2, 3]

    
    g = Graphic() # cooperative form
    
    copy_of_g = g.clone()
    copy_of_g.will_be_copied = 2
    
    print(g.will_be_copied, copy_of_g.will_be_copied) # 1 2

if __name__ == "__main__":
    main()
