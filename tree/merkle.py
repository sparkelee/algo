#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib
import os
import Queue

class Node:
    #node_cnt = 0
    def __init__(self, hash_code='', left=None, right=None, begin=0, end=0):
        self.hash_code = hash_code
        self.left = left
        self.right = right
        self.level = 1
        self.begin = begin
        self.end = end
        if left != None:
            if right != None:
                self.hash_code = calc_hash(left.hash_code + right.hash_code)
            else:
                self.hash_code = calc_hash(left.hash_code)
            self.level = left.level + 1
        #node_cnt += 1


def calc_hash(content):
    md5 = hashlib.md5()
    md5.update(content)
    return md5.hexdigest()

def create_merkle_tree(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    p_list = []
    i = 0
    while i < len(list):
        if i+1 == len(list):
            p_node = Node(left=list[i])
        else:
            p_node = Node(left=list[i], right=list[i+1])
        p_list.append(p_node)
        i += 2
    return create_merkle_tree(p_list)


def traverse_merkle_tree(node):
    q = Queue.Queue()
    q.put(node)
    while q.empty() is False:
        n = q.get()
        # print n.hash_code, n.level, n.left, n.right
        if n.left != None:
            q.put(n.left)
        if n.right != None:
            q.put(n.right)

def build_merkle_from_file(file_path):
    leaf_list = []
    with open(file_path, 'rb') as f:
        begin = 0
        end = 10240
        while end - begin >= 10240:
            content = f.read(10240)
            leaf_list.append(Node(calc_hash(content), begin = begin, end = begin + len(content)))
            begin = end
            end = len(content) + begin
    # if len(leaf_list) % 2 != 0:
    #     leaf_list.append(Node(leaf_list[-1].hash_code))
    root = create_merkle_tree(leaf_list)
    print file_path, root.hash_code
    return root

# two MT has same height and leaf node
def traverse_and_diff(root1, root2, diff_leaf_list):
    if root1.hash_code == root2.hash_code:
        return
    if root1.level == 1 and root2.level == 1:
        print root1.hash_code, root1.level, root2.hash_code, root2.level, root1.begin, root1.end
        diff_leaf_list.append(root1)
    if root1.left != None and root2.left != None:
        traverse_and_diff(root1.left, root2.left, diff_leaf_list)
    if root1.right != None and root2.right != None:
        traverse_and_diff(root1.right, root2.right, diff_leaf_list)


def main():
    root1 = build_merkle_from_file('test1.file')
    root2 = build_merkle_from_file('test2.file')
    diff_leaf_list = []
    traverse_and_diff(root1, root2, diff_leaf_list)
    for diff_leaf in diff_leaf_list:
        f1 = open('test1.file', 'rb')
        f2 = open('test2.file', 'rb')
        f1.seek(diff_leaf.begin, 0)
        f2.seek(diff_leaf.begin, 0)
        content1 = f1.read(10240)
        content2 = f2.read(10240)
        for idx in range(len(content1)):
            if content1[idx] != content2[idx]:
                print "%x %x offset:%d" % (ord(content1[idx]), ord(content2[idx]), diff_leaf.begin + idx)

if __name__ == '__main__':
    main()
