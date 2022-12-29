pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
    bool isNewAccount = true;
    uint accountBalance = 50000;
    string customerName = "Buddy";
    string customerLastName = "Elf";

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
}
