// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

import {Test, console} from "forge-std/Test.sol";
import {StorageExample} from "../src/StorageExample.sol";

contract StorageExampleTest is Test {
    StorageExample public s;

    function setUp() public {
        s = new StorageExample();
    }
}
