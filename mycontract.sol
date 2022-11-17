pragma solidity 0.5.1;

contract MyContract{

    string value;
    bool public boolean = false;
    int public myInt = 8;
    uint public myUint = 8;
    uint16 public myuint16 = 45;
    enum State {waiting, ready, active}
    State public state = State.waiting;

    struct person{
        uint _id;
        string _firstName;
        string _lastName;
    }
    person[] public people;
    mapping(uint => person) public people1;
    uint public peopleCount = 0;

    address owner;  
    modifier onlyOwner(){
        // sends the address of the account
        // who called the function
        require(msg.sender == owner);
        _;
    }

    uint256 openingTime;
    modifier onlyWhileOpen(){
        require(block.timestamp >= openingTime );
        _;
    }

    mapping (address => uint256) public balances;
    address payable wallet;

    event purchase(
        address indexed _buyer,
        uint _amount
    );

    constructor(address payable _wallet) public{
        value = "myValue";
        owner = msg.sender;
        openingTime = 1768625700;
        wallet = _wallet;
    }

    function get() public view returns(string memory) {
        return value;
    }

    function set(string memory _value) public {
        value = _value;
    }

    function activate() public{
        state = State.active;
    }

    function isActive() public view returns(bool){
        return state == State.active;
    }

    function addPerson(string memory _firstName,string memory _lastName) public onlyOwner{
        incrementCount();
        people.push(person(peopleCount,_firstName,_lastName));
    }

    function addPerson1(string memory _firstName,string memory _lastName) public onlyWhileOpen{
        incrementCount();
        people1[peopleCount] = person(peopleCount,_firstName,_lastName);
    }

    function incrementCount() internal{
        peopleCount += 1;
    }

    function() external payable{
        buyToken();
    }

    function buyToken() public payable{
        // buy one token 
        balances[msg.sender] += 1;
        // send ether to a wallet
        wallet.transfer(msg.value);
        emit purchase(msg.sender,1);
    }



}