public class Solution {
    public bool IsValid(string s) {
        Dictionary<char, char> matchings = new Dictionary<char, char>();
        Stack<char> stack = new Stack<char>();

        matchings.Add(')', '(');
        matchings.Add(']', '[');
        matchings.Add('}', '{');

        foreach (char c in s) {
            if (matchings.ContainsKey(c)) {
                if (stack.Count() == 0 || matchings[c] != stack.Peek()) {
                    return false;
                } else {
                    stack.Pop();
                }
            } else {
                stack.Push(c);
            }
        }

        return stack.Count == 0;
    }
}
