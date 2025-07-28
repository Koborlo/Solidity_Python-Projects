// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import{getConvertor} from "./PriceConvertor.sol";
error notOwner();
contract FundMe {
    using getConvertor for uint256;
    uint256 constant MINIMUM_USD = 5e18; 
    address[] public Funders;
    mapping(address => uint256) public addresstoFunders;
    address immutable i_owner;
    constructor() {
        i_owner = msg.sender;
    }

    function getFund() public payable {
        require(msg.value.priceConvertor() >= MINIMUM_USD, "Not Enough Eth!!");
        if (addresstoFunders[msg.sender] == 0) {
            Funders.push(msg.sender);
        }
        addresstoFunders[msg.sender] += msg.value ;

    }
    function withdraw() public onlyOwner
     {
        // require(msg.sender == owner, "Not Eligible to withdraw!!!"); // Replaced with modifier
        for(uint256 fundersIndex = 0; fundersIndex < Funders.length; fundersIndex ++){
            address Funder = Funders[fundersIndex];
            addresstoFunders[Funder] = 0;
        }
        // Reset the array
        Funders = new address[] (0);
        // withdrawing the funds
        // three main ways to withdraw the funds
        // transfer
        // payable(msg.sender).transfer(address(this).balance);
        // // send
        // bool sendSuccess = payable(msg.sender).send(address(this).balance);
        // require(sendSuccess, "Send failed");
        // // call
        (bool callSuccess, ) = payable(msg.sender).call{value: address(this).balance}("");
    require(callSuccess, "Call failed");


    }
    modifier onlyOwner() {
    //    require(msg.sender == i_owner, "Not Eligible to withdraw!!!"); 
    if(msg.sender != i_owner){ revert notOwner();}
       _;
    }
    receive() external payable { 
        getFund();
    }
    fallback() external payable {
        getFund();
     }
} 