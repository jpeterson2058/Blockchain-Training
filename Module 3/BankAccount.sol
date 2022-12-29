pragma solidity ^0.5.0;

contract BankAccount {
    address payable accountOwner = 0x838B260B95e04ff23D5066B9af0211E683539F2F;

    function withdraw(uint amount, address payable recipient) public {
        require(recipient == accountOwner, "You don't own this account homeslice!");
            return recipient.transfer(amount);   
    }

    function deposit() public payable{}

    function() external payable {}
}
