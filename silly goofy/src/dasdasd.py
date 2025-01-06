"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sushant Sah
ID:            169060628
Email:    sahx0628@mylaurier.ca
__updated__ = "2024-04-23"
-------------------------------------------------------
"""
# Imports

# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy
from Priority_Queue_linked import Priority_Queue


class Queue:
    """
    A linked Queue class.
    """

    def to_priority_queue(self):
        """
        ---------------------------------------------------------
        Converts a linked Queue to a linked Priority Queue by moving all nodes
        to a new Priority Queue. source is empty when finished.
        Use: pq = source.to_priority_queue()
        ---------------------------------------------------------
        Parameters:
            None
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            pq - a linked Priority Queue. (Priority_Queue)
        ---------------------------------------------------------
        """

        pq = Priority_Queue()
        while self._front is not None:
            node = self._front
            self._front = self._front._next
            pq._move_node(node)
        
        return pq

    
    def sum_consecutive(self):
        """
        ---------------------------------------------------------
        Sums consecutive equal elements and replaces them with that sum.
        Use: queue.sum_consecutive()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​‌​‌​‌‌‌​‌‌:
            None
        ---------------------------------------------------------
        """

        if self._front is None:
            pass

        
        current = self._front
        next = self._front._next
        #sum_count = 1
        #total_sum = current._value


        while next is not None:
            if current._value == next._value:
                current._value += next._value
                current._next = next._next
                if next._next == self._rear:
                    self._rear = current
                    current_next = None
                next = next._next
            else:
                current = next 
                next = next._next
                    
        #while current._next is not None:
         #   if current._value == current._next._value:
          #      sum_count += 1
           #     total_sum += current._next._value
            #else:
                #if sum_count > 1:
              #      if prev is None:
                #        self._front = _Queue_Node(total_sum, current._next)
                 #   else:
                  #      prev._next = _Queue_Node(total_sum, current._next)
                    #total_sum = current._next._value
                    #sum_count = 1
                #else:
                    #prev = current
                    #total_sum = current._next._value
                    #sum_count = 1

            #current = current._next

        #if sum_count > 1:
            #if prev is None:
            #    self._front = _Queue_Node(total_sum, None)
            #else:
                #prev._next = _Queue_Node(total_sum, None)

        return

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        ---------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            a new Queue object (Queue)
        ---------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        node = _Queue_Node(value, None)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _Queue_Node:
    """
    A linked Queue Node class.
    """

    def __init__(self, value, next_):
        """
        ---------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        ---------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            a new _Queue_Node object (_Queue_Node)
        ---------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        
        
        
        
        
        
        
        
    #2 
    # pylint: disable=W0212
    # pylint: disable=E2515
    # pylint: disable=E0303
    # pylint: disable=W0613
    # pylint: disable=E1128
    
    # Imports
    from copy import deepcopy
    
    
    class Priority_Queue:
        """
        A linked Priority Queue class.
        """
    
        def _move_node(self, node):
            """
            -------------------------------------------------------
            Moves node into source at the correct position.
            Use: source._insert_node(source)
            -------------------------------------------------------
            Parameters:
                node - a linked node (PQ_Node / Stack_Node / Queue_Node / List_Node)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                None
            -------------------------------------------------------
            """
    
            if self._front is None or node._value < self._front._value:
                node._next = self._front
                self._front = node
            else:
                first = self._front
                while first._next is not None and first._next._value <= node._value:
                    first = first._next
                node._next = first._next
                first._next = node
            self._count += 1
    
            return
    
    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================
    
        def __init__(self):
            """
            -------------------------------------------------------
            Initializes an empty priority queue.
            Use: pq = Priority_Queue()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                a new Priority_Queue object (Priority_Queue)
            -------------------------------------------------------
            """
            self._front = None
            self._rear = None
            self._count = 0
    
        def is_empty(self):
            """
            -------------------------------------------------------
            Determines if the priority queue is empty.
            Use: b = pq.is_empty()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                True if priority queue is empty, False otherwise.
            -------------------------------------------------------
            """
            return self._front is None
    
        def insert(self, value):
            """
            -------------------------------------------------------
            A copy of value is inserted into the priority queue.
            Values are stored in priority order.
            Use: pq.insert(value)
            -------------------------------------------------------
            Parameters:
                value - a data element (?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                None
            -------------------------------------------------------
            """
            if self._front is None:
                # Priority queue is empty
                node = _PQ_Node(value, None)
                self._front = node
                self._rear = node
            elif value < self._front._value:
                # New value has highest priority
                self._front = _PQ_Node(value, self._front)
            elif value >= self._rear._value:
                # New value has lowest priority
                node = _PQ_Node(value, None)
                self._rear._next = node
                self._rear = node
            else:
                # Find the proper position for value.
                prev = None
                curr = self._front
    
                while value >= curr._value:
                    prev = curr
                    curr = curr._next
    
                # Create the new node and link it to curr.
                # The previous node is linked to the new node.
                prev._next = _PQ_Node(value, curr)
            # Increment the priority queue size.
            self._count += 1
            return
    
        def __iter__(self):
            """
            USE FOR TESTING ONLY
            -------------------------------------------------------
            Generates a Python iterator. Iterates through the queue
            from front to rear.
            Use: for value in pq:
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                value - the next value in the priority queue (?)
            -------------------------------------------------------
            """
            curr = self._front
    
            while curr is not None:
                yield curr._value
                curr = curr._next
    
    
    class _PQ_Node:
        """
        A linked Priority Queue Node class.
        """
    
        def __init__(self, value, _next):
            """
            -------------------------------------------------------
            Initializes a priority queue node that contains a copy of value
            and a link to the next node in the priority queue
            Use: node = _PQ_Node(value, _next)
            -------------------------------------------------------
            Parameters:
                value - value value for node (?)
                _next - another priority queue node (_PQ_Node)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                a new Priority_Queue object (_PQ_Node)
            -------------------------------------------------------
            """
            self._value = deepcopy(value)
            self._next = _next
            
            
            #BST LINKED 
            
            
    class BST:
        """
        A linked BST class.
        """
    
        def are_siblings(self, v1, v2):
            """
            -------------------------------------------------------
            Determines if nodes containing values v1 and v2 are siblings.
            Nodes are siblings if they have the same parent.
            Use: b = source.are_siblings(v1, v2)
            -------------------------------------------------------
            Parameters:
                v1 - a node value (*)
                v2 - a node value (*)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                siblings - True if the nodes containing v1 and v2 are siblings,
                    False otherwise.
            -------------------------------------------------------
            """
            siblings = self._are_siblings_aux(self._root, v1, v2)
            return siblings
    
        def _are_siblings_aux(self, parent, v1, v2):
            """
            -------------------------------------------------------
            Determines if nodes containing values v1 and v2 are siblings.
            Nodes are siblings if they have the same parent.
            Use: siblings = self._are_siblings_aux(parent, v1, v2)
            -------------------------------------------------------
            Parameters:
                parent - a potential parent of nodes containing v1 and v2 (_BST_Node)
                v1 - a node value (*)
                v2 - a node value (*)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                siblings - True if the nodes containing v1 and v2 are siblings,
                    False otherwise.
            -------------------------------------------------------
            """
    
            if parent is None:
                siblings = False
            elif (parent._left and parent._left._value == v1 and parent._right and parent._right._value == v2) or \
                    (parent._left and parent._left._value == v2 and parent._right and parent._right._value == v1):
                siblings = True
            elif v1 < parent._value and v2 < parent._value:
                siblings = self._are_siblings_aux(parent._left, v1, v2)
            elif v1 > parent._value and v2 > parent._value:
                siblings = self._are_siblings_aux(parent._right, v1, v2)
            else:
                siblings = False
            return siblings
    
    
        def longest_path(self):
            """
            ---------------------------------------------------------
            Returns the values in the longest path of source. If there are multiple
            paths of the same maximum length, return the leftmost path.
            Returns an empty list if source is empty.
            Use: path = source.longest_path()
            ---------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                path - a list of values of the longest path from 
                    root to the leaves of source (list of *)
            ---------------------------------------------------------
            """
            path = self._longest_path_aux(self._root)
            #if self._root is not None:
            #    path += self._longest_path_aux(self._root, path)
            return path
    
        def _longest_path_aux(self, node):
            """
            ---------------------------------------------------------
            Returns a list of the values in the longest path from node to the
            leaves of self.
            Private auxiliary method for max_path.
            Use: path = self._longest_path_aux(node)
            ---------------------------------------------------------
            Parameters:
                node - a BST node (_BST_Node)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                path - a list of the values in the longest path from node
                    to the leaves of self (list of *)
            ---------------------------------------------------------
            """
            path = []
            if node is None:
                path = []
            else:
                path = [node._value]
                left = self._longest_path_aux(node._left)
                right = self._longest_path_aux(node._right)
                
                if len(left) >= len(right):
                    path += left
                else:
                    path += right
            
                    
            return path
        def __len__(self):
            return self._count
        def furthest(self):
            """
            -------------------------------------------------------
            Returns the values of the left-most and right-most nodes in source.
            Use: values = source.furthest()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                values - the values in the left-most and right-most nodes,
                    in that order, an empty list if the bst is empty (list of *)
            -------------------------------------------------------
            """
            #values = []
            #right = self._root
            #left = self._root
            #if self._count == 1:
            #    values.append(self._root._value)
            #elif self._count != 0:
            #    while left._left is not None:
            #        left = left._left
            #    values.append(left._value)
            #    while right._right is not None:
            #        right = right._right
            #    values.append(right._value)
            values = []
            if self._root is not None:
                left = self._root
                right = self._root
                while left is not None and left._left is not None:
                    left = left._left
                while right is not None and right._right is not None:
                    right = right._right
                values = [left._value,right._value]
            else:
                values = []
            return values
        # DO NOT CHANGE CODE BELOW THIS LINE
        # =======================================================================
    
        def __init__(self):
            """
            -------------------------------------------------------
            Initializes an empty BST.
            Use: bst = BST()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                A BST object (BST)
            -------------------------------------------------------
            """
            self._root = None
            self._count = 0
    
        def is_empty(self):
            """
            -------------------------------------------------------
            Determines if bst is empty.
            Use: b = bst.is_empty()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                True if bst is empty, False otherwise.
            -------------------------------------------------------
            """
            return self._root is None
    
        def insert(self, value):
            """
            -------------------------------------------------------
            Inserts a copy of value into bst. Values may appear
            only once in a tree.
            Use: b = bst.insert(value)
            -------------------------------------------------------
            Parameters:
                value - data to be inserted into bst (?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                inserted - True if value is inserted into bst,
                    False otherwise. (boolean)
            -------------------------------------------------------
            """
            self._root, inserted = self._insert_aux(self._root, value)
            return inserted
    
        def _insert_aux(self, node, value):
            """
            -------------------------------------------------------
            Inserts a copy of value into node.
            Private recursive operation called only by insert.
            Use: node, inserted = self._insert_aux(node, value)
            -------------------------------------------------------
            Parameters:
                node - a bst node (_BST_Node)
                value - data to be inserted into the node (?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                node - the current node (_BST_Node)
                inserted - True if value is inserted into node,
                    False otherwise. (boolean)
            -------------------------------------------------------
            """
            if node is None:
                # Base case: add a new node containing the value.
                node = _BST_Node(value)
                self._count += 1
                inserted = True
            elif value < node._value:
                # General case: check the left subtree.
                node._left, inserted = self._insert_aux(node._left, value)
            elif value > node._value:
                # General case: check the right subtree.
                node._right, inserted = self._insert_aux(node._right, value)
            else:
                # Base case: value is already in the BST.
                inserted = False
    
            if inserted:
                # Update the node height if any of its children have been changed.
                node._update_height()
            return node, inserted
    
        def retrieve(self, key):
            """
            -------------------------------------------------------
            Retrieves a copy of a value matching key in bst. (Iterative)
            Use: v = bst.retrieve(key)
            -------------------------------------------------------
            Parameters:
                key - data to search for (?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                value - value in the node containing key, otherwise None (?)
            -------------------------------------------------------
            """
            node = self._root
            value = None
    
            while node is not None and value is None:
    
                if node._value > key:
                    node = node._left
                elif node._value < key:
                    node = node._right
                elif node._value == key:
                    # for comparison counting
                    value = deepcopy(node._value)
            return value
    
        def inorder(self):
            """
            -------------------------------------------------------
            Generates a list of the contents of the tree in inorder order.
            Use: a = bst.inorder()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                a - copy of the contents of the tree in inorder (list of ?)
            -------------------------------------------------------
            """
            a = []
            self._inorder_aux(self._root, a)
            return a
    
        def _inorder_aux(self, node, a):
            """
            ---------------------------------------------------------
            Traverses node subtree in inorder. a contains the contents of
            node and its children in inorder.
            Private recursive operation called only by inorder.
            Use: self._inorder_aux(node, a)
            ---------------------------------------------------------
            Parameters:
                node - an BST node (_BST_Node)
                a - target list of data (list of ?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                None
            ---------------------------------------------------------
            """
            if node is not None:
                self._inorder_aux(node._left, a)
                a.append(deepcopy(node._value))
                self._inorder_aux(node._right, a)
            return
    
        def preorder(self):
            """
            -------------------------------------------------------
            Generates a list of the contents of the tree in preorder order.
            Use: a = bst.preorder()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                a - copy of the contents of the tree in preorder (list of ?)
            -------------------------------------------------------
            """
            a = []
            self._preorder_aux(self._root, a)
            return a
    
        def _preorder_aux(self, node, a):
            """
            ---------------------------------------------------------
            Traverses node subtree in preorder. a contains the contents of
            node and its children in preorder.
            Private recursive operation called only by preorder.
            Use: self._preorder_aux(node, a)
            ---------------------------------------------------------
            Parameters:
                node - an BST node (_BST_Node)
                a - target of data (list of ?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                None
            ---------------------------------------------------------
            """
            if node is not None:
                a.append(deepcopy(node._value))
                self._preorder_aux(node._left, a)
                self._preorder_aux(node._right, a)
            return
    
        def postorder(self):
            """
            -------------------------------------------------------
            Generates a list of the contents of the tree in postorder order.
            Use: a = bst.postorder()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                a - copy of the contents of the tree in postorder (list of ?)
            -------------------------------------------------------
            """
            a = []
            self._postorder_aux(self._root, a)
            return a
    
        def _postorder_aux(self, node, a):
            """
            ---------------------------------------------------------
            Traverses node subtree in postorder. a contains the contents of
            node and its children in postorder.
            Private recursive operation called only by postorder.
            Use: self._postorder_aux(node, a)
            ---------------------------------------------------------
            Parameters:
                node - an BST node (_BST_Node)
                a - target of data (list of ?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                None
            ---------------------------------------------------------
            """
            if node is not None:
                self._postorder_aux(node._left, a)
                self._postorder_aux(node._right, a)
                a.append(deepcopy(node._value))
            return
    
        def levelorder(self):
            """
            -------------------------------------------------------
            Copies the contents of the tree in levelorder order to a list.
            Use: values = bst.levelorder()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                values - a list containing the values of bst in levelorder.
                (list of ?)
            -------------------------------------------------------
            """
            values = []
    
            if self._root is not None:
                # Put the nodes for one level into a queue.
                queue = []
                queue.append(self._root)
    
                while len(queue) > 0:
                    # Add a copy of the data to the sublist
                    node = queue.pop(0)
                    values.append(deepcopy(node._value))
    
                    if node._left is not None:
                        queue.append(node._left)
                    if node._right is not None:
                        queue.append(node._right)
            return values
    
        def __iter__(self):
            """
            -------------------------------------------------------
            Generates a Python iterator. Iterates through a BST node
            in level order.
            Use: for v in bst:
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                yields
                value - the values in the BST node and its children (?)
            -------------------------------------------------------
            """
            if self._root is not None:
                # Put the nodes for one level into a queue.
                queue = []
                queue.append(self._root)
    
                while len(queue) > 0:
                    # Add a copy of the data to the sublist
                    node = queue.pop(0)
                    yield node
                    # yield node._value
    
                    if node._left is not None:
                        queue.append(node._left)
                    if node._right is not None:
                        queue.append(node._right)
    
    
    class _BST_Node:
        """
        A linked BST Node class.
        """
    
        def __init__(self, value):
            """
            -------------------------------------------------------
            Initializes a BST node containing value. Child pointers
            are None, height is 1.
            Use: node = _BST_Node(value)
            -------------------------------------------------------
            Parameters:
                value - value for the node (?)
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                A _BST_Node object (_BST_Node)
            -------------------------------------------------------
            """
            self._value = deepcopy(value)
            self._left = None
            self._right = None
            self._height = 1
            self._count = 0
    
        def _update_height(self):
            """
            -------------------------------------------------------
            Updates the height of the current node. _height is 1 plus
            the maximum of the node's (up to) two child heights.
            Use: node._update_height()
            -------------------------------------------------------
            Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
                None
            -------------------------------------------------------
            """
            if self._left is None:
                left_height = 0
            else:
                left_height = self._left._height
    
            if self._right is None:
                right_height = 0
            else:
                right_height = self._right._height
    
            self._height = max(left_height, right_height) + 1
            return
    
        def __str__(self):
            """
            USE FOR TESTING ONLY
            -------------------------------------------------------
            Returns node height and value as a string - for debugging.
            -------------------------------------------------------
            """
            return f"h: {self._height}, v: {self._value}"
            
            
            
            
            #Deque linked 
            """
# Imports

# Constants


# Imports
from copy import deepcopy
from pickle import NONE


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        if self._front is None:
            yes = True 
        else:
            yes = False 
            
        return yes 

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals = True 
        if self._count != target._count:
            equals = False
        if equals == True:
            current = self._front 
            tar_curr = target._front 
            while current is not None and tar_curr is not None:
                if current._value != tar_curr._value:
                    equals = False 
                current = current._next 
                tar_curr = tar_curr._next
                
        return equals

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _Deque_Node(value,None,self._front)
        if self._front is None:
            self._front = node 
            self._rear = node 
        else:
            self._front = node 
        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _Deque_Node(value,self._rear,None)
        if self._front is None:
            self._front = node 
            self._rear = node 
        else:
            self._rear._next = node 
        self._rear = node 
        self._count +=1 
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"
        
        # your code here
        value = self._front._value
        self._front = self._front._next
        self._count -= 1
        if self._front is not None:
            self._front._prev = None
        if self._front is None:
            self._rear = None
            self._count = 0
        return value
        #return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        # your code here
        if self._rear is not None:
            value = self._rear._value
            self._rear = self._rear._prev
            self._count -= 1
            if self._rear is not None:
                self._rear._next = None
            if self._rear is None:
                self._front = None
                self._count = 0
            
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        # your code here
        value = deepcopy(self._front._value)
        
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        # your code here
        value = deepcopy(self._rear._value)
        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
            
            
        
        #list linked
        
        # pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class List:
    """
    A linked List class.
    """

    def pair_count(self):
        """
        -------------------------------------------------------
        Returns the number of pairs of values (values that are adjacent
        to each other) in source.
        Use: source.pair_count(n)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            pairs - the number of pairs in source (int >= 0)
        -------------------------------------------------------
        """
        pairs = 0
        second = self._front
        first = self._front._next
        while first is not None and second is not None:
            if second._value == first._value:
                pairs += 1
            second = first
            first = first._next
        return pairs
    

    def rotate_front(self):
        """
        -------------------------------------------------------
        Moves the front node to the rear of the List.
        Use: source.rotate_front()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            None
        -------------------------------------------------------
        """
        if not self.is_empty():
            self._count -= 1
            x = self._front
            self._front = self._front._next
            a = self._front is None
            if a:
                self._rear = None
            b = self._rear is None
            if b:
                self._front = x
            else:
                self._rear._next = x
            x._next = None
            self._rear = x
            self._count += 1
        return
    
    

    def rotate_rear(self):
        """
        -------------------------------------------------------
        Moves the rear node to the front of the List.
        Use: source.rotate_rear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            None
        -------------------------------------------------------
        """
        if self._front is not None and self._front is not self._rear:
            curr_node = self._front
            while curr_node._next is not self._rear:
                curr_node = curr_node._next
            self._rear._next = self._front
            self._front = self._rear
            self._rear = curr_node
            self._rear._next = None
        return


    def has_loop(self):
        """
        -------------------------------------------------------
        Determines if source contains a circular reference/loop.
        Use: loop = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            loop - True if source contains a circular reference,
                False otherwise (bool)
        -------------------------------------------------------
        """
        if self._front is None:
            return False
        a = self._front
        b = self._front
        while b is not None and b._next is not None:
            a = a._next
            b = b._next._next
            if a == b:
                return True
        return False


    def remove_loop(self):
        """
        -------------------------------------------------------
        Locates and removes any loop in the list. The rear node is preserved.
        Use: source.remove_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            None
        -------------------------------------------------------
        """

        # Check if there is a loop
        if self.has_loop():
            # Initialize two pointers
            slow = self._front
            fast = self._front
    
            # Detect the meeting point which is in the loop
            while fast and fast._next:
                slow = slow._next
                fast = fast._next._next
                if slow == fast:
                    break
    
            # Find the start of the loop
            slow = self._front
            while slow != fast:
                prev = fast  # Keep track of the node before the meeting point
                slow = slow._next
                fast = fast._next
    
            # prev now points to the node before the start of the loop
            # Disconnect the loop
            prev._next = None

        return


# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns‌​‌​​​​‌​​‌‌​‌‌​​​​‌​​​​‌​‌‌:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_