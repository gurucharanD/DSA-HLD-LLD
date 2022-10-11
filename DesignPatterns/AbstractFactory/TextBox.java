package DesignPatterns.AbstractFactory;

interface TextBox {
    public void printText();
}

class MacTextBox implements TextBox {
    public void printText() {
        System.out.println("print text from mac textbox");
    }
}

class WinTextBox implements TextBox {
    public void printText() {
        System.out.println("print text from win textbox");
    }
}