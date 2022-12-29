pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner;
    bool isNewAccount;
    uint public accountBalance;
    string customerName;
    string customerLastName;

    function getInfo() view public returns(address, bool, uint, string memory, string memory) {
        return(owner, isNewAccount, accountBalance, customerName, customerLastName);

    }

    function setInfo(address newOwner, bool newAccountStatus, uint newAccountBalance, string memory newCustomerName, string memory newCustomerLastName) public {
        owner = newOwner;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;

    }

    function sendRemittance(uint amount, address payable recipient) public {
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function() external payable {}
}
