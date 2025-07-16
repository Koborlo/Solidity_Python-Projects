// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {SimpleStorage} from './simplestorage.sol';
contract Five is SimpleStorage {
    uint256 public mynumber;
    
    function store(uint256 _mynumber) public override {
        mynumber = _mynumber + 5;
    }
}
