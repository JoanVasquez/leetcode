/*
 *Create a dummy node as a placeholder to simplify pointer handling.
Use a pointer tail that always refers to the end of the merged list.
While both lists are not empty:
    Compare the current values of list1 and list2.
    Attach the node with the smaller value to tail.next.
    Move forward in the list from which the node was taken.
    Update tail to the newly attached node.
When one list is exhausted, connect the remaining part of the other list to the merged result.
Return dummy.next as the head of the new merged list.
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  const dummy: ListNode | null = new ListNode(0, null);
  let tail: ListNode = dummy;

  while (list1 !== null && list2 !== null) {
    if (list1.val < list2.val) {
      tail.next = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      list2 = list2.next;
    }
    tail = tail.next;
  }

  if (list1 !== null) {
    tail.next = list1;
  }
  if (list2 !== null) {
    tail.next = list2;
  }

  return dummy.next;
}
