class Node:
    def __init__(self, val):
        self.val = val

class ThreeInOne:
    def __init__(self):
        self.array = [None]*60
        self.length = 60
        self.stacks = [0, 20, 40]
        self.stack_size = [0,0,0]
        self.expand = 1
    def push(self, item, stack):
        if stack > 3 or stack < 1:
            return
        if self.stack_size[stack-1]<self.length//3:
            node = Node(item)
            self.array[self.stacks[stack-1]] = node
            self.stacks[stack-1] += 1
            self.stack_size[stack-1] += 1
        else:
            prev_len = self.length
            self.expand *= 2
            self.length = self.expand*60
            new_array = [None]*self.length
            for i in range(prev_len//3):
                new_array[i] = self.array[i]
                new_array[self.length//3+i] = self.array[prev_len//3+i]
                new_array[self.length*2//3+i] = self.array[prev_len*2//3+i]
            array = self.array
            for i in range(len(self.stack_size)):
                self.stacks[i] = self.length*i//3+self.stack_size[i]
            self.array = new_array
            del array
            self.push(item, stack)
    def pop(self, stack):
        if stack > 3 or stack < 1:
            return
        if self.stack_size[stack-1]<1:
            return
        node = self.array[self.stacks[stack-1]-1]
        self.array[self.stacks[stack-1]-1] = None
        self.stacks[stack-1] -= 1
        self.stack_size[stack-1] -= 1
        return node
    def peek(self, stack):
        if stack > 3 or stack < 1:
            return
        if not self.is_empty(stack):
            return self.array[self.stacks[stack-1]-1]
        else:
            return
    def is_empty(self, stack):
        if stack > 3 or stack < 1:
            return
        if self.stack_size[stack-1]<1:
            return True
        else:
            return False
    def print_stack(self, stack):
        if stack > 3 or stack < 1:
            return
        temp = self.array[(stack-1)*self.expand*20:stack*self.expand*20]
        string = ''
        for node in range(len(temp)-1):
            if temp[node]:
                string += str(temp[node].val)+'|'
            else:
                string += 'None|'
        if temp[-1]:
            string += str(temp[-1].val)
        else:
            string += 'None'
        print(string)

