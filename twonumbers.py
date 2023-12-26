# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        parsedinput1 = []
        parsedinput2 = []

        while l1 != None:
            parsedinput1.insert(0, l1.val)
            l1 = l1.next

        while l2 != None:
            parsedinput2.insert(0, l2.val)
            l2 = l2.next

        parsedstring1 = "".join([str(x) for x in parsedinput1])
        parsedinput1 = int(parsedstring1)

        parsedstring2 = "".join([str(y) for y in parsedinput2])
        parsedinput2 = int(parsedstring2)

        answer = parsedinput1 + parsedinput2

        answer = str(answer)

        answer = list(answer)

        print(answer)
        finalreturn = ListNode()

        index = ListNode()
        index = finalreturn

        for i in range(0, len(answer), 1):
            index.val = answer[len(answer) - i - 1]

            if len(answer) - 1 != i:
                tempnode = ListNode()

                index.next = tempnode
                index = tempnode

        return finalreturn

        print(parsedinput1)
