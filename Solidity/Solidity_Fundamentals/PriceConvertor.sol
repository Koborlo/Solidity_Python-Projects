// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/shared/interfaces/AggregatorV3Interface.sol";
library getConvertor {
        function getPrice() internal  view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface (
            0x694AA1769357215DE4FAC081bf1f309aDC325306
        );
        (, int answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 1e10); // Adjust to 18 decimals
    }

    function priceConvertor(uint256 ethAmount) internal  view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 priceInUsd = (ethPrice * ethAmount) / 1e18;
        return priceInUsd;
    }

}

