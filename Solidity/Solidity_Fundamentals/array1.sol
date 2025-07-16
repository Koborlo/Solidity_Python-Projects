// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
contract SimpleStorage {

   struct Person {
       string name;
       uint256 favoriteNumber;
    }

  // existing code...

 Person[] public  listofperson;

 function addnewPerson(string memory _name, uint256 _favoritenumber)
        external
    {
      require(_favoritenumber >0);

       listofperson.push(Person( _name, _favoritenumber));  //pushing a new instance of 'person'
   }

}