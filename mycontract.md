Solidity: 

memory is a keyword used to store data for the execution of a contract. 
It holds functions argument data and is wiped after execution. storage can be seen as the default solidity data storage. 
It holds data persistently and consumes more gas.


<!-- DataTypes in solidity -->

string
int => can have both + and - values
uint => can only have + values
bool    
address => used to store the address of the account

string value;
bool public boolean = false;
int public myInt = 8;
uint public myUint = 8;
uint16 public myuint16 = 45;
we can also specify the number of bits or bytes using uint8

<!-- // enums  -->
enum State {waiting, ready, active}
State public state = State.waiting;

<!-- // structs -->
structs are a way for you to define your own datatypes in solidity
and model our arbitrary data

struct person{
    string _firstName;
    string _lastName;
}
person[] public people;

people is an array of type person

// mapping is another datastructure
// that works like an associative array
// it is similar to hashMap where data 
// is stored in the from of key value pairs

<!-- // access modifiers -->
public 
internal
we can create custom access modifiers by defining our own rules and attach it to a function
example: onlyOwner -> only the owner of the smart contract can run the function

modifier onlyOwner(){
    // sends the address of the account
    // who called the function
    require(msg.sender == owner);
    _;
}

<!-- // time in solidity ->  -->
timestamps are expressed in seconds in solidity i.e epoch seconds
lets assume we allow the execution of a
function only when a certain time has passed
we can create another access modifier for this
lets call it onlyWhileOpen


// create a function that accepts ether as input
payable modifier
fallback function 

<!-- // events in solidity -->
events are a way for external consumers to listen
to what is happening inside smart contract
indexed keyword

<!-- Realtionship between smart contracts -->
