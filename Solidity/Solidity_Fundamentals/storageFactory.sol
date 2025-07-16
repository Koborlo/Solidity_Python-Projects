// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {SimpleStorage} from './SimpleStorage.sol';
contract StorageFactory{
    SimpleStorage[] public newSimplestoragelist;
    function createsimpleStorage() public {
        SimpleStorage storageInstance = new SimpleStorage();
        newSimplestoragelist.push(storageInstance);
    } 
    function sfstore(uint256 _simpleStorageIndex, uint256 _number, string memory _name) public {
        SimpleStorage newsimplestorage = newSimplestoragelist[_simpleStorageIndex];
        newsimplestorage.addperson(_number, _name);
    }
    function sfget(uint256 _simpleStorageIndex) public view returns(SimpleStorage.Person[] memory) {
        SimpleStorage newsimplestorage = newSimplestoragelist[_simpleStorageIndex];
        return newsimplestorage.getlist();
    }
    function sfupdateList( uint256 _simpleStorageIndex, uint256 _personIndex, uint256 _number, string memory _name ) public {
        SimpleStorage newsimplestorage = newSimplestoragelist[_simpleStorageIndex];
        newsimplestorage.updateList(_personIndex, _number, _name);
    }
    function sfdelete(uint256 _simpleStorageIndex, uint256 _personIndex) public {
        SimpleStorage newsimplestorage = newSimplestoragelist[_simpleStorageIndex];
        newsimplestorage.removeperson(_personIndex);
    }
}
