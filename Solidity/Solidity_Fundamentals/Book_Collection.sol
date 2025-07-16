//  SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;
contract Booklog {
    struct Book {
    string title;
      string  owner;
            uint256 year; 
 }
 Book[] Books;
 function AddBook(string memory _title,string memory _owner,uint256 _year) public{
    // Book memory newbook = Book (_title,_owner,_year);
    Books.push(Book (_title,_owner,_year));
  }
  function ViewBooks() public view returns (Book[]memory){
    return Books;
   }
 
 }
