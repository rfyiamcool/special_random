# special_random

一个有权重功能的随机模块

```
import special_random

class BasicClass(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __repr__(self):
        return str(self.name)

ll = []
ll.append(BasicClass("xiaogang", 40))
ll.append(BasicClass("aiyu", 30))
ll.append(BasicClass("dehua", 20))
ll.append(BasicClass("yueyue", 10))

choosen_one = special_random.choice(ll, lambda x: x.weight)
print choosen_one


ll = ["xiaogang", "aiyu", "dehua", "zhilin"]

print special_random.shuffle(ll, weight_key=lambda x: len(x))

sample = [1, 2, 3, 4]

print special_random.sample(sample, weight_key=lambda x: x)
```
