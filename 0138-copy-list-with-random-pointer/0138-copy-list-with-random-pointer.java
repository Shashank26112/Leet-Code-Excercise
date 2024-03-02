import java.util.HashMap;
import java.util.Map;
class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> nodeMap = new HashMap<>();
        nodeMap.put(null, null);
        Node current = head;
        if (current == null) {
            return null;
        }
        while (current != null) {
            Node copy = new Node(current.val);
            nodeMap.put(current, copy);
            current = current.next;
        }
        current = head;
        while (current != null) {
            Node newCurrent = nodeMap.get(current);
            newCurrent.next = nodeMap.get(current.next);
            if (current.random != null) {
                newCurrent.random = nodeMap.get(current.random);
            }
            current = current.next;
        }
        return nodeMap.get(head);
    }
}