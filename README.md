# leetcode-collection

* [Single Number](single_number.py)
  * Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.

* [Happy Number](happy_number.py)
  * Write an algorithm to determine if a number `n` is "happy".
  * A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1. Those numbers for which this process **ends in 1** are happy numbers.
  * Return True if `n` is a happy number, and False if not.

* [Maximum Subarray](maximum_subarray.py)
  * Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

* [Move Zeroes](move_zeroes.py)
  * Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

* [Best Time to Buy and Sell Stock II](stock_buy_sell.py)
  * Say you have an array `prices` for which the ith element is the price of a given stock on day i.
  * Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
  * Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

* [Group Anagrams](group_anagrams.py)
  * Given an array of strings, group anagrams together.

* [Counting Elements](count_element.py)
  * Given an integer array `arr`, count element `x` such that `x + 1` is also in `arr`.
  * If there're duplicates in `arr`, count them seperately.
  
* [Middle of the Linked List](middle_linked_list.py)
  * Given a non-empty, singly linked list with head node `head`, return a middle node of linked list.
  * If there are two middle nodes, return the second middle node.

* [Backspace String Compare](backspace_string_compare.py)
  * Given two strings `S` and `T`, return if they are equal when both are typed into empty text editors. `#` means a backspace character.

* [Min Stack](min_stack.py)
  * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
  
* [Diameter of Binary Tree](diameter_of_binary_tree.py)
  * Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest** path between any two nodes in a tree. This path may or may not pass through the root.
  * The length of path between two nodes is represented by the number of edges between them.
  
* [Last Stone Weight](last_stone_weight.py)
  * We have a collection of stones, each stone has a positive integer weight.
  * Each turn, we choose the two **heaviest** stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:
    * If `x == y`, both stones are totally destroyed;
    * If `x != y`, the stone of weight `x` is totally destroyed, and the stone of weight `y` has new weight `y-x`.
  * At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

* [Contiguous Array](contiguous_array_equal_0_1.py)
  * Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

* [Perform String Shifts](string_shift.py)
  * You are given a string `s` containing lowercase English letters, and a matrix `shift`, where `shift[i] = [direction, amount]`:
    * `direction` can be `0` (for left shift) or `1` (for right shift). 
    * `amount` is the amount by which string `s` is to be shifted.
    * A left shift by 1 means remove the first character of `s` and append it to the end.
    * Similarly, a right shift by 1 means remove the last character of `s` and add it to the beginning.
  * Return the final string after all operations.

* [Product of Array Except Self](prod_of_arr_except_self.py)
  * Given an array `nums` of n integers where n > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
  * Please solve it **without division** and in O(n) with constant space complexity.

* [Valid Parenthesis String](valid_paren_str.py)
  * Given a string containing only three types of characters: `'('`, `')'` and `'*'`, write a function to check whether this string is valid. We define the validity of a string by these rules:
    1. Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
    2. Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
    3. Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
    4. `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string.
    5. An empty string is also valid.

* [Number of Islands](num_of_islands.py)
  * Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
