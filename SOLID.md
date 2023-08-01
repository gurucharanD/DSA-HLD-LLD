S:single responsibility principle

A class should have only one responsibility, further more it should have only one reason to change
this provides following benefits:
    testing: a class with one responsibility has far fewer test cases
    lower coupling: less functionality in a single class will have fewer dependencies
    easy to maintain as the surface area of change is small
    avoids code duplication
    easy to understand

consider a class that generates an invoice, with methods to calculate the price and save the invoice to datastore
this class is violating the single responsibility principle because it has more than one reason to change
if there is a change in the price calculation logic to include taxes the invoice class has to change
if there is a change in the save to datastore the invoice class has to change

to fix this we can move the price calculation and save to datastore methods to a different store
and use them in the invoice class, with this the invoice class will not have to change for every change 
______________________________________
O:open closed principle

A class should be open for extension but it should be closed for modification.
In other words a class that has been tested and deployed to production should not be modified

for example, consider a InvoiceDao class that has a method to save the invoice into a database
this class has been tested and deployed, later you want to add a method to this class to save
the invoice to a file. to implement this behaviour the easiest thing to do would be to add a new method
tothe InvoiceDao to save the invoice to file. this violates the open closed principle

to fix this, the best way is to create a InvoiceDao class with save method and the save to DB implementation will
extend this class, the save to file class will also implement the same
______________________________________
L:liskov substitution principle

if class B is a ssubtype of class A, then class A can be replaced by class B without breaking the behaviour of the program.

we can identify that there is a violation is Liskov substitution principle,

    if we are adding if conditions to check the type of an object and then make a decision to invoke the method or not. which implies that the subclass is not a direct substitue of parent class.This is forcing the high level class that is using these class to be aware of the internal implementations of these classes to make these exceptions
    which is violating abstraction principle

    return null or throw UnsupportedOperationException from a method is also sign of violation

https://github.com/Sunchit/Coding-Decoded/tree/master/SystemDesign/Lowlevel/Solid/LiskovSubstitutionPrinciple/src

______________________________________
I:interface segrigation principle

    Larger interfaces should be split into smaller interfaces. 
    by doing this can ensure that implementing classes only need to be concerned about the methods they are interested in

    consider a class Animal which has methods such as fly(), swim(), walk()
    if we want to create an instance of fish , we dont need fly and walk methods
    if we want to create an instane of bird, we dont need swim method
    if we want to create an instance of dog, we dont need fly and swim methods

    to fix this, we can break down the Animal interface into multiple interfaces each implementing a behaviour
    such as IWalkable, ISwimable, IFlyable and place the appropriate methods inside each of them
    and animals can implement which ever behaviour they want.
______________________________________
D:dependency inversion principle

    it states that high level modules should depend on the interfaces of the low level modules rather than
    depending on their concrete implementations.

    dependency injection helps us create loosely coupled high level and low level modules
    by providing abstraction for low level modules and all the dependencies of the high level modules
    are passed as arguments to the constructor instead of creating objects of the low level modules 
    in the code of the high level modules.

Example:
    consider a ShopingCartService which is a high level module which is dependent on a
low level module PaymentService and the payment service has various implementations
such as StripePaymentService, CreditCardPaymentService which are the concrete implementations.

    The PaymentService instead of depending on the concrete implementations should depend on 
the interface because of this loose coupling is established between the modules
and low level modules can be changed without changing the high level modules.

class ShoppingCartService {
    private paymentProcessor: PaymentProcessor;

    constructor(paymentProcessor: PaymentProcessor) {
        this.paymentProcessor = paymentProcessor;
    }

    public checkout(cart: Cart) {
        this.paymentProcessor.processPayment(cart);
    }
} 
const paymentProcessor = new PayPalPaymentProcessor();
const shoppingCartService = new ShoppingCartService(paymentProcessor);
______________________________________



