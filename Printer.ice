module Demo {
    interface Printer {
        void printString(string s);
        string toUpperCase(string s);
        int countCharacters(string s);
    }

    interface Calculator {
        int add(int a, int b);
        int multiply(int a, int b);
    }
}
