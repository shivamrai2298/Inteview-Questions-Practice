#important topics to cover which will help you clear media.net


ARRAYS / SLIDING WINDOW Question highest ROi
1. Longest subarray with sum ≤ K

(Positive numbers only – sliding window)

def longest_subarray_sum_leq_k(arr, k):
    left = 0
    curr_sum = 0
    max_len = 0

    for right in range(len(arr)):
        curr_sum += arr[right]

        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


Time: O(n)
Space: O(1)

2. Subarray sum equals K

(Handles negatives – prefix sum + hashmap)

def subarray_sum_k(arr, k):
    prefix_sum = 0
    seen = {0: 1}
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


Time: O(n)
Space: O(n)

3. Product of array except self

(No division)

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


Time: O(n)
Space: O(1) (output excluded)

STRINGS
4. Anagram check
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True


Time: O(n)
Space: O(1) (fixed alphabet)

5. Longest substring without repeating characters
def longest_unique_substring(s):
    seen = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


Time: O(n)
Space: O(n)

6. String compression
def compress_string(s):
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1

    result.append(s[-1] + str(count))
    return "".join(result)


Time: O(n)
Space: O(n)

STACK
7. Valid parentheses
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)

    return not stack


Time: O(n)
Space: O(n)

8. Next greater element
def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


Time: O(n)
Space: O(n)

9. Min Stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1]


All operations: O(1)

LINKED LIST
10. Detect cycle (Floyd’s Algorithm)
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


Time: O(n)
Space: O(1)

11. Reverse linked list (Iterative)
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

12. Reverse linked list (Recursive)
def reverse_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

TREES (BASIC)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

13. Inorder Traversal
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

14. Preorder Traversal
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

15. Height of tree
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

16. Lowest Common Ancestor (Binary Tree)
def lca(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    return left or right


Time: O(n)
Space: O(h)
