public class MinStack {
    private Stack<int> stack = new Stack<int>();
    private Stack<int> min = new Stack<int>();

    public MinStack() {
    }

    public void Push(int val) {
        stack.Push(val);
        if (min.Count == 0 || val <= min.Peek()) {
            min.Push(val);
        }
    }

    public void Pop() {
        if (stack.Pop() == min.Peek()) {
            min.Pop();
        }
    }

    public int Top() {
        return stack.Peek();
    }

    public int GetMin() {
        return min.Peek();
    }
}
