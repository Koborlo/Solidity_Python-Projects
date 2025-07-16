// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
contract SimpleStorage{
    // uint256 favoriteNumber;
    Person[] listofPeople;
    mapping (string => uint256) namesToNumber;
    struct Person {
        uint256 number;
        string name;
    }

    // function store(uint256 _favoriteNumber) public {
    //     favoriteNumber = _favoriteNumber;

    // }
    
    // function retrieve() public view returns (uint256){
    //     return favoriteNumber;
    // }
    function addperson(uint256 _number, string memory _name ) public {
        Person memory newperson = Person(_number,_name);
        listofPeople.push(newperson);
        namesToNumber[_name] = _number;

    }
function updateList(uint256 _index, uint256 _number, string memory _name) public {
    require(_index < listofPeople.length, "Index out of range");
    listofPeople[_index].number = _number;
    listofPeople[_index].name = _name;
}
function removeperson(uint256 _index) public {
    require(_index < listofPeople.length, "Index out of range");
    delete(listofPeople[_index]);
    delete namesToNumber[listofPeople[_index].name]; // ❗ Remove mapping entry too
}

    function getlist() public view returns(Person[]memory) {
        return listofPeople;
    }
    function getPerson (string memory _name/*, uint256 _index*/ ) public view returns (uint256 /*,string memory*/){
        // Person memory names = listofPeople[_index];
        return (namesToNumber[_name]/*, names.name*/);
    }
} 